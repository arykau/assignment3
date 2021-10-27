Database should store login, password and token issued to user during the authentication

-Installation:
pip install flask
pip install flask_sqlalchemy 
pip install jwt
pip install request

-Usage:
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import jwt
from sqlalchemy.sql.schema import Column
from werkzeug.security import check_password_hash
import datetime
import uuid

-Example:
/login
After successful login( if login and password matches with a record in User Table), as response route should return html text: token: <token value> and store that token in the User Table
If provided login and password does not exist in the User Table, as a response route should return html text: Could not found a user with login: <login>
/protected
This route should receive as a parameter token value
Token value needs to be passed over URL, 
e.g. http://127.0.01:5000/protected?token=24230ifdsjfjdsklfj43943ut943
This route should return html text: <h1>Hello, token which is provided is correct </h1>, if as a parameter RIGHT token value is passed
This route should return html text: <h1>Hello, Could not verify the token </h1>, if as a parameter WRONG token value is passed
![image](https://user-images.githubusercontent.com/74668998/139093501-402458dc-6851-407b-a111-96200834848e.png)
