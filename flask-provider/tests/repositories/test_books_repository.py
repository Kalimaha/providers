from provider.repositories.books_repository import BooksRepository as r


def test_get():
    assert r.get(42).title == 'The Hitchhicker\'s Guide to the Galaxy'
