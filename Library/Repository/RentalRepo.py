from Repository.Depository import *
from domain.Book import *
from domain.Client import *
from domain.Rental import *
from datetime import *
from Repository.Iterable import *
class RentalRepository(Iterator):
    
    def __init__(self):
        '''
        initialises a list of rental data
        '''
        self._repo = []
        Iterator.__init__(self)
        
    def delete(self, rent):
        '''
        deletes a rental
        '''
        for i in self._repo:
            if i.get_rentalID() == rent.get_rentalID():
                self._repo.remove(i)
                Iterator.__delitem__(self, self._repo.index(i))
        
    def getAll(self):
        '''
        gets a list of rentals
        '''
        return self._repo
    
    def rent_book (self, client, book, date):
        '''
        'rents a book': basically adds a new entry to the rental list
        '''
        self._repo.append(Rental(client.get_id(), book.get_id(), len(self._repo), date, date + timedelta(days = 14), None))
        Iterator.addaos(self, Rental(client.get_id(), book.get_id(), len(self._repo), date, date + timedelta(days = 14), None))
        
    def return_book(self, client, book, date):
        '''
        sets the returned date of a book. thus the book is 'returned'
        '''
        index = 0
        ok = False
        for i in self._repo:
            if book.get_id() == i.get_bookID() and client.get_id() == i.get_clientID():
                i.set_return_date(date)
                Iterator.__setitem__(self, i, index)
                return 
            index += 1
        if ok == False:
            raise IndexError("Rental not found... :(")
        
def test_repo():
    client1 = Client(1, "Scott Fitzgerald")
    book1 = Book(1, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
    book2 = Book(2, "Persona 5", "5th entry in the series", "Atlus")
    
    repo = RentalRepository()
    
    repo.rent_book(client1, book1, datetime(2018, 11, 3))
    listRent = repo.getAll()
    
    assert len(listRent) == 1
    assert listRent[0].get_clientID() == 1
    assert listRent[0].get_bookID() == 1
    assert listRent[0].get_rentalID() == 0
    assert str(listRent[0].get_rented_date()) == "2018-11-03 00:00:00"
    assert str(listRent[0].get_due_date()) == "2018-11-17 00:00:00"
    assert str(listRent[0].get_return_date()) == "None"
    
    repo.return_book(client1, book1, datetime(2018, 11, 10))
    listRent = repo.getAll()
    
    #assert listRent[0].get_return_date() == "2018-11-10 00:00:00"
    
    
    
test_repo()