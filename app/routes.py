from app import app, db, request, Response
from datetime import datetime
import json
from app.models import Books, BooksTrash


@app.route('/create-book', methods=['POST'])
def create_book():
    if request.method == 'POST':
        data = request.get_json()
        book = Books(book_name=data['book_name'],
                     author=data['author'],
                     rating=data['rating'],
                     date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
                     )
        db.session.add(book)
        db.session.flush()
        db.session.commit()
        data = {
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "rating": book.rating,
            "date": book.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        return Response(response=json.dumps(data, ensure_ascii=False),
                        headers={'Location': f'/read-users/{book.id}'},
                        status=201,
                        mimetype='application/json')


@app.route('/get-books/', defaults={"book_id": None}, methods=['GET'])
@app.route('/get-books/<book_id>', methods=['GET'])
def read_book(book_id):
    if request.method == 'GET':
        if book_id:
            book = Books.query.filter_by(id=book_id).first()
            data = {
                "id": book.id,
                "book_name": book.book_name,
                "author": book.author,
                "rating": book.rating,
                "date": book.date.strftime('%Y-%m-%d %H:%M:%S')
            }
            return Response(response=json.dumps(data, ensure_ascii=False),
                            status=200,
                            mimetype='application/json'
                            )
        else:
            all_books = Books.query.all()
            data = [
                {
                    "id": book.id,
                    "book_name": book.book_name,
                    "author": book.author,
                    "rating": book.rating,
                    "date": book.date.strftime('%Y-%m-%d %H:%M:%S')
                }
                for book in all_books]
            data = {"data": data}
            return Response(response=json.dumps(data, ensure_ascii=False),
                            status=200,
                            mimetype='application/json')


@app.route('/update-book/<book_id>', methods=['PATCH'])
def update_book(book_id):
    if request.method == 'PATCH':
        rating = request.get_json()
        book = Books.query.filter_by(id=book_id).first()
        book.rating = rating['rating']
        db.session.commit()
        data = {
                "id": book.id,
                "book_name": book.book_name,
                "author": book.author,
                "rating": book.rating,
                "date": book.date.strftime('%Y-%m-%d %H:%M:%S')
            }
        return Response(response=json.dumps(data, ensure_ascii=False),
                        status=200,
                        mimetype='application/json')


@app.route('/delete-book/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    if request.method == 'DELETE':
        book = Books.query.filter_by(id=book_id).first()
        Books.query.filter_by(id=book_id).delete()
        data = BooksTrash(
            book_id=book_id,
            book_name=book.book_name,
            author=book.author,
            rating=book.rating,
            date=book.date
        )
        db.session.add(data)
        db.session.delete(book)
        db.session.commit()
        return Response(status=204,
                        mimetype='application/json')


@app.route('/get-trash', methods=['GET'])
def read_trash():
    if request.method == 'GET':
        trash_resource = BooksTrash.query.all()
        data = [
            {
                "id": trash.id,
                "book_id": trash.book_id,
                "book_name": trash.book_name,
                "author": trash.author,
                "rating": trash.rating,
                "date": trash.date.strftime('%Y-%m-%d %H:%M:%S')
            }
            for trash in trash_resource]
        data = {"data": data}
        print(data)
        return Response(response=json.dumps(data, ensure_ascii=False),
                        status=200,
                        mimetype='application/json')

