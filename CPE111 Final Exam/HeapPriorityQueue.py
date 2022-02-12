import ctypes
# Array class from week2 lab
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
    def __add__(self,rhsArray):
        assert self._size == rhsArray._size, "Array can't be added"
        newArray = Array(self._size)
        for i in range(self._size):
            newArray[i] = self[i] + rhsArray[i]
        return newArray
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

# Creates an Entry as a element in Queue
class Entry(object) :
    def __init__(self,item,priority) :
        self._item = item
        self._priority = priority

# Show the items in Entry
    def __repr__(self):
        s = str(self._priority) + "  "
        s = s + str(self._item)
        return s
    
    def __str__(self):
        s = str(self._priority) + "  "
        s = s + str(self._item)
        return s

# Queue that sort Entry by its prioity 
# 1 is the Highest prioiry
# 5 is the Lowest priority
class HeapPriorityQueue() :
    def __init__(self,size) :
        self._hpqarray = Array(size) # Creates an array to store the element(Entry)
        self._size = size # the maximum size of queue
        self._count = 0 # the number of element(Entry) in queue

# Returns TRUE if the queue has no element(Entry)
    def isEmpty(self) :
        return self._count == 0   

# Returns the number of element(Entry) in queue
    def __len__(self) :
        return self._count

# Sift the value at the ndx element up the queue ( make the root to be the highest priority )
    def _siftUp( self, ndx ):
        if ndx > 0 :
            parent = (ndx - 1) // 2
            if self._hpqarray[ndx]._priority < self._hpqarray[parent]._priority : # swap elements
                self._hpqarray[ndx], self._hpqarray[parent] = self._hpqarray[parent], self._hpqarray[ndx]
                self._siftUp( parent )

# Sift the value at the ndx element down the queue 
# (after removes old root. then,takes the last element in queue to be the root)
    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2

# Determine which node contains the lower value.
        lowest = ndx
        if left < self._count and self._hpqarray[left]._priority <= self._hpqarray[lowest]._priority :
            lowest = left
        elif right < self._count and self._hpqarray[right]._priority <= self._hpqarray[lowest]._priority:
            lowest = right

# If the lowest value is not in the current node (ndx), 
# swap it with the lowest value and repeat the process.
        if lowest != ndx :
# swap the position of element
            self._hpqarray[ndx], self._hpqarray[lowest] = self._hpqarray[lowest], self._hpqarray[ndx]
            self._siftDown( lowest ) 

# enqueue the new Entry to the queue
    def enqueue(self,item,priority):
        assert priority <= 5 and priority > 0 ,\
            "Priority must be in 1-5"
# Create a new Entry
        self._hpqarray[self._count] = Entry(item,priority)
# Plus the number for queue
        self._count += 1
# Sift up
        self._siftUp(self._count - 1)

# Removes the Root Entry
    def dequeue(self):
# The queue must not be empty
        assert self._count != 0,\
            "Can't dequeue from empty queue"
        L = list()
# Value of the highest priority
        value = self._hpqarray[0]._priority
        result = self._hpqarray[0]
        self._count -= 1
        self._hpqarray[0] = self._hpqarray[self._count ]
        self._siftDown(0)
        L.append(result)
# Finds more the same priority as the Root
        for i in range(self._count):
            while self._hpqarray[i]._priority == value :
                result = self._hpqarray[i]
                self._count -= 1
                self._hpqarray[i] = self._hpqarray[self._count]
                self._siftDown(0)
                L.append(result)
        self._siftDown(0)
        return L
            
# Show the items in queues
    def __repr__(self):
        s = "-------------\n"
        for i in range(len(self)):
            s = s + str(self._hpqarray[i]._priority) + "  "
            s = s + str(self._hpqarray[i]._item) + "\n"
        s = s + "-------------"
        return s
    
    def __str__(self):
        s = "-------------\n"
        for i in range(len(self)):
            s = s + str(self._hpqarray[i]._priority) + "  "
            s = s + str(self._hpqarray[i]._item) + "\n"
        s = s + "-------------"
        return s         

# Implement 
mytask = HeapPriorityQueue(7)
mytask.enqueue("do GEN121 Final exam",3)
mytask.enqueue("do CPE111 Final exam",2)
mytask.enqueue("play COOKIE RUN",1)
mytask.enqueue("sleep all day",1)
mytask.enqueue("do something",4)
mytask.enqueue("read CHHD102",5)
mytask.enqueue("listen to music",2)

print("My task is : \n",mytask)
print("Length of my task is : ",len(mytask))
print("Is my task empty? : ",mytask.isEmpty())
print("The dequeued task is : \n",mytask.dequeue())
print("Now, My task is : \n",mytask)
print("And now Length of my task is : ",len(mytask))
print("The dequeued task is : \n",mytask.dequeue())
print("The dequeued task is : \n",mytask.dequeue())
print("The dequeued task is : \n",mytask.dequeue())
print("The dequeued task is : \n",mytask.dequeue())
print("And now, Is my task empty? : ",mytask.isEmpty())


