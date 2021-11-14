"""
     Table : account
"""
from database import db


class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    profile_name = db.Column(db.String(20))
    password = db.Column(db.String(20))

