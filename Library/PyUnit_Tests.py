import unittest
from domain.Book import Book
from domain.Client import Client
from Controller.ListController import *
from Controller.RentalController import *
from datetime import *
from Repository.RentalRepo import *
from Repository.Depository import *

class RepoDomainTest(unittest.TestCase):
    '''
    Class for testing the book/client and rentals repositoriesand domains
    '''
    def setUp(self):
        self._book_repo = BookRepository()
        self._client_repo = ClientRepository()
        self._rental_repo = RentalRepository()
        unittest.TestCase.setUp(self)
        
    def test_add(self):
        '''
        testing the add function of both client repo and book repo + rent repo
        also testing return function for rent
        '''
        book1 = Book(0, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
        self._book_repo.add(book1)
        listBooks = self._book_repo.getAll()
        assert len(listBooks) == 1
        assert listBooks[0].get_title() == "Persona 3"
        assert listBooks[0].get_author() == "Shuji Sogabe"
        assert listBooks[0].get_desc() == "3rd entry in the series"
        assert listBooks[0].get_id() == 0
        client1 = Client(1, "Scott Fitzgerald")
        self._client_repo.add(client1)
        listClients = self._client_repo.getAll()
        assert len(listClients) == 1
        assert listClients[0].get_name() == "Scott Fitzgerald"
        self._rental_repo.rent_book(client1, book1, datetime(2018, 11, 3))
        listRent = self._rental_repo.getAll()
        assert len(listRent) == 1
        assert listRent[0].get_clientID() == 1
        assert listRent[0].get_bookID() == 0
        assert listRent[0].get_rentalID() == 0
        assert str(listRent[0].get_rented_date()) == "2018-11-03 00:00:00"
        assert str(listRent[0].get_due_date()) == "2018-11-17 00:00:00"
        assert str(listRent[0].get_return_date()) == "None"
        self._rental_repo.return_book(client1, book1, datetime(2018, 12, 3))
        assert str(listRent[0].get_return_date()) == "2018-12-03 00:00:00"
        
    def test_delete(self):
        '''
        testing the delete function of client, book and rental repositories
        also tests find functions for books/ clients
        '''
        book1 = Book(0, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
        self._book_repo.add(book1)
        book2 = Book(1, "Persona 5", "5th entry in the series", "Atlus")
        self._book_repo.add(book2)
        self._book_repo.remove(book1)
        listBooks = self._book_repo.getAll()
        assert len(listBooks) == 1
        assert listBooks[0].get_title() == "Persona 5"
        assert listBooks[0].get_author() == "Atlus"
        assert listBooks[0].get_desc() == "5th entry in the series"
        assert listBooks[0].get_id() == 1
        try:
            self._book_repo.remove(Book(34, "til", "de", "dw"))
            assert True
        except IndexError:
            pass
        except ValueError:
            pass
        
        assert self._book_repo.find(book1) == False
        assert self._book_repo.find(book2) == True
        assert self._book_repo.find_by_id(book2.get_id()) == book2
            
        client1 = Client(1, "Scott Fitzgerald")
        client2 = Client(2, "Shuji Sogabe")
        self._client_repo.add(client1)
        self._client_repo.add(client2)
        self._client_repo.remove(client1)
        listClients = self._client_repo.getAll() 
        assert len(listClients) == 1
        assert listClients[0].get_name() == "Shuji Sogabe"
        assert listClients[0].get_id() == 2
        try:
            self._client_repo.remove(Client(34, "til"))
            assert True
        except IndexError:
            pass
        except ValueError:
            pass
        
        assert self._client_repo.find(client1) == False
        assert self._client_repo.find(client2) == True
        assert self._client_repo.find(Client(1, "Shuji Sogabe")) == False  
        assert self._client_repo.find_by_id(client2.get_id()) == client2 
        self._rental_repo.rent_book(client1, book1, datetime(2018, 11, 3))
        self._rental_repo.rent_book(client2, book1, datetime(2018, 12, 3))  
        self._rental_repo.delete(self._rental_repo.getAll()[1])
        listRent = self._rental_repo.getAll() 
        assert len(listRent) == 1
        assert listRent[0].get_clientID() == 1
        assert listRent[0].get_bookID() == 0
        assert listRent[0].get_rentalID() == 0
        assert str(listRent[0].get_rented_date()) == "2018-11-03 00:00:00"
        assert str(listRent[0].get_due_date()) == "2018-11-17 00:00:00"
        assert str(listRent[0].get_return_date()) == "None"
        try:
            self._rental_repo.rent_book(client2, book1, datetime(2018, 12, 7)) 
            assert True
        except IndexError:
            pass
        except ValueError:
            pass
    
    def test_domains(self):
        '''
        tests the implicit functions of book, client and rent domains
        '''
        book1 = Book(1, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
        book2 = Book(2, "Persona 5", "5th entry in the series", "Atlus")
        assert book1.get_id() == 1
        assert book2.get_title() == "Persona 5"
        assert book1.get_desc() == "3rd entry in the series"
        assert book2.get_author() == "Atlus"
        assert Book.__str__(book1) == "Persona 3 by Shuji Sogabe described as '3rd entry in the series' with id 1"
        try:
            Book("Five", 5, 324, "Name")
            assert False
        except ValueError:
            pass
        book1.set_id(8)
        book1.set_author("banana")
        book1.set_title("coconut")
        book1.set_desc("fruits")
        assert book1.get_id() == 8
        assert book1.get_desc() == "fruits"
        assert book1.get_author() == "banana"
        assert book1.get_title() == "coconut"
        client1 = Client(1, "Scott Fitzgerald")
        client2 = Client(2, "Shuji Sogabe")
        assert client1.get_id() == 1
        assert client2.get_name() == "Shuji Sogabe"
        assert Client.__str__(client1) == "Scott Fitzgerald with id 1"
        try:
            Client("Five", "Name")
            assert False
        except ValueError:
            pass
        client1.set_id(8)
        client1.set_name("banana")
        assert client1.get_id() == 8
        assert client1.get_name() == "banana"
        rent = Rental(12, 23, 34, datetime(2018, 2, 2), datetime(2018, 2, 16), datetime(2018, 2, 10))
        assert rent.get_bookID() == 23
        assert rent.get_clientID() == 12
        assert rent.get_rentalID() == 34
        assert str(rent.get_due_date()) == "2018-02-16 00:00:00"
        assert str(rent.get_return_date()) == "2018-02-10 00:00:00"
        assert str(rent.get_rented_date()) == "2018-02-02 00:00:00"
        rent.set_bookID(23)
        rent.set_clientID(9)
        rent.set_rentalID(10)
        rent.set_rented_date(datetime(2018, 11, 3))
        rent.set_return_date(datetime(2018, 8, 31))
        rent.set_due_date(datetime(2018, 2, 8))
        assert rent.get_bookID() == 23
        assert rent.get_clientID() == 9
        assert rent.get_rentalID() == 10
        assert str(rent.get_due_date()) == "2018-02-08 00:00:00"
        assert str(rent.get_return_date()) == "2018-08-31 00:00:00"
        assert str(rent.get_rented_date()) == "2018-11-03 00:00:00"
        
class ControllerTest(unittest.TestCase):
    '''
    class for testing the book, client and rent controllers and other associated classes
    '''
    def setUp(self):
        self._controller = Controller(BookRepository(), ClientRepository(), undoController())
        self._service = RentalService(BookRepository(), ClientRepository(), RentalRepository(), undoController())
        unittest.TestCase.setUp(self)
        
    def test_add(self):
        '''
        tests the add function for client and book controller and rent function for rental service
        also the return function for rental service
        '''
        book = Book(0, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
        self._controller.add_book(book)
        listBooks = self._controller._book_repo.getAll()
        assert len(listBooks) == 1
        assert listBooks[0].get_title() == "Persona 3"
        assert listBooks[0].get_author() == "Shuji Sogabe"
        assert listBooks[0].get_desc() == "3rd entry in the series"
        assert listBooks[0].get_id() == 0
        client1 = Client(1, "Scott Fitzgerald")
        self._controller.add_client(client1)
        listClients = self._controller._client_repo.getAll()
        assert len(listClients) == 1
        assert listClients[0].get_name() == "Scott Fitzgerald" 
        self._service.rent(book, client1, datetime(2018, 11, 3))
        listRent = self._service._rent_repo.getAll()
        assert len(listRent) == 2
        assert listRent[0].get_clientID() == 1
        assert listRent[0].get_bookID() == 0
        assert listRent[0].get_rentalID() == 0
        assert str(listRent[0].get_rented_date()) == "2018-11-03 00:00:00"
        assert str(listRent[0].get_due_date()) == "2018-11-17 00:00:00"
        assert str(listRent[0].get_return_date()) == "None"
        self._service.return_book(book, client1, datetime(2018, 12, 3))
        listRent = self._service._rent_repo.getAll()
        assert str(listRent[0].get_return_date()) == "2018-12-03 00:00:00"
        
    def testSearchAvailable(self):
        '''
        tests search function for client/book and available function for rentals
        '''
        book = Book(0, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
        self._controller.add_book(book)
        client = Client(1, "Scott Fitzgerald")
        self._controller.add_client(client)
        self._service.rent(book, client, datetime(2018, 11, 3))
        assert self._controller.parse_search_word("pErSoNa") == "persona"
        assert self._controller.parse_search_word(5) == 5
        assert self._service.available_book(book, datetime(2018, 11, 3), datetime(2018, 12, 3)) == False
        self._service.return_book(book, client, datetime(2018, 12, 3))
        assert self._service.available_book(book, datetime(2019, 12, 4), datetime(2019, 12, 23)) == False
        
    
if __name__ == "__main__":
    unittest.main()

        
        