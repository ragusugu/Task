from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

password = 'Sugan@123'
# Encode the password
encoded_password = quote(password)
#PostgreSQL database URI
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
    finally:
        db.engine.dispose()
    
if __name__ == '__main__':
    app.run(debug=True)