from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conn import create_app


app = Flask(__name__)
app = create_app()
db = SQLAlchemy()
db.init_app(app)

class Refresh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_count = db.Column(db.Integer)
    avg_row_count=db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

@app.route('/refresh', methods=['POST'])  
def refresh():
    # Get parameters from the request
    new_row_count = int(request.json['new_row_count'])
    metric_threshold = float(request.json['metric_threshold'])
    window_size = int(request.json['window_size'])

    # Calculate row count drift
    row_count_drift, avg_row_count = calculate_row_count_drift(window_size,new_row_count)
    # Store the parameters in the database
    refresh_entry = Refresh(row_count=new_row_count,avg_row_count=avg_row_count)
    db.session.add(refresh_entry)
    db.session.commit()

    # Check if it violates metric threshold
    if abs(row_count_drift) > metric_threshold:
        violation_message = f"Row count drift exceeds the threshold: {row_count_drift}%"
    else:
        violation_message = None

    return jsonify({
        'row_count_drift': row_count_drift,
        'violation_message': violation_message
    })

def calculate_row_count_drift(window_size,row_count):
    # Retrieve row counts for the specified window size
    recent_refreshes = Refresh.query.order_by(Refresh.timestamp.desc()).limit(window_size).all()
    row_counts = [refresh.row_count for refresh in recent_refreshes]
    prev_row_count = [refresh.avg_row_count for refresh in recent_refreshes]
    if len(row_counts) ==0:  
        avg_row_count=row_count
        row_count_drift=0
        return row_count_drift, avg_row_count

    if len(row_counts) == window_size:
        row_counts.pop(-1)
    row_counts.append(row_count)
    avg_row_count = sum(row_counts) / len(row_counts)
     
    prev_row_count = prev_row_count[0]
    row_count_drift = ((row_count - prev_row_count) / prev_row_count) * 100

    return row_count_drift, avg_row_count

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
