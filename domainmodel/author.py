class Author:
    def __init__(self, author_id, author_full_name):
        self.__authorlist = []
        if(isinstance(author_id, int) and author_id>=0 and author_id != None):
            self.__unique_id = author_id
        else:
            raise ValueError()
        
        if(isinstance(author_full_name, str) and len(author_full_name.strip())>0 and author_full_name != None):
            self.__full_name = author_full_name
        else:
            raise ValueError()
    
    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, author_full_name):
        if(isinstance(author_full_name, str) and len(author_full_name.strip())>0 and author_full_name != None):
            self.__full_name = author_full_name
        else:
            raise ValueError()
    
    @property   
    def unique_id(self):
        return self.__unique_id
    
    def __repr__(self):
        return f'<Author {self.__full_name}, author id = {self.__unique_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__unique_id == self.__unique_id

    def __lt__(self, other):
        return self.__unique_id < other.__unique_id

    def __hash__(self):
        return hash(self.__unique_id)
    
    def add_coauthor(self, coauthor):
        if coauthor not in self.__authorlist:
            self.__authorlist.append(coauthor)
            coauthor.__authorlist.append(self)
            
    def check_if_this_author_coauthored_with(self, author):
        return author in self.__authorlist