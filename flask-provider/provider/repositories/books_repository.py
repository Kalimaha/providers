from provider.models.book import Book


class BooksRepository(object):
    @staticmethod
    def get(id):
        if int(id) is 42:
            return Book('The Hitchhicker\'s Guide to the Galaxy')
        return Book('Just a book')
