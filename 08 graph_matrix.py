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
        assert row >= 0 and row < self.numRows()             and col >= 0 and col < self.numCols(),                 "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]
    # Sets the contents of the element at position [i,j] to value.
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows()             and col >= 0 and col < self.numCols(),                 "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

    
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

class Graph:
    def __init__(self,directed=False):
        self._Vertices = list()
        self._MATRIX = Array2D(17,17)
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
        
#-----------------------------------------------------------
    def is_directed(self):
        return self._directed

    def findindex(self,v):
        if v in self._Vertices:
            return self._Vertices.index(v)
#-------------------------------------------------------------------------        
    def vertex_count(self):
        return len(self._Vertices)
    
    def vertices(self):
        return self._Vertices
    
    def edge_count(self):
        total = 0
        for row in range(self.vertex_count()):
            for col in range(self.vertex_count()):
                if self._MATRIX[row,col] != None:
                    total += 1
        return total if self.is_directed() else total // 2

    def edges(self):
        edges_list = list()
        for row in range(self.vertex_count()):
            for col in range(self.vertex_count()):
                if (self._MATRIX[row,col] not in edges_list) and (self._MATRIX[row,col] is not None):
                    edges_list.append(self._MATRIX[row,col])
        return edges_list
    
    def get_edge(self, u, v):
        return self._MATRIX[self.findindex(u),self.findindex(v)]
    
    def degree(self, v, outgoing=True):
        total = 0
        if outgoing:
            for col in range(self.vertex_count()):
                if self._MATRIX[self.findindex(v),col] != None:
                    total += 1
        #incoming
        else:
            for row in range(self.vertex_count()):
                if self._MATRIX[row,self.findindex(v)] != None:
                    total += 1
                    
        return total

    def incident_edges(self, v, outgoing=True):
        adj = list()
        if outgoing:
            for col in range(self.vertex_count()):
                if self._MATRIX[self.findindex(v),col] != None:
                    adj.append(self._MATRIX[self.findindex(v),col])
        #incoming
        else:
            for row in range(self.vertex_count()):
                if self._MATRIX[row,self.findindex(v)] != None:
                    adj.append(self._MATRIX[row,self.findindex(v)])
        return adj
    def insert_vertex(self, x):
        v = self.Vertex(x)
        self._Vertices.append(v)
        return v

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
        A = self.findindex(v)
        C = self.vertex_count()
        while A <= C :
            for B in range(C) :
                self._MATRIX[self.findindex(v),A] = self._MATRIX[self.findindex(v)+1,A]
                self._MATRIX[A,self.findindex(v)] = self._MATRIX[A,self.findindex(v)+1]
            A += 1
        self._Vertices.remove(v)
        
    def remove_edge(self,e):
        self._MATRIX[self.findindex(e.endpoints()[0]),self.findindex(e.endpoints()[1])] = None
    
def DFS(g,u,discovered={}):
    discovered[u] = None
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            print("add "+str(v)+" to discovered")
            discovered[v] = e
            DFS(g,v,discovered)
    return discovered.keys()

def BFS(g,s,discovered={}):
    level = [s]
    discovered[s] = None
    while len(level)>0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    print("add "+str(v)+" to discovered")
                    discovered[v] = e
                    next_level.append(v)
            level = next_level
    return discovered.keys()
#--------------- test graph --------------
g = Graph()
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
K = g.insert_vertex('K')
L = g.insert_vertex('L')
M = g.insert_vertex('M')
N = g.insert_vertex('N')
O = g.insert_vertex('O')
P = g.insert_vertex('P')

ab = g.insert_edge(A,B,1)
af = g.insert_edge(A,F,1)
ae = g.insert_edge(A,E,1)
bc = g.insert_edge(B,C,1)
bf = g.insert_edge(B,F,1)
cd = g.insert_edge(C,D,1)
cg = g.insert_edge(C,G,1)
dg = g.insert_edge(D,G,1)
dh = g.insert_edge(D,H,1)
fe = g.insert_edge(F,E,1)
fi = g.insert_edge(F,I,1)
ei = g.insert_edge(E,I,1)
gj = g.insert_edge(G,J,1)
gk = g.insert_edge(G,K,1)
gl = g.insert_edge(G,L,1)
hl = g.insert_edge(H,L,1)
ij = g.insert_edge(I,J,1)
im = g.insert_edge(I,M,1)
iin = g.insert_edge(I,N,1)
jk = g.insert_edge(J,K,1)
kn = g.insert_edge(K,N,1)
ko = g.insert_edge(K,O,1)
lp = g.insert_edge(L,P,1)
mn = g.insert_edge(M,N,1)

g.vertices()
#g.remove_vertex(I)
DFS(g,A)
#g.vertex_count()

#g.remove_edge(fe)
BFS(g,A)





