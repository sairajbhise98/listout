"""
     Table : account
"""
from database import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    profile_name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(20))
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.String(20), nullable=False)
    business_name = db.Column(db.String(200))







