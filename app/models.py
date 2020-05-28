from app import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime)


class BooksCrash(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_book = db.Column(db.Integer)
    book_name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime)
