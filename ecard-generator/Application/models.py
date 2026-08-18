from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(32), default="general", nullable=False)
    details = db.relationship("Info", backref="creator", lazy=True, cascade="all, delete-orphan")


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute_name = db.Column(db.String(120), nullable=False)
    attribute_value = db.Column(db.Text, nullable=False)
    card_name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
