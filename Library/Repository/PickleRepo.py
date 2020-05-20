from Repository.Depository import *
from domain.Book import *
from domain.Client import *
from domain.Rental import *
from Repository.RentalRepo import *
import pickle

class RentalPickleRepo(RentalRepository):
    def __init__(self, filename = "rents.txt"):
        RentalRepository.__init__(self)
        self._filename = filename
        self._loadFile()
    
    def _loadFile(self):
        try:
            f = open(self._filename, "rb")
            while True:
                try:
                    rent = pickle.load(f)
                    client = Client(rent.get_clientID(), "")
                    book = Book(rent.get_bookID(), "", "", "")
                    RentalRepository.rent_book(self, client, book, rent.get_rented_date())
                    RentalRepository.return_book(self, client, book, rent.get_return_date())
                except EOFError:
                    break
        except IOError:
            raise Exception("Invalid file... :(")
        finally:
            f.close()
            
        
    def rent_book(self, client, book, date):
        '''
        adds a new entry in the rental repo then saves it to the file
        '''
        RentalRepository.rent_book(self, client, book, date)
        self._saveFile()
        
    def return_book(self, client, book, date):
        '''
        adds a return date to a rental entry and then saves it to the file
        '''
        RentalRepository.return_book(self, client, book, date)
        self._saveFile()
        
    def delete(self, rent):
        '''
        deletes an entry from the repository and tehn updates the file
        '''
        RentalRepository.delete(self, rent)
        self._saveFile()
    
    def _saveFile(self):
        '''
        saves a binary file
        '''
        f = open(self._filename, "wb")
        for rent in self.getAll():
            pickle.dump(rent, f)