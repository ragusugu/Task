from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

# Securely store sensitive information like passwords
password = 'Sugan@123'
encoded_password = quote(password)
# PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{encoded_password}@localhost/sugan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

@app.route('/')
def hello_world():
 try:
     db.engine.connect()
     return 'Connected to PostgreSQL!'
 except Exception as e:
     return f'Error connecting to PostgreSQL: {str(e)}'

class employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)



@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a+b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide numeric values for "a" and "b"'})

@app.route('/get_user', methods=['GET'])
def get_users():
    try:
        employees_list = []
        employees_data = employees.query.all()
        for employee in employees_data:
            employees_list.append({
                'id': employee.employee_id,
                'fname': employee.first_name,
                'lname': employee.last_name,
                'email': employee.email
            })
        return jsonify({'employees': employees_list})
    except Exception as e:
        return jsonify({'error': f'Error retrieving users: {str(e)}'}), 500  # HTTP 500 for internal server error

@app.route('/compute_net_amount', methods=['POST'])
def compute_net_amount():
    try:
        data = request.get_json()

        # Extract input values
        net_amount = data.get('net_amount', 0)
        mode = data.get('mode', '')
        amount = data.get('amount', 0)

        # Perform computation based on the transaction mode
        if mode.lower() == 'deposit':
            net_amount += amount
        elif mode.lower() == 'withdraw':
            net_amount -= amount
        else:
            return jsonify({'error': 'Invalid transaction mode. Use "deposit" or "withdraw".'}), 400

        return jsonify({'net_amount': net_amount})
    except Exception as e:
        return jsonify({'error': f'Error processing the request: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
