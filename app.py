import os
from flask import Flask


DB_URL = os.getenv("DB_URL", 'mysql+pymysql://root:123456@127.0.0.1:3306/myBlog')
SECRET_KEY = os.getenv("SECRET_KEY", '42a185930e20453aa62b88e16ef4cf48')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'

from controller import *
from models import *