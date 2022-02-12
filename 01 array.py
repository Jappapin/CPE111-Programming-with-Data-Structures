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
            s = s + str(x) + ' '
        s = s[:-1] + ' ]'
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
    # Returns the string reputation of an object
    def __repr__(self):
        
        # ...... Edit here ......
        s = '[ '


        for x in self._theRows:
            s = s + str(x) + '\n'            

        s = s[:-2] + ' ] ]'
    
        return s    


class Matrix(Array2D):
    # Scales the matrix by the given scalar.
    def __init__(self, numRows, numCols):
        super().__init__(numRows, numCols)
        
    def _scaleBy( self, scalar):
        for r in range(self.numRows()):
            for c in range( self.numCols()):
                self[ r, c ] *= scalar

    # Creates and returns a new matrix that is the transpose of this matrix.
    def _tranpose( self ):
        # ...... Edit here ......
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[c,r]
        
        return newMatrix
    
    # Creates and returns a new matrix that results from matrix addition.    
    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__( self, rhsMatrix ):
        # ...... Edit here ......
        
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatible for the sub operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]
        return newMatrix
    
    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__( self, rhsMatrix ):
        assert self.numCols() == rhsMatrix.numRows(), \
               "Matrix size not compatible for the multiple operation"
        newMatrix = Matrix( self.numRows(),rhsMatrix.numCols())
        for r in range(newMatrix.numRows()):
            for c in range(self.numCols()):
                for i in range(self.numCols()):
                    newMatrix[r,c] = (self[r,i] * rhsMatrix[i,c])
        return newMatrix

    # Find and returns the determinant of 2*2 or 3*3 matrix
    def det(self):
        # It is must be a square matrix
        assert self.numCols() == self.numRows(), \
                "It should be a square matrix."
        # Only 2*2 or 3*3 matrix can be found the determinant in this method
        assert self.numCols() < 4 and self.numRows() < 4 ,\
                "It can find only det of 2*2 or 3*3 matrix."
        # Formula for 2*2 matrix
        if self.numRows() == 2 :
            result = ( self[0,0]*self[1,1] ) - ( self[1,0]*self[0,1] )
        # Formula for 3*3 matrix
        elif self.numRows() == 3 :
            result = ( self[0,0]*self[1,1]*self[2,2] ) + (self[0,1]*self[1,2]*self[2,0]) + \
                ( self[0,2]*self[1,0]*self[2,1] ) - ( self[0,2]*self[1,1]*self[2,0] ) - \
                ( self[0,1]*self[1,0]*self[2,2] ) - ( self[0,0]*self[1,2]*self[2,1] )
        return result

    # Find and returns the inverse of 2*2 matrix
    def inverse(self):
        # It is must be a 2*2 matrix
        assert self.numCols() == self.numRows() == 2, \
                "It can find only inverse of 2*2 matrix."
        # The determinant must not be zero
        assert self.det() == 0,\
                "Determinant of this matrix is 0, so it has no inverse."
        # Implement a new matrix for the formula (to find the inverse)
        newMatrix = Matrix(2,2)
        newMatrix[0,0] = self[0,0]
        newMatrix[0,1] = -self[0,1]
        newMatrix[1,0] = -self[1,0]
        newMatrix[1,1] = self[1,1]
        # Formula
        result = (1/self.det())*newMatrix
        return result

A = Array(10)
print(A)
A_iter = iter(A)
print(next(A_iter))

