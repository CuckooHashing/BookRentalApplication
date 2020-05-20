
class Iterator:
    def __init__(self):
        self._start = 0
        self._all = []
        
    def __iter__(self):
        return self
    
    def addaos(self, obj):
        self._all.append(obj)
    
    def __next__(self):
        if self._start >= len(self._all):
            raise StopIteration
        else:
            self._start += 1
            return self._all[self._start - 1]
        
    def __getitem__(self, index):
        return self._all[index]
    
    def __delitem__(self, index):
        del self._all[index]
    
    def __setitem__(self, obj, index):
        self._all[index] = obj
        
    def __str__(self):
        stringy = ""
        for i in self._all:
            stringy += str(i)
        return stringy
    
    @staticmethod
    def par(x):
        if x%2 == 1:
            return True
        else:
            return False 
            
    def filther(self, fct):
        '''
        filthers a list
        '''
        some = []
        for i in self._all:
            if fct(i):
                some.append(i)
        return some
         
    def maximum(self, n, reverse):
        '''
        returns the index of the maximum value in the array between 0 and n-1
        '''
        Max = 0
        for i in range (0, n):
            if reverse == False:
                if self._all[i] > self._all[Max]:
                    Max = i
            else:
                if self._all[i] < self._all[Max]:
                    Max = i
        return Max
    
    def flip_pancakes(self, index):
        '''
        reverses an array from a given index
        '''
        i = 0
        while i < index:
            aux = self._all[i]
            self._all[i] = self._all[index]
            self._all[index] = aux
            i += 1
            index -= 1
            
    def pancake_sort(self, reverse = False):
        '''
        stating from the complete array reduce the size by finding the max of a subarray and moving
        it to end
        '''
        dim = len(self._all)
        while dim > 1:
            Max = self.maximum(dim, reverse)
            if Max != dim - 1:
                self.flip_pancakes(Max)
                self.flip_pancakes(dim - 1)
            dim -= 1 
                
           

        