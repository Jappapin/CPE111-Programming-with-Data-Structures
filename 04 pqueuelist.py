# Implements the Prority Queue ADT using a list.

# Defines a private storage class for creating PQEntry.
class PriorityQEntry(object):
    def __init__(self,item,priority):
        self._item = item
        self._priority = priority
        
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
        # Enter code here
        #...
        #...
        #...

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


        
# Test Code start here
mytask = PriorityQueue()
mytask.enqueue("do homeworks",5)
mytask.enqueue("call my girlfriend",2)
mytask.enqueue("call my mom",3)
mytask.enqueue("play RoV",1)
mytask.enqueue("do Aj K's assignment",1)

