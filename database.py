from flask_sqlalchemy import SQLAlchemy
from app import app
from constants.names import DATABASE_URL, DATABASE_TRACK_MODIFICATIONS
from hashlib import md5

# configuration
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DATABASE_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

