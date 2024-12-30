from flask_login import UserMixin
from app import db
class teammates(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.LargeBinary(60), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def is_active(self):
        return self.active

    def __repr__(self):
        return f'<User {self.name}>'