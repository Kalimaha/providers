from json import dumps
from json import loads
from flask import Flask
from provider.controllers.application_controller import app


def test_get_book():
    # app = Flask(__name__)
    # app.register_blueprint(books_blueprint, url_prefix='/books')
    tester = app.test_client()
    response = tester.get('/books/42/')
    json = loads(response.data.decode('utf-8'))

    title = "The Hitchhicker's Guide to the Galaxy"
    expected_json = {"id": 42, 'title': title}

    assert json == expected_json


def test_get_books():
    # app = Flask(__name__)
    # app.register_blueprint(books_blueprint, url_prefix='/books')
    tester = app.test_client()
    response = tester.get('/books/')
    json = loads(response.data.decode('utf-8'))

    title = "The Hitchhiker's Guide to the Galaxy"
    expected_json = [{'id': 42, 'title': title}]

    assert json == expected_json
