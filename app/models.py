from app import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime)


class BooksTrash(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer)
    book_name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime)
