# Implements the Stack ADT using a singly linked list.

# Defines a private storage class for creating list nodes.
class ListNode( object ):
    def __init__( self, item ) :
        self._item = item
        self._next = None

class LStack :
    # Constructs an empty stack.
    def __init__( self ):
        self._head = None
        self._size = 0

    # Return True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0
    
    # Returns the number of items in the bag.
    def __len__( self ):
        return self._size

    # Return the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty(),"Cannot peek at an empty stack"
        return self._head._item

    # Removes and return the top (head of the linked list) item  on the stack
    def pop(self):
        assert not self.isEmpty(),"Cannot pop from an empty stack"
        item = self._head._item
        self._head = self._head._next
        self._size -= 1
        return item    

    # push a new item onto the top of the stack (head of the linked list).
    def push( self, item ):
        newNode = ListNode(item)
        newNode._next = self._head
        self._head = newNode
        self._size += 1
        return item

    # Traversing a linked list
    def __repr__(self):
        curNode = self._head
        s = "--\n"
        while curNode is not None:
            #print(curNode._item)
            s = s + str(curNode._item)+ "\n"
            curNode = curNode._next
        s = s + "--"
        return s
    
    def __str__(self):
        curNode = self._head
        s = "--\n"
        while curNode is not None:
            #print(curNode._item)
            s = s + str(curNode._item)+ "\n"
            curNode = curNode._next
        s = s + "--"
        return s
        
    # Determines if an item is contained in the stack.
    def isContain( self, target ):
        curNode = self._head
        while curNode is not None and curNode._item != target :
            curNode = curNode._next
        return curNode is not None

        
# Code start here
A = LStack()
A.push(4)
A.push(19)
A.push(23)
A.push(74)
A.push(12)
A.pop()
print(A)
