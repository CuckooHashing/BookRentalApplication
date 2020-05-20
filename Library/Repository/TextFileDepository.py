from domain.Book import *
from domain.Client import *
from builtins import ValueError
from Repository.Depository import *

class BookTextFileRepo(BookRepository):
    def __init__(self, filename = "books.txt"):
        BookRepository.__init__(self)
        self._filename = filename
        self._loadFile()
    
    def _loadFile(self):
        '''
        loads the repo file
        '''
        try:
            f = open(self._filename, "r")
            
            line = f.readline()
            while len(line) > 2:
                tok = line.split(",")
                book = Book(int(tok[0]), tok[1], tok[2], tok[3].strip())
                BookRepository.add(self, book)
                line = f.readline()
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
        saves the repo to the file
        '''
        try:
            f = open(self._filename, "w")
            for b in self.getAll():
                f.write(str(b.get_id()) + "," + str(b.get_title()) + "," + str(b.get_desc()) + "," + str(b.get_author()) +"\n")
        except IOError:
            raise Exception("Cannot write to file... :(")
        finally:
            f.close()

class ClientTextFileRepo(ClientRepository):
    def __init__(self, filename = "clients.txt"):
        ClientRepository.__init__(self)
        self._filename = filename
        self._loadFile()
    
    def _loadFile(self):
        '''
        loads the repo file
        '''
        try:
        
            f = open(self._filename, "r")
            
            line = f.readline()
            while len(line) > 2:
                tok = line.split(",")
                client = Client(int(tok[0]), tok[1].strip())
                ClientRepository.add(self, client)
                line = f.readline()
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
        saves the repo to the file
        '''
        try:
            f = open(self._filename, "w")
            for b in self.getAll():
                f.write(str(b.get_id()) + "," + str(b.get_name()) + "\n")
        except IOError:
            raise Exception("Cannot write to file... :(")
        finally:
            f.close()
