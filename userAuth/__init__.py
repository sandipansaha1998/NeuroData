from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.update(dict(
    SECRET_KEY='1acc8e0196e8403fdd23e4502051937a',
    WTF_CSRF_SECRET_KEY='1acc8e0196e8403fdd23e4502051937a'
))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from userAuth import routes


