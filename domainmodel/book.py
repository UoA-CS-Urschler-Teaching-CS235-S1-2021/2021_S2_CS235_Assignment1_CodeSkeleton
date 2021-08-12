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
    def publisher(self):
        return self.__publisher
    
    @publisher.setter
    def publisher(self, pub):
        self.__publisher = pub
    
    @property
    def authors(self):
        return self.__authors
    
    @authors.setter
    def authors(self, au):
        self.__authors = au
    
    def __repr__(self):
        return f"<Book {self.__book_title}, book id = {self.__book_id}>"
    
    def _eq__(self):


    def __lt__(self): 
    def __hash__(self): 
    def add_author(author): 