from database import db
from .accounts import Account
from .connections import Connection


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    connection_id = db.Column(db.Integer, db.ForeignKey("connection.id"), nullable=False)
    connection_name = db.Column(db.String(200), db.ForeignKey("connection.name"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    status = db.Column(db.String(10))
    created_at = db.Column(db.String(10))
