from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = "147852369147852"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/firstapp"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db=SQLAlchemy(app)
login_manager = LoginManager(app)

from micro import routes