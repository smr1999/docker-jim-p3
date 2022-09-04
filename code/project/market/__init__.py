from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from market.config import Development,Production

app = Flask(__name__)

if os.environ.get('DEBUG') == '1':
    app.config.from_object(Development)
else:
    app.config.from_object(Production)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = "login_page"
login.login_message_category = "info"

from market import routes,models