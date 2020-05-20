from Repository.Depository import *
from domain.Book import *
from domain.Client import *
from domain.Rental import *
from Repository.RentalRepo import *
from datetime import datetime

class RentalTextFileRepo(RentalRepository):
    def __init__(self, filename = "rents.txt"):
        RentalRepository.__init__(self)
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
                date = datetime.strptime(tok[3], '%Y-%m-%d %H:%M:%S')
                '''
                yeah, month, day = map(int, tok[3].split("-"))
                date = datetime.date(yeah, month, day)
                '''
                book = Book(int(tok[1]), "", "", "")
                client = Client(int(tok[0]), "")
                ret = tok[4].strip()
                RentalRepository.rent_book(self, client, book, date)
                if str(ret) != "None":
                    '''
                    yeah, month, day = map(int, ret.split("/"))
                    date = datetime.date(yeah, month, day)
                    '''
                    date = datetime.strptime(ret, '%Y-%m-%d %H:%M:%S')
                    RentalRepository.return_book(self, client, book, date)
                line = f.readline()
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
        saves the repo to the file
        '''
        try:
            f = open(self._filename, "w")
            for b in self.getAll():
                f.write(str(b.get_clientID()) + "," + str(b.get_bookID()) + "," + str(b.get_rented_date()) + "," + str(b.get_due_date()) + "," + str(b.get_return_date()) + "\n")
        except IOError:
            raise Exception("Cannot write to file... :(")
        finally:
            f.close()
