from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

password = 'Sugan@123'
# Encode the password
encoded_password = quote(password)
#PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{encoded_password}@localhost/sugan'
db = SQLAlchemy(app)


class Metrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    window_size = db.Column(db.Integer, nullable=False)
    metric_threshold = db.Column(db.Float, nullable=False)
    base_row_count = db.Column(db.Integer, default=0)

class RefreshHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    refresh_number = db.Column(db.Integer, nullable=False)
    row_count = db.Column(db.Integer, nullable=False)
    moving_average = db.Column(db.Float)
    metrics_id = db.Column(db.Integer, db.ForeignKey('metrics.id'), nullable=False)
    metrics = db.relationship('Metrics', backref=db.backref('refresh_history', lazy=True))

# Create the tables within the context of the application
with app.app_context():
    db.create_all()

def calculate_percentage_diff(incremental_row_count, prev_moving_average):
    if prev_moving_average == 0:
        return 0  # Avoid division by zero

    return ((incremental_row_count - prev_moving_average) / prev_moving_average) * 100

@app.route('/update_metrics', methods=['POST'])
def update_metrics():
    data = request.get_json()

    window_size = data.get('window_size')
    metric_threshold = data.get('metric_threshold')

    # Validate inputs
    if not all(isinstance(param, int) for param in [window_size]) or not (0 <= metric_threshold <= 100):
        return jsonify({'error': 'Invalid parameters'}), 400

    metrics = Metrics(window_size=window_size, metric_threshold=metric_threshold)
    db.session.add(metrics)
    db.session.commit()

    return jsonify({'message': 'Metrics updated successfully'}), 201

@app.route('/refresh', methods=['POST'])
def refresh():
    data = request.get_json()

    metrics_id = data.get('metrics_id')
    row_count = data.get('row_count')

    metrics = Metrics.query.get(metrics_id)
    if not metrics:
        return jsonify({'error': 'Metrics not found'}), 404

    refresh_number = len(metrics.refresh_history) + 1

    # Calculate moving average
    incremental_row_count = row_count - metrics.base_row_count
    prev_moving_average = 0 if len(metrics.refresh_history) == 0 else metrics.refresh_history[-1].moving_average
    moving_average = (prev_moving_average * len(metrics.refresh_history) + incremental_row_count) / refresh_number

    # Calculate percentage difference
    percentage_diff = calculate_percentage_diff(incremental_row_count, prev_moving_average)

    # Update metrics and refresh history
    metrics.base_row_count = row_count
    refresh_history = RefreshHistory(refresh_number=refresh_number, row_count=row_count, metrics=metrics, moving_average=moving_average)
    db.session.add(refresh_history)
    db.session.commit()

    # Check if threshold is violated
    if abs(percentage_diff) > metrics.metric_threshold:
        return jsonify({'message': 'Refresh recorded successfully. Threshold violated!'}), 201

    return jsonify({'message': 'Refresh recorded successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
