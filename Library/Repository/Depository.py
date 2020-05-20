from domain.Book import *
from domain.Client import *
#from builtins import ValueError
from Repository.Iterable import *

class BookRepository(Iterator):
    
    def __init__(self):
        self._repo = []
        Iterator.__init__(self)
        
        
    def add(self, book):
        '''
        adds new book to repository
        '''
        if self.find(book):
            raise ValueError("ID already exists...:(")
        else:
            self._repo.append(book)
            Iterator.addaos(self, book)
        
    def getAll(self):
        '''
        gets a list of books
        '''
        return self._repo
    
    def remove(self, book):
        '''
        removes a book
        '''
        try:
            for i in self._repo:
                if i.get_id() == book.get_id():
                    self._repo.remove(i)
                    Iterator.__delitem__(self, self._repo.index(i))
        except ValueError:
            raise ValueError("No such book... :(")
    
    def find(self, book):
        '''
        finds a book by all its data
        '''
        for i in self.getAll():
            if i.get_id() == book.get_id():
                return True
        return False 
    
    def find_by_id(self, id):
        '''
        finds a book by its id
        '''
        for i in self.getAll():
            if i.get_id() == id:
                return i
        return 
    '''
    def update(self, book):
        if self.find(book) == False:
            raise IndexError("No such book...:(")
        else:
            self._repo[self.find(book)] = book
    '''
    def update(self, book):
        '''
        updates the information of a book
        '''
        ok = False
        for i in self._repo:
            if i.get_id() == book.get_id():
                i.set_author(book.get_author()) 
                i.set_title(book.get_title()) 
                i.set_desc(book.get_desc()) 
                Iterator.__setitem__(self, book, self._repo.index(i))
                ok = True
        if ok == False:
            raise IndexError("No such book...:(") 
    
    def search(self, word):
        '''
        finds and returns all books that partially match any of their field with the parameter 'word'
         '''
        match = []
        for i in self._repo:
            if i.get_id() == word or word in i.get_author().lower() or word in i.get_desc().lower() or word in i.get_title().lower():
                match.append(i)
        if len(match) == 0:
            raise ValueError("No books found... :(")
        else:
            return match
    
def test_book_repo(): 
    book1 = Book(0, "Persona 3", "3rd entry in the series", "Shuji Sogabe")
    book2 = Book(1, "Persona 5", "5th entry in the series", "Atlus")
    
    repo = BookRepository()
    repo.add(book1)
    listBooks = repo.getAll()
    
    assert len(listBooks) == 1
    assert listBooks[0].get_title() == "Persona 3"
    assert listBooks[0].get_author() == "Shuji Sogabe"
    assert listBooks[0].get_desc() == "3rd entry in the series"
    assert listBooks[0].get_id() == 0
    repo.add(book2)
    
    repo.remove(book1)
    listBooks = repo.getAll()
    assert len(listBooks) == 1
    assert listBooks[0].get_title() == "Persona 5"
    assert listBooks[0].get_author() == "Atlus"
    assert listBooks[0].get_desc() == "5th entry in the series"
    assert listBooks[0].get_id() == 1
    try:
        repo.remove(Book(34, "til", "de", "dw"))
        assert True
    except IndexError:
        pass
    except ValueError:
        pass
    
    assert repo.find(book1) == False
    assert repo.find(book2) == True
    
    
    repo.update(Book(1, "P3", "third entry in the series, manga", "Shuji Sogabe"))
    listBooks = repo.getAll()
    
    assert listBooks[0].get_title() == "P3"
    assert listBooks[0].get_author() == "Shuji Sogabe"
    assert listBooks[0].get_desc() == "third entry in the series, manga"
    assert listBooks[0].get_id() == 1
    try:
        repo.update(book1)
        assert False
    except IndexError:
        pass
    
#test_book_repo()

class ClientRepository(Iterator):
    
    def __init__(self):
        self._repo = []
        Iterator.__init__(self)
        
    def add(self, client):
        '''
        adds new client to repository
        '''
        if self.find(client):
            raise ValueError
        else:
            self._repo.append(client)
            Iterator.addaos(self, client)
        
    def getAll(self):
        '''
        gets a list of clients
        '''
        return self._repo
    
    def remove(self, client):
        '''
        removes a client
        '''
        try:
            #self._repo.remove(client)
            for i in self._repo:
                if i.get_id() == client.get_id():
                    self._repo.remove(i)
                    Iterator.__delitem__(self, self._repo.index(i))
        except ValueError:
            raise ValueError("No such client...:(")
    
    def find(self, client):
        '''
        finds a client 
        '''
        for i in self.getAll():
            if i.get_id() == client.get_id():
                return True
        return False 
    
    def find_by_id(self, id):
        '''
        finds a client by its id
        '''
        for i in self.getAll():
            if i.get_id() == id:
                return i
        return 
    
    def update(self, client):
        '''
        updates the information of a client
        '''
        ok = False
        for i in self._repo:
            if i.get_id() == client.get_id():
                i.set_name(client.get_name())
                Iterator.__setitem__(self, client, self._repo.index(i))
                ok = True
        if ok == False:
            raise IndexError("No such client...:(") 
        
    def search(self, word):
        '''
        finds and returns all clients that partially match any of their field with the parameter 'word'
         '''
        match = []
        for i in self._repo:
            if i.get_id() == word or word in i.get_name().lower():
                match.append(i)
        if len(match) == 0:
            raise ValueError("No clients found... :(")
        else:
            return match
        
def test_client_repo(): 
    client1 = Client(1, "Scott Fitzgerald")
    client2 = Client(2, "Shuji Sogabe")
    
    repo = ClientRepository()
    repo.add(client1)
    listClients = repo.getAll()
    
    assert len(listClients) == 1
    assert listClients[0].get_name() == "Scott Fitzgerald"
    repo.add(client2)
    listClients = repo.getAll()
    assert len(listClients) == 2
    assert listClients[1].get_name() == "Shuji Sogabe"
    assert listClients[0].get_id() == 1
    assert listClients[1].get_id() == 2
    
    repo.remove(client1)
    listBooks = repo.getAll()
    assert len(listClients) == 1
    assert listBooks[0].get_name() == "Shuji Sogabe"
    assert listBooks[0].get_id() == 2
    try:
        repo.remove(Client(34, "til"))
        assert True
    except IndexError:
        pass
    except ValueError:
        pass
    
    assert repo.find(client1) == False
    assert repo.find(client2) == True
    assert repo.find(Client(1, "Shuji Sogabe")) == False
    
    repo.update(Client(2, "Atlus"))
    listClients = repo.getAll()
    
    assert listClients[0].get_name() == "Atlus"
    assert listClients[0].get_id() == 2
    try:
        repo.update(client1)
        assert False
    except IndexError:
        pass
    
#test_client_repo()