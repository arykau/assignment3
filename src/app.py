from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import jwt
from sqlalchemy.sql.schema import Column
from werkzeug.security import check_password_hash
import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '7xKlb34rb5wWRYM36wte'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:020716@localhost:5432/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    token = db.Column(db.Text)

    def __init__(self,email,password,token):
        self.email = email
        self.password = password
        self.token = token

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        auth = request.authorization
        callable(auth)
        token = token = jwt.encode({'email' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY']);        
        user = User(email = auth.username,password = auth.password,token = token)
        db.session.add(user)
        db.session.commit()
        result = 'token:' + token
        return result
    else:
        return 'Welcome to the register page'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        auth = request.authorization
        callable(auth)
        user = db.session.query(User).filter_by(email = auth.username).first()
        if user:
            if db.session.query(User).filter_by(password = auth.password).first():
                token = token = jwt.encode({'email' : user.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])       
                result = 'token:' + token
                return result
        else:
            return 'Something is invalid!'
    else:
        return 'Welcome to the login page'

@app.route('/protected/<token>',methods=['POST','GET'])
def protected(token):
    if request.method == 'POST':
        user = db.session.query(User).filter_by(token=token).first()
        if user:
            return '<h1>Hello, token which is provided is correct</h1>';
        else:
            return '<h1>Hello, Could not verify the token </h1>'
        
    else:
        return 'Welcome to the protected page'


if __name__ == '__main__':
    app.run(debug=True, port=8080)