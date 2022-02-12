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
    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value
    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )

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


# An array-based implementation of the max-heap.
class MaxHeap :
    # Create a max-heap with maximum capacity of maxSize.
    def __init__( self,maxSize):
        self._elements = Array( maxSize )
        self._count = 0

    # Return the number of items in the heap.
    def __len__( self ):
        return self._count

    # Return the maximum capacity of the heap.
    def capacity( self ):
        return len( self._elements )

    # Add a new value to the heap.
    def add( self, value ):
        #assert self._count < self.capacity(), "Cannot add to a full heap."
        # Add the new value to the end of the list.
        self._elements[ self._count ] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp( self._count - 1 )

    # Extract the maximum value from the heap.
    def extract( self ):
        assert self._count > 0, "Cannot extract from an empty heap."
        # Save the root value and copy the last heap value to the root.
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[ self._count ]
        # Sift the root value down the tree.
        self._siftDown( 0 )
        return value

    # Sift the value at the ndx element up the tree.
    def _siftUp( self, ndx ):
        if ndx > 0 :
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent] : # swap elements
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftUp( parent )

    # Sift the value at the ndx element down the tree.
    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the larger value.
        largest = ndx
        if left < self._count and self._elements[left] >= self._elements[largest] :
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        # If the largest value is not in the current node (ndx), swap it with
        # the largest value and repeat the process.
        if largest != ndx :
            #swap( self._elements[ndx], self._elements[largest] )
            tmp = self._elements[ndx]
            self._elements[ndx] = self._elements[largest]
            self._elements[largest] = tmp
            self._siftDown( largest )
    # Display the value in the heap
    def __str__(self):
        s = "-------------\n"
        for i in range(self._count):
            s = s + str(self._elements[i]) + " \n"
        s = s + "-------------"
        return s        

    def __repr__(self):
        s = "-------------\n"
        for i in range(self._count):
            s = s + str(self._elements[i]) + " \n"
        s = s + "-------------"
        return s
#------------------------------- MinHeap --------------------------
class MinHeap :
    def __init__( self,maxSize):
        self._elements = Array( maxSize )
        self._count = 0

    # Return the number of items in the heap.
    def __len__( self ):
        return self._count

    # Return the maximum capacity of the heap.
    def capacity( self ):
        return len( self._elements )

    # Add a new value to the heap.
    def add( self, value ):
        #assert self._count < self.capacity(), "Cannot add to a full heap."
        # Add the new value to the end of the list.
        self._elements[ self._count ] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp( self._count - 1 )

    # Extract the maximum value from the heap.
    def extract( self ):
        assert self._count > 0, "Cannot extract from an empty heap."
        # Save the root value and copy the last heap value to the root.
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[ self._count ]
        # Sift the root value down the tree.
        self._siftDown( 0 )
        return value

    # Sift the value at the ndx element up the tree.
    def _siftUp( self, ndx ):
        if ndx > 0 :
            parent = ndx // 2
            if self._elements[ndx] < self._elements[parent] : # swap elements
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftUp( parent )

    # Sift the value at the ndx element down the tree.
    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the lower value.
        lowest = ndx
        if left < self._count and self._elements[left] <= self._elements[lowest] :
            lowest = left
        elif right < self._count and self._elements[right] <= self._elements[lowest]:
            lowest = right
        # If the lowest value is not in the current node (ndx), swap it with
        # the lowest value and repeat the process.
        if lowest != ndx :
            #swap( self._elements[ndx], self._elements[lowest] )
            self._elements[ndx], self._elements[lowest] = self._elements[lowest], self._elements[ndx]
            self._siftDown( lowest )
    # Display the value in the heap
    def __str__(self):
        s = "-------------\n"
        for i in range(self._count):
            s = s + str(self._elements[i]) + " \n"
        s = s + "-------------"
        return s        


# test Max-Heap
H = MaxHeap(20)
H.add(100)
H.add(84)
H.add(71)
H.add(60)
H.add(23)
H.add(12)
H.add(29)
H.add(1)
H.add(37)
H.add(4)
print('MaxHeap is \n',H)
# test Min-Heap
#M = MinHeap(20)
M = MinHeap(20)
M.add(100)
M.add(84)
M.add(71)
M.add(60)
M.add(23)
M.add(12)
M.add(29)
M.add(1)
M.add(37)
M.add(4)
print('MinHeap is \n',M)

