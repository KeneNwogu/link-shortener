##### HANDLES ALL DATABASE ACTIONS #####
from app import db

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_url = db.Column(db.String(200), unique=True, nullable=False)
    short_url = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.full_url}: {self.short_url}"