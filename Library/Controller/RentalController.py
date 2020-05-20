from domain.Rental import Rental
from domain.Book import Book
from domain.Client import Client
from Repository.RentalRepo import *
from datetime import *
from Controller.undoController import *
from Repository.Iterable import *

class RentalService:
    def __init__(self, book_repo, client_repo, rent_repo, undoController):
        self._book_repo = book_repo
        self._client_repo = client_repo
        self._rent_repo = rent_repo
        self._undoController = undoController
        
        
    def list_rents(self):
        for i in self._rent_repo.getAll():
            print(i)
    
    def rent(self, book, client, date):
        '''
        rents a book
        '''
        try:
            if self.available_book(book, date, date + timedelta(days = 14)):
                RentalRepository.rent_book(self._rent_repo, client, book, date)
            else:
                raise Exception("Book not available at selected time...:(")
        except Exception as error:
            raise Exception(error)
        
        undo = FunctionCall(self._rent_repo.delete, RentalRepository.rent_book(self._rent_repo, client, book, date))
        redo = FunctionCall(self._rent_repo.rent_book, book, client, date)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(oper)
        
        
    def delete_by_id(self, id, which):
        '''
        removes all rentals that either have a give book/client id
        '''
        for i in self._rent_repo.getAll():
            if which == 1:
                if id == i.get_bookID():
                    self._rent_repo.delete(i)
                    
            else:
                if id == i.get_clientID():
                    self._rent_repo.delete(i)
                    
        
    def available_book(self, book, start, end):
        '''
        checks if a selected book is available. It is if it's not already in rent_repo 
        '''
        for i in self._rent_repo.getAll():
            if book.get_id() == i.get_bookID():
                if start < i.get_due_date() or end > i.get_rented_date():
                    return False
                elif i.get_return_date() != None:
                    if start < i.get_return_date():
                        return False
        return True
    
    def return_book(self, book, client, date):
        '''
        returns a book
        '''
        try:
            RentalRepository.return_book(self._rent_repo, client, book, date)
        except Exception:
            raise Exception
        
        undo = FunctionCall(self._rent_repo.return_book, book, client, None)
        redo = FunctionCall(self._rent_repo.return_book, book, client, date)
        oper = Operation(undo, redo)
        co = CascadedOperation()
        co.add(oper)
        self._undoController.add_operation(co)
        
            
    def most_rented_books(self):
        '''
        returns a list of books in descending order of the number of times they were rented
        '''
        mostRented = {}
        
        for i in self._rent_repo.getAll():
            if i.get_bookID() not in mostRented.keys():
                mostRented[i.get_bookID()] = 1
            else:
                mostRented[i.get_bookID()] += 1
        
        for book in self._book_repo.getAll():
            if book.get_id() not in mostRented.keys():
                mostRented[book.get_id()] = 0
        
        result = Iterator()
        #result = []
        for i in mostRented:
            b = self._book_repo.find_by_id(i)
            result.addaos(BookRentalCount(b, mostRented[i]))
            #result.append(BookRentalCount(b, mostRented[i]))
        result.pancake_sort(reverse=True)
        return result
    
    
    def most_active_clients(self):
        '''
        returns a list of clients sorted in descending order of the number of book rental days they have
        '''
        mostActive = {}
        for i in self._rent_repo:
            if i.get_clientID() not in mostActive.keys():
                if i.get_return_date() is not None:
                    mostActive[i.get_clientID()] = (i.get_return_date() - i.get_rented_date()).days
            else:
                if i.get_return_date() is not None:
                    mostActive[i.get_clientID()] += (i.get_return_date() - i.get_rented_date()).days
        
        for client in self._client_repo.getAll():
            if client.get_id() not in mostActive.keys():
                mostActive[client.get_id()] = 0
        
        result = []
        for i in mostActive:
            c = self._client_repo.find_by_id(i)
            result.append(ClientRentalCount(c, mostActive[i]))
        result.sort(reverse=True)
        return result
    
    def most_rented_author(self):
        '''
        returns list of book authored, sorted in descending order of the total number of rentals their books have.
        '''
        authors = {}
        for i in self._rent_repo:
            book = self._book_repo.find_by_id(i.get_bookID())
            if book is not None:
                if book.get_author() not in authors.keys():
                    authors[book.get_author()] = 1
                else:
                    authors[book.get_author()] += 1
        sorted(authors.values(), reverse=True)
        author = list(authors.keys())[0]
        most = {}
        for i in self._rent_repo.getAll():
            book = self._book_repo.find_by_id(i.get_bookID())
            if book.get_author() == author:
                if book.get_id() not in most.keys():
                    most[book.get_id()] = 1
                else:
                    most[book.get_id()] += 1
        result = []
        for i in most:
            b = self._book_repo.find_by_id(i)
            result.append(BookRentalCount(b, most[i]))
        result.sort(reverse=True)
        return result
        
    @staticmethod
    def late(i):
        if ((datetime.now() - i.get_due_date()).days) > 14:
            return True
        else:
            return False
            
    def late_rentals(self):
        '''
       books that are currently rented, for which the due date for return has passed, 
       sorted in descending order
        '''
        lister = self._rent_repo.filther(RentalService.late)
        lateRented = {}
        
        for i in lister:
            if i.get_due_date() < datetime.now():
                if i.get_bookID() not in lateRented.keys():
                    lateRented[i.get_bookID()] = (datetime.now() - i.get_due_date()).days
                else:
                    lateRented[i.get_bookID()] += (datetime.now() - i.get_due_date()).days

        result = []
        for i in lateRented:
            b = self._book_repo.find_by_id(i)
            result.append(BookRentalCount(b, lateRented[i]))
        result.sort(reverse=True)
        '''
        someother = Iterator(result)
        someother.pancake_sort(reverse=True)
        '''
        return result       
    
class BookRentalCount(Iterator):
    '''
    data transfer object for books
    '''
    def __init__(self, book, count):
        self._book = book
        self._count = count
        Iterator.__init__(self)
        
    def __str__(self):
        return str(self._count) + " for book Id: " + str(self._book.get_id()) + ", title: " + str(self._book.get_title()) + ", author: " + str(self._book.get_author()) +", described as: " + str(self._book.get_desc())
    
    def __lt__(self, obj):
        return self._count < obj._count 

class ClientRentalCount:
    '''
    data transfer object for clients
    '''
    def __init__(self, client, count):
        self._client = client
        self._count = count

    def __str__(self):
        return str(self._count) + " for client Id: " + str(self._client.get_id()) + ", whose name is: " + str(self._client.get_name())
    
    def __lt__(self, obj):
        return self._count < obj._count 

     