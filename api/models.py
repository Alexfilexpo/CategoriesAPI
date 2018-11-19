from api import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    path = db.Column(db.String(50), default=' ', nullable=False)