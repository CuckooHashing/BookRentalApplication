class Book:
    '''
    instance of this class represents a book with bookId, title, description, author
    '''
    
    def __init__(self, ID, titles, description, authors):
        '''
        creates a book with the given parameters
        '''
        try:
            self._id = int(ID)
            self._title = titles
            self._desc = description
            self._author = authors
        except ValueError:
            raise ValueError("Invalid entry... :(")

    def get_id(self):
        return self._id
    def get_title(self):
        return self._title
    def get_desc(self):
        return self._desc
    def get_author(self):
        return self._author
    
    def set_id(self, id):
        self._id = id
    def set_title(self, title):
        self._title = title
    def set_desc(self, desc):
        self._desc = desc
    def set_author(self, author):
        self._author = author
        
    def __str__(self):
        return str(self._title) + " by " + str(self._author) + " described as '" + str(self._desc) + "' with id "+ str(self._id) 
