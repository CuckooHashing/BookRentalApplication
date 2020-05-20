#from test.test_aifc import AifcTest
class undoController:
    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False
        
    def add_operation(self, operation):
        if self._duringUndo == True:
            return
        self._index += 1
        self._operations = self._operations[:self._index]
        self._operations.append(operation)
        self._duringUndo = False
        
    
    def undo(self):
        if self._index == -1:
            raise Exception("No more undos!")
        
        self._duringUndo = True
        self._operations[self._index].undo()
        #self._duringUndo = False
        self._index -= 1
        
        return True
    
    def redo(self):
        self._index += 1
        if self._index >= len(self._operations) or self._index == -1:
            raise Exception("No more redos!")
        
        
        self._duringUndo = True
        self._operations[self._index].redo()
        self._duringUndo = False
        
        return True
        
class CascadedOperation:
    def __init__(self):
        self._operations = []
        
    def add(self, op):
        self._operations.append(op)
        
    def undo(self):
        for o in self._operations:
            o.undo()
            
    def redo(self):
        for o in self._operations:
            o.redo()
            
class Operation:
    def __init__(self, undo_function, redo_function):
        self._undo_function = undo_function
        self._redo_function = redo_function
        
    def undo(self):
        self._undo_function.call()
    
    def redo(self):
        self._redo_function.call()
    
class FunctionCall:
    def __init__(self, fct, *params):
        self._function = fct
        self._params = params
        
    def call(self):
        self._function(*self._params)
        
        