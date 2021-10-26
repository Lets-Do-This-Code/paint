from app import db
from datetime import datetime

class client(db.Model):
    custID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False) 


    def __repr__(self):
        return '<Client {}>'.format(self.name)