# Implements the Prority Queue ADT using a list.

# Defines a private storage class for creating PQEntry.
class PriorityQEntry(object):
    def __init__(self,item,priority):
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

class PriorityQueue :
    # Constructs an empty queue.
    def __init__( self ):
        self._queue = list() # use ._queue is a list for collect the PriorityQEntry

    # Return True if the queue is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0
    
    # Returns the number of items in the queue.
    def __len__( self ):    
        return len(self._queue)

    # Removes and return the first item from the queue
    def dequeue(self):
        assert not self.isEmpty(),"Queue is empty"
        item = self._queue.pop(0)
        return item

    # add a new item onto the last of the queue.
    def enqueue( self, item , priority ):
        newEntry = PriorityQEntry(item,priority )
        self._queue.append(newEntry)
        #sort priority here
        self.prioritySort()


    def prioritySort( self ):
        n = len( self._queue ) - 1
        # Perform n-1 bubble operations on the sequence
        for i in range( n , 0 , -1 ) :
        # Bubble the largest item to the end.
            for j in range(i) :
                if self._queue[j]._priority > self._queue[j + 1]._priority : # swap the j and j+1 items.
                    tmp = self._queue[j]
                    self._queue[j] = self._queue[j + 1]
                    self._queue[j + 1] = tmp        
        return self

    # Show the items in queues
    def __repr__(self):
        s = "-------------\n"
        for i in range(len(self)):
            s = s + str(self._queue[i]._priority) + "  "
            s = s + str(self._queue[i]._item) + "\n"
        s = s + "-------------"
        return s
    
    def __str__(self):
        s = "-------------\n"
        for i in range(len(self)):
            s = s + str(self._queue[i]._priority) + "  "
            s = s + str(self._queue[i]._item) + "\n"
        s = s + "-------------"
        return s

# Implement 
mytask = PriorityQueue()
mytask.enqueue("do GEN121 Final exam",3)
mytask.enqueue("do CPE111 Final exam",2)
mytask.enqueue("play COOKIE RUN",1)
mytask.enqueue("sleep all day",1)
mytask.enqueue("do something",4)
mytask.enqueue("read CHHD102",5)

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

