from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from sqlalchemy.exc import IntegrityError
from flask import redirect

app = Flask(__name__)

password = 'Sugan@123'
# Encode the password
encoded_password = quote(password)
# PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{encoded_password}@localhost/sugan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Define Employee model
class Employee1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the tables within the context of the application
with app.app_context():
    db.create_all()

# Render the HTML form
@app.route('/')
def add_employee_form():
    return render_template('index.html')

# # API to add employee details
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    id = data['id']
    name = data['name']
    email = data['email']

    try:
        new_employee = Employee1(id=id, name=name, email=email)
        db.session.add(new_employee)
        db.session.commit()
        
        # Assuming you have a template 'success.html' for successful addition
        return redirect('http://127.0.0.1:5000/employees')
    
    except IntegrityError as ie:
        db.session.rollback()
        return jsonify({'error': 'Integrity error: Employee already exists'}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# API to get all employee details
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee1.query.all()
    employee_list = []
    for employee in employees:
        employee_data = {'id': employee.id, 'name': employee.name, 'email': employee.email}
        employee_list.append(employee_data)
    return render_template('table.html', employees=employees)

# API to update employee details
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee1.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404

    data = request.get_json()
    employee.name = data['name']
    employee.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Employee updated successfully'})

# API to delete employee details
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee1.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
