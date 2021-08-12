import pytest

from domainmodel.publisher import Publisher

class TestPublisher:

    def test_construction(self):
        publisher1 = Publisher("Avatar Press")
        assert str(publisher1) == "<Publisher Avatar Press>"
        publisher2 = Publisher("  ")
        assert str(publisher2) == "<Publisher N/A>"
        publisher3 = Publisher("  DC Comics ")
        assert str(publisher3) == "<Publisher DC Comics>"
        publisher4 = Publisher(42)
        assert str(publisher4) == "<Publisher N/A>"

class TestBook:
    def test_construction(self):
        book = Book(84765876, "Harry Potter")
        assert str(book) == "<Book Harry Potter, book id = 84765876>"

        publisher = Publisher("Bloomsbury")
        book.publisher = publisher
        print(book.publisher)

        author = Author(635, "J.K. Rowling")
        book.add_author(author)
        print(book.authors)
