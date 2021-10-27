#Database should store login, password and token issued to user during the authentication

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
