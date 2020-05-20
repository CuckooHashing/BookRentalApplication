from Repository.Depository import *
from domain.Book import *
from domain.Client import *
from Repository.RentalRepo import *
from Controller.undoController import *
class Controller:
    
    def __init__(self, book_repo, client_repo, undoController):
        self._book_repo = book_repo
        self._client_repo = client_repo
        self._undoController = undoController
          
    @staticmethod
    def parse_search_word(search):
        '''
        if search is string it turns all its characters into lowercase
        '''
        if type(search) == str:
            return search.lower()
        else:
            return search
    
    def search_book(self, search_word):
        '''
        searches and prints all books that partially match the search word
        '''
        word = Controller.parse_search_word(search_word)
        match = self._book_repo.search(word)
        for i in match:
            print(i)
    
    def search_client(self, search_word):
        '''
        searches and prints all clients that partially match the search word
        '''
        word = Controller.parse_search_word(search_word)
        match = self._client_repo.search(word)
        for i in match:
            print(i)
        
    def list_book(self):
        '''
        prints all books
        '''
        list_books = BookRepository.getAll(self._book_repo)
        
        for i in range(0, len(list_books)):
            print(list_books[i])
    
    def list_client(self):
        '''
        prints all clients
        '''
        list_clients = ClientRepository.getAll(self._client_repo)
        
        for i in range(0, len(list_clients)):
            print(list_clients[i])
            
    def add_book(self, book, rents):
        '''
        adds a book to the repository
        '''
        try:
            BookRepository.add(self._book_repo, book)
        except ValueError:
            raise ValueError
        redo = FunctionCall(self.add_book, book, rents)
        undo = FunctionCall(self.remove_book, book, rents)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(co)
        
        
    def add_client(self, client, rents):
        '''
        adds a client to the repository
        '''
        try:
            ClientRepository.add(self._client_repo, client)
        except ValueError:
            raise ValueError
        redo = FunctionCall(self.add_client, client, rents)
        undo = FunctionCall(self.remove_client, client, rents)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(co)
        
    def remove_book(self, book, rents):
        '''
        removes a book from the repository and all its rentals from the rental repo
        '''
        try:
            self._book_repo.remove(book)
        except IndexError:
            raise IndexError("No such book...:(")
        undo = FunctionCall(self.add_book, book, rents)
        redo = FunctionCall(self.remove_book, book, rents)
        
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        
        for r in rents.getAll():
            if r.get_bookID() == book.get_id():
                a = r
                rents.delete(r)
                redo = FunctionCall(rents.delete, a)
                undo = FunctionCall(rents.rent_book, self._client_repo.find_by_id(a.get_clientID()), book, a.get_rented_date())
                oper = Operation(undo, redo)
                co.add(oper)
        self._undoController.add_operation(co)
        
    def remove_client(self, client, rents):
        '''
        removes a client from the repository and all its rentals from the rental repo
        '''
        try:
            self._client_repo.remove(client)
        except IndexError:
            raise IndexError("No such client...:(")
        undo = FunctionCall(self.add_client, client, rents)
        redo = FunctionCall(self.remove_client, client, rents)
        
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        
        for r in rents.getAll():
            if r.get_clientID() == client.get_id():
                a = r
                rents.delete(r)
                redo = FunctionCall(rents.delete, a)
                undo = FunctionCall(rents.rent_book, client, self._book_repo.find_by_id(a.get_bookID()), a.get_rented_date())
                oper = Operation(undo, redo)
                co.add(oper)
        self._undoController.add_operation(co)
        
    def update_book(self, book):
        '''
        updates the info of a book
        '''
        try:
            old_book = self._book_repo.find_by_id(book.get_id())
            BookRepository.update(self._book_repo, book)
        except IndexError:
            raise IndexError
        redo = FunctionCall(self.update_book, book)
        undo = FunctionCall(self.update_book, old_book)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(co)
    
    def update_client(self, client):
        '''
        updates the info of a client
        '''
        try:
            old_client = self._client_repo.find_by_id(client.get_id())
            ClientRepository.update(self._client_repo, client)
        except IndexError:
            raise IndexError
        redo = FunctionCall(self.update_client, client)
        undo = FunctionCall(self.update_book, old_client)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(co)
        