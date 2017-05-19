from provider.models.book import Book


def test_book():
    title = 'The Hitchhicker\'s Guide to the Galaxy'
    b = Book(title)
    assert b.title == title
