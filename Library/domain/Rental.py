from datetime import *
class Rental:

    
    def __init__(self, clientID, bookID, rentalID, rented_date, due_date, return_date):
        '''
        init a rental set of data
        '''
        self._clientID = clientID
        self._bookID = bookID
        self._rentalID = rentalID
        self._rented_date = rented_date
        self._due_date = due_date
        self._return_date = return_date
    
    def __str__(self):
        return "Client id: " + str(self._clientID) + ", Book id: " + str(self._bookID) + ", Rent date: " + str(self._rented_date) + ", Due date: " + str(self._due_date) + ", Return date: " + str(self._return_date)
    
    def get_clientID(self):
        return self._clientID
    def get_bookID(self):
        return self._bookID
    def get_rentalID(self):
        return self._rentalID
    def get_rented_date(self):
        return self._rented_date
    def get_due_date(self):
        return self._due_date
    def get_return_date(self):
        return self._return_date
    
    def set_clientID(self, idiu):
        self._clientID = idiu
    def set_bookID(self, idiu):
        self.bookID = idiu
    def set_rentalID(self, idiu):
        self._rentalID = idiu
    def set_rented_date(self, idiu):
        self._rented_date = idiu
    def set_due_date(self, idiu):
        self._due_date = idiu
    def set_return_date(self, idiu):
        self._return_date = idiu
