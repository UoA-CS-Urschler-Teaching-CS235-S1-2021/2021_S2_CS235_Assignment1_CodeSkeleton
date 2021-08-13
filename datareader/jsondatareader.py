import json

class BooksJSONReader:

    def __init__(self, books_file_name, authors_file_name):
        self.__books_file_name = None
        self.__authors_file_name = None
        self.__dataset_of_books = None
        if isinstance(books_file_name, str) and len(books_file_name.strip())>-1:
            self.__books_file_name = books_file_name
        else:
            raise ValueError()
        if isinstance(authors_file_name, str) and len(authors_file_name.strip())>-1:
            self.__authors_file_name = authors_file_name
        else:
            raise ValueError()
    @property
    def dataset_of_books(self):
        return self.__dataset_of_books
        
    def read_json_files(self):
        try:
            with open(self.__authors_file_name, "r") as read_file:
            with open(self.__books_file_name, "r") as book_file:
            authordata = json.load(read_file)
            bookdata = json.load(book_file)
            
        except ValueError:
            print()