class Client:
    '''
    instance of this class represents a book with bookId, title, description, author
    '''
    
    def __init__(self, ID, names):
        '''
        creates a book with the given parameters
        '''
        try:
            self._id = int(ID)
            self._name = names
        except ValueError:
            raise ValueError("Invalid entry... :(")
    
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def set_id(self, id):
        self._id = id
    def set_name(self, name):
        self._name = name
        
    def __str__(self):
        return str(self._name) + " with id " + str(self._id)
        
