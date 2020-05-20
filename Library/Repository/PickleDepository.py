from Repository.Depository import *
import pickle

class BookPickleRepository(BookRepository):
    def __init__(self, filename = "books.txt"):
        BookRepository.__init__(self)
        self._filename = filename
        self._loadFile()
        
    def _loadFile(self):
        try:
            f = open(self._filename, "rb")
            while True:
                try:
                    book = pickle.load(f)
                    BookRepository.add(self, book)
                except EOFError:
                    break
        except IOError:
            raise Exception("Invalid file... :(")
        finally:
            f.close()
    
    def add(self, book):
        '''
        adds a new book to the memory repo then saves it to the file
        '''
        BookRepository.add(self, book)
        self._saveFile()
        
    def remove(self, book):
        '''
        removes a book from the memory repo then saves it to the file
        '''
        BookRepository.remove(self, book)
        self._saveFile()
        
    def update(self, book):
        '''
        updates the information of a book then saves it to the file
        '''
        BookRepository.update(self, book)
        self._saveFile()
        
    def _saveFile(self):
        '''
        saves a binary file
        '''
        f = open(self._filename, "wb")
        for book in self.getAll():
            pickle.dump(book, f)

class ClientPickleRepository(ClientRepository):
    def __init__(self, filename = "clients.txt"):
        ClientRepository.__init__(self)
        self._filename = filename
        self._loadFile()
        
    def _loadFile(self):
        try:
            f = open(self._filename, "rb")
            while True:
                try:
                    client = pickle.load(f)
                    ClientRepository.add(self, client)
                except EOFError:
                    break
        except IOError:
            raise Exception("Invalid file... :(")
        finally:
            f.close()
            
    def add(self, client):
        '''
        adds a new client to the memory repo then saves it to the file
        '''
        ClientRepository.add(self, client)
        self._saveFile()
        
    def remove(self, client):
        '''
        removes a client from the memory repo then saves it to the file
        '''
        ClientRepository.remove(self, client)
        self._saveFile()
        
    def update(self, client):
        '''
        updates the information of a client then saves it to the file
        '''
        ClientRepository.update(self, client)
        self._saveFile()
    
            
    def _saveFile(self):
        '''
        saves a binary file
        '''
        f = open(self._filename, "wb")
        for client in self.getAll():
            pickle.dump(client, f)

    