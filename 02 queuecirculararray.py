import ctypes
class Array :
# Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear( None )
    # Returns the size of the array.
    def __len__( self ):
        return self._size
    # Gets the contents of the index element.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]
    # Puts the value in the array element at index position.
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value
    def __add__(self,rhsArray):
        assert self._size == rhsArray._size, "Array can't be added"
        newArray = Array(self._size)
        for i in range(self._size):
            newArray[i] = self[i] + rhsArray[i]
        return newArray
    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value
    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )
    # Returns the string reputation of an object
    def __repr__(self):
        s = '[ '
        for x in self._elements:
            s = s + str(x) + ' ,'
        s = s[:-2] + ' ]'
        return s    
            

# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__( self ):
        return self
    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
                
class Queue :
    # Creates an empty queue.
    def __init__( self, maxSize ) :
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array( maxSize )
        self.maxSize = maxSize

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return self._count == 0

    # Returns True if the queue is full.
    def isFull( self ) :
        return self._count == self.maxSize

    # Returns the number of items in the queue.
    def __len__( self ) :
        return self._count

    # Adds the given item to the queue.
    def enqueue( self, item ):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        self.maxSize = len(self._qArray)
        self._back = (self._back + 1) % self.maxSize
        self._qArray[self._back] = item
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[ self._front ]
        self.maxSize = len(self._qArray)
        self._front = (self._front + 1) % self.maxSize
        self._count -= 1
        return item
