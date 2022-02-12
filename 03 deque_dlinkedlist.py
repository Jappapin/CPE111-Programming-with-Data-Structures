# Implements the Deque ADT using a doubly linked list.

# Defines a Simple DlinkNode. 
class DlinkNode(object):
    def __init__(self,item,prev,next):
        self._item = item
        self._prev = prev
        self._next = next

class DDeque:
    # Construct an empty Deque.
    def __init__(self):
        self._header = DlinkNode(None,None,None)
        self._trailer = DlinkNode(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    # Return the number of items in the deque
    def __len__(self):
        return self._size

    # Return True if the Deque is empty or False otherwise
    def isEmpty(self):
        return self._size == 0

    # Insert node between predecessor and successor
    def insert_between(self,item,predecessor,successor):
        newNode = DlinkNode(item,predecessor,successor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1
        
    # Delete a node 
    def delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        item = node._item
        node._prev = node._next = node._item = None
        return item

    def __str__(self):
        curNode = self._header
        s = "["
        while curNode is not None:
            s = s + str(curNode._item)+ " "
            curNode = curNode._next
        s = s[:-1] + "]"
        return s

    def __repr__(self):
        curNode = self._header
        s = "["
        while curNode is not None:
            s = s + str(curNode._item)+ " "
            curNode = curNode._next
        s = s[:-1] + "]"
        return s
    
    def First(self):
        assert not self.isEmpty(), "Deque is empty"
        return self._header._next._item
        
    def Rear(self):
        assert not self.isEmpty(), "Deque is empty"
        return self._trailer._prev._item

    def AddFirst(self,item):
        self.insert_between(item, self._header , self._header._next )


    def AddRear(self,item):
        self.insert_between(item, self._trailer._prev , self._trailer )
        
    def DeleteFirst(self):
        assert not self.isEmpty(),"Deque is empty"
        self.delete_node( self._header._next )


    def DeleteRear(self):
        assert not self.isEmpty(),"Deque is empty"
        self.delete_node( self._trailer._prev )

# Code Start here
D = DDeque()
D.AddRear(5)
D.AddFirst(3)
D.AddRear(25)
D.AddRear(99)
D.AddFirst(12)
i = D.DeleteFirst()
print(D.First())
print(D)
