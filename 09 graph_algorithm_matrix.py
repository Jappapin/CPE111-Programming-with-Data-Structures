# Implements the Array ADT using array capabilities of the ctypes module.
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

# Implementation of the Array2D ADT using an array of arrays.
class Array2D :
    # Creates a 2-D array of size numRows x numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )
        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ) :
            self._theRows[i] = Array( numCols )
    # Returns the number of rows in the 2-D array.
    def numRows( self ):
        return len( self._theRows )
    # Returns the number of columns in the 2-D array.
    def numCols( self ):
        return len( self._theRows[0] )
    # Clears the array by setting every element to the given value.
    def clear( self, value ):
        for row in range( self.numRows() ):
            #row_.clear( value )
            self._theRows[row].clear(value)
    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]
    # Sets the contents of the element at position [i,j] to value.
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

class Graph:
    def __init__(self,size,directed=False):
        self._Vertices = [None]*size
        self._MATRIX = Array2D(size,size)
        self._MATRIX.clear(None)
        self._directed = directed
#------------------------- Vertex class -----------------------
    class Vertex:
        __slots__ = '_element'

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __repr__(self):
            return self._element

        def __str__(self):
            return str(self._element)

#------------------------- Edge class -------------------------
    class Edge:
        __slots__ = '_origin' , '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __repr__(self):
            return str(self._element)
#-----------------------------------------------------------
    def is_directed(self):
        return self._directed

    def findindex(self,v):
        if v in self._Vertices:
            return self._Vertices.index(v)
#-------------------------------------------------------------------------
    def vertex_count(self):
        return len(list(filter(None,self._Vertices)))

    def vertices(self):
        return list(filter(None,self._Vertices))

    def edge_count(self):
        total = 0
        for row in range(len(self._Vertices)):
            for col in range(len(self._Vertices)):
                if self._MATRIX[row,col] != None:
                    total += 1
        return total if self.is_directed() else total // 2

    def edges(self):
        edges_list = list()
        for row in range(len(self._Vertices)):
            for col in range(len(self._Vertices)):
                if (self._MATRIX[row,col] not in edges_list) and (self._MATRIX[row,col] is not None):
                    edges_list.append(self._MATRIX[row,col])
        return edges_list

    def get_edge(self, u, v):
        return self._MATRIX[self.findindex(u),self.findindex(v)]

    def degree(self, v, outgoing=True):
        total = 0
        if outgoing:
            for col in range(len(self._Vertices)):
                if self._MATRIX[self.findindex(v),col] != None:
                    total += 1
        #incoming
        else:
            for row in range(len(self._Vertices)):
                if self._MATRIX[row,self.findindex(v)] != None:
                    total += 1

        return total

    def incident_edges(self, v, outgoing=True):
        adj = list()
        if outgoing:
            for col in range(len(self._Vertices)):
                if self._MATRIX[self.findindex(v),col] != None:
                    adj.append(self._MATRIX[self.findindex(v),col])
        #incoming
        else:
            for row in range(len(self._Vertices)):
                if self._MATRIX[row,self.findindex(v)] != None:
                    adj.append(self._MATRIX[row,self.findindex(v)])
        return adj
    def insert_vertex(self, x):
        v = self.Vertex(x)
        if None in self._Vertices:
            self._Vertices[self._Vertices.index(None)] = v
            return v
        else:
            #self._Vertices.append(v)
            print("Vertices number was exceeded")


    def insert_edge(self, u, v, x):
        # u is origin
        # v is destination
        e = self.Edge(u, v, x)
        if self.is_directed():
            self._MATRIX[self.findindex(u),self.findindex(v)] = e
        else:
            self._MATRIX[self.findindex(u),self.findindex(v)] = e
            self._MATRIX[self.findindex(v),self.findindex(u)] = e
        return e

    def remove_vertex(self,v):
        # enter code here
        if v in self._Vertices:
            # Delete edge first
            for e in self.incident_edges(v):# Set all incident_edge to None
                self.remove_edge(e)
            # Then delete Vertex
            self._Vertices[self.findindex(v)] = None
            del(v)

    def remove_edge(self,e):
        # enter code here
        # find the connected u and v of e
        [u,v] = e.endpoints()
        if self.is_directed():
            self._MATRIX[self.findindex(u),self.findindex(v)] = None
        else:
            self._MATRIX[self.findindex(u),self.findindex(v)] = None
            self._MATRIX[self.findindex(v),self.findindex(u)] = None
        return e
