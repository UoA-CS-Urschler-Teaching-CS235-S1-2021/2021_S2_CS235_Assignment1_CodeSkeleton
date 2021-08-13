from domainmodel.publisher import Publisher
from domainmodel.author import Author
class Book:
    def __init__(self, id, title):
        if isinstance(id, int) and id >=0:
            self.__book_id = id
        else:
            raise ValueError()
        if isinstance(title, str) and len(title.strip()) >0:
            self.__book_title = title
        else:
            raise ValueError()
        self.__publisher = None
        self.__description = None
        self.__authors = []
        self.__release_year = None
        self.__ebook = False
    
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__book_title
    
    @title.setter
    def title(self, t):
        if isinstance(t, str) and len(t.strip()) >0:
            self.__book_title = t
        else:
            raise ValueError()
    
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        if isinstance(d, str) and len(d.strip()) >0:
            self.__description = d.strip()

    @property
    def publisher(self):
        return self.__publisher
    
    @publisher.setter
    def publisher(self, pub):
        if isinstance(pub, Publisher):
            self.__publisher = pub
    
    @property
    def authors(self):
        return self.__authors
    
    @authors.setter
    def authors(self, au):
        self.__authors = au
    
    @property
    def release_year(self):
        return self.__release_year
    
    @release_year.setter
    def release_year(self, r):
        if isinstance(r, int) and r>-1:
            self.__release_year = r
        else:
            raise ValueError()

    @property
    def ebook(self):
        return self.__ebook
    
    @ebook.setter
    def ebook(self, e):
        if isinstance(e, bool):
            self.__ebook = e

    def __repr__(self):
        return f"<Book {self.__book_title}, book id = {self.__book_id}>"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__book_id == self.__book_id

    def __lt__(self, other): 
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)
    def add_author(self, author):
        if isinstance(author, Author) and author not in self.__authors:
            self.__authors.append(author)
    def remove_author(self, author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)