from database import db


class Connection(db.Model):
    connection_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)