#----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class PriorityQueueBase:
#Abstract base class for a priority queue.
    class Item:
        __slots__ = '_key' , '_value'

        def __init__ (self, k, v):
            self._key = k
            self._value = v

        def __lt__ (self, other):
            return self._key < other._key # compare items based on their keys

        def is_empty(self): # concrete method assuming abstract len
            return len(self) == 0
#-------------------------------------------
class HeapPriorityQueue(PriorityQueueBase): # base class defines Item
#Use Heap to implement PriorityQueue
    def _parent(self, j):
        return (j - 1) // 2
    def _left(self, j):
        return 2*j + 1
    def _right(self, j):
        return 2*j + 2
    def _has_left(self, j):
        return self._left(j) < len(self._data) # index beyond end of list?
    def _has_right(self, j):
        return self._right(j) < len(self._data) # index beyond end of list?
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    def _siftup(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._siftup(parent) # recur at position of parent
    def _siftdown(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._siftdown(small_child) # recur at position of small child
    def __init__ (self):
        self._data = [ ]
    def __len__ (self):
        return len(self._data)
    def is_empty(self): # concrete method assuming abstract len
        return len(self) == 0
    def add(self, key, value):
        self._data.append(self.Item(key, value))
        self._siftup(len(self._data) - 1)# upheap newly added position
    def min(self):
        if self.is_empty( ):
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        if self.is_empty( ):
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1) # put minimum item at the end
        item = self._data.pop( ) # and remove it from the list;
        self._siftdown(0) # then fix new root
        return (item._key, item._value)
#---------------------------------------------------------------------------------
class AdaptableHeapPriorityQueue(HeapPriorityQueue):
# A locator-based priority queue implemented with a binary heap.
    #------------------------------ nested Locator class --------------------------
    class Locator(HeapPriorityQueue.Item):
    # Token for locating an entry of the priority queue.
        __slots__ = '_index' # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j
#------------------------------ nonpublic behaviors ------------------------------
# override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i,j) # perform the swap
        self._data[i]._index = i # reset locator index (post-swap)
        self._data[j]._index = j # reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._siftup(j)
        else:
            self._siftdown(j)

    def add(self, key, value):
    #Add a key-value pair
        token = self.Locator(key, value, len(self._data)) # initiaize locator index
        self._data.append(token)
        self._siftup(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
    #Update the key and value for the entry identified by Locator loc
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
    #Remove and return the (k,v) pair identified by Locator loc.”””
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1: # item at last position
            self._data.pop( ) # just remove it
        else:
            self._swap(j, len(self)-1) # swap item to the last position
            self._data.pop( ) # remove it from the list
            self._bubble(j) # fix item displaced by the swap
        return (loc._key, loc._value)


def Dijkstra(g, src):
    d = { } # d[v] is upper bound from s to v
    cloud = { } # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue( ) # vertex v will have key d[v]
    pqlocator = { } # map from vertex to its pq locator
    output = list()

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices( ):
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf') # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v) # save locator for future updates

    while not pq.is_empty( ):
        key, u = pq.remove_min() # key is Priority(weight), u is vertex
        cloud[u] = key
        #cloud[u] = key # its correct d[u] value
        del pqlocator[u] # u is no longer in pq
        for e in g.incident_edges(u): # outgoing edges (u,v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element( )
                if d[u] + wgt < d[v]: # better path to v?
                    d[v] = d[u] + wgt # update the distance
                    pq.update(pqlocator[v], d[v], v) # update the pq entry
    return cloud # only includes reachable vertices

#--------------------------------------------------------------------------
def PrimJarnik(g):
#Compute a minimum spanning tree of weighted graph g.
#Return a list of edges that comprise the MST (in arbitrary order).
    d = { } # d[v] is bound on distance to tree
    tree = {  } # edges in spanning tree
    pq = AdaptableHeapPriorityQueue( ) # d[v] maps to value (v, e=(u,v))
    pqlocator = { } # map from vertex to its pq locator
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices( ):
        if len(d) == 0: # this is the first node
            d[v] = 0 # make it the root
        else:
            d[v] = float('inf') # positive infinity
        pqlocator[v] = pq.add(d[v], (v,None))
    while not pq.is_empty( ):
        key,value = pq.remove_min()
        u,edge = value # unpack tuple from pq
        tree[u] = edge
        del pqlocator[u] # u is no longer in pq
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator: # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element( )
                if wgt < d[v]: # better edge to v?
                    d[v] = wgt # update the distance
                    pq.update(pqlocator[v], d[v], (v, link)) # update the pq entry
    return tree

class UnionFind:
# Python Implementation of Union_find class using union-by-size and path compression
#------------------------- nested Position class -------------------------
    class Position:
        __slots__ = '_container' , '_element' , '_size' , '_parent'
        def __init__(self, container, e):
            self._container = container # reference to UnionFind instance
            self._element = e
            self._size = 1
            self._parent = self # convention for a group leader
        def element(self):
            return self._element
#------------------------- Union-find -------------------------
    def make_group(self, e):
        return self.Position(self, e)
    def find(self, p):
        if p._parent != p:
            p._parent = self.find(p._parent) # overwrite p. parent after recursion
        return p._parent
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b: # only merge if different groups
            if a._size >= b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
#-----------------------------------------------------------------------------
def Kruskal(g):
#Compute a minimum spanning tree of a graph using Kruskal s algorithm.
#Return a list of edges that comprise the MST.
#The elements of the graph s edges are assumed to be weights.
    tree = { } # Dictionary of edges in spanning tree
    pq = HeapPriorityQueue( ) # entries are edges in G, with weights as key
    forest = UnionFind( ) # keeps track of forest clusters
    position = { } # map each node to its Partition entry
    for v in g.vertices( ):
        position[v] = forest.make_group(v)
    for e in g.edges( ):
        pq.add(e.element( ), e) # edge’s element is assumed to be its weight
    size = g.vertex_count( )
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight,edge = pq.remove_min()
        u,v = edge.endpoints( )
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree[edge.endpoints()] = edge
            forest.union(a,b)
    return tree

g = Graph(10)
A = g.insert_vertex('A')
B = g.insert_vertex('B')
C = g.insert_vertex('C')
D = g.insert_vertex('D')
E = g.insert_vertex('E')
F = g.insert_vertex('F')
G = g.insert_vertex('G')
H = g.insert_vertex('H')
I = g.insert_vertex('I')
J = g.insert_vertex('J')

ab = g.insert_edge(A,B,2)
ae = g.insert_edge(A,E,1)
ag = g.insert_edge(A,G,5)
bc = g.insert_edge(B,C,2)
bj = g.insert_edge(B,J,5)
ce = g.insert_edge(C,E,1)
cf = g.insert_edge(C,F,6)
ci = g.insert_edge(C,I,5)
de = g.insert_edge(D,E,2)
dg = g.insert_edge(D,G,2)
df = g.insert_edge(D,F,3)
dh = g.insert_edge(D,H,7)
fg = g.insert_edge(F,G,3)
fi = g.insert_edge(F,I,4)
hi = g.insert_edge(H,I,1)
hj = g.insert_edge(H,J,2)
ij = g.insert_edge(I,J,3)

print('Kruskal test : ',Kruskal(g))
print('PrimJarnik test : ',PrimJarnik(g))
print('Dijkstra test : ',Dijkstra(g, A))