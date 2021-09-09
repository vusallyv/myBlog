from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/myBlog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'

from controller import *
from models import *

if __name__=='__main__':
    app.run(port=5000, debug=True)