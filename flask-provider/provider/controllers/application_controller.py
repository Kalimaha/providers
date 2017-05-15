from flask import Flask
from flask import jsonify
from provider.controllers.books_controller import books_blueprint


app = Flask(__name__)
app.register_blueprint(books_blueprint, url_prefix='/books')


if __name__ == '__main__':
    app.run()
