from flask import Blueprint
from json import dumps
from provider.repositories.books_repository import BooksRepository


books_blueprint = Blueprint('books', __name__)


@books_blueprint.route('/')
def books_service():
    out = [
        {
            'id': 42,
            'title': 'The Hitchhiker\'s Guide to the Galaxy'
        }
    ]
    return dumps(out)


@books_blueprint.route('/<id>/')
def book_service(id):
    book = BooksRepository.get(id)
    out = {
        'id': book.id,
        'title': book.title
    }
    return dumps(out)
