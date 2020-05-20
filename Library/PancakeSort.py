def maximum(x, n):
    '''
    returns the index of the maximum value in the array between 0 and n-1
    '''
    Max = 0
    for i in range (0, n):
        if x[i] > x[Max]:
            Max = i
    return Max

def findMax(arr, n): 
    mi = 0
    for i in range(0,n): 
        if arr[i] > arr[mi]: 
            mi = i 
    return mi 

l = [8, 9, 7, 6, 5, 4, 2, 3, 5]

def flip_pancakes(x, index):
    '''
    reverses an array from a given index
    '''
    i = 0
    while i < index:
        aux = x[i]
        x[i] = x[index]
        x[index] = aux
        i += 1
        index -= 1
        
def flip(arr, i): 
    start = 0
    while start < i: 
        temp = arr[start] 
        arr[start] = arr[i] 
        arr[i] = temp 
        start += 1
        i -= 1

def flippy(x, index):
    i = 0
    while i < index:
        aux = x[i]
        x[i] = x[index]
        x[index] = aux
        i += 1
        index -= 1

def pancake_sort(x):
    '''
    stating from the complete array reduce the size by finding the max of a subarray and moving
    it to end
    '''
    dim = len(x)
    while dim > 1:
        Max = maximum(x, dim)
        if Max != dim - 1:
            flip_pancakes(x, Max)
            flip_pancakes(x, dim-1)
        dim -= 1


 

def pancakeSort(arr, n): 

    curr_size = n 
    while curr_size > 1: 
        mi = findMax(arr, curr_size) 
        if mi != curr_size-1: 
            flippy(arr, mi) 
            flippy(arr, curr_size-1) 
        curr_size -= 1
   
l = [8, 9, 7, 6, 5, 4, 2, 3, 5]     
pancake_sort(l)
print(l)