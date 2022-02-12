from collections.abc import MutableMapping
from random import randrange
class Map(MutableMapping):
    """ Our own abstract base class that includes a nonpublic_Item class"""
    #-------- nested _Item class -------------
    class _Item:
        """ Lightweight composite to store key-value pairs as map items"""
        __slots__ = '_key','_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __eq__(self,other):
            return self._key == other._key # compare items based on their keys

        def __ne__(self,other):
            return not (self == other) # opposite of __eq__

        def __lt__(self,other):
            return self._key < other._key # compare items based on their keys

class TableMap(Map):
    """Map implementation using an unordered list"""
    def __init__(self):
        """Create an empty map"""
        self._table = []

    def __getitem__(self,k):
        """Return value associated with key (raise Key Error if not found)"""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: '+repr(k))

    def __setitem__(self,k,v):
        """ Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if k == item._key:  #Found a match:
                item._value = v #reassign value
                return          # and quit
        # did not find match for key
        self._table.append(self._Item(k,v))

    def __delitem__(self,k):
        """ Remove item associated with key k (raise KeyError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' +repr(k))

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys"""
        for item in self._table:
            yield item._key
class ChainHashMap(Map):
    """Abstract base class for map using hash-table with MAD compression"""
    def __init__(self, cap = 11, p = 109345121):
        """Create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0 # number of entries in the map
        self._prime = p # prime for MAD compression
        self._scale = 1 + randrange(p-1) # scale for 1 to p-1 for MAD
        self._shift = randrange(p)  # shift from 0 to p-1 for MAD
    def _hash_function(self,k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)

    def __setitem__(self,k,v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v) # subroutime maintains self._n
        if self._n > len(self._table) // 2: # keep load factor <= 0.5
            self._resize(2 * len(self._table) -1)   # number 2^x -1 is often prime

    def __delitem__(self,k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n -= 1

    def _resize(self,c): # resize bucket array to capacity c
        old = list(self.items()) # use iteration to record existing items
        self._table = c * [None] # 
        self._n = 0
        for (k,v) in old:
            self[k] = v

    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+ repr(k)) # no match found
        return bucket[k]

    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = TableMap() # sent New table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # key was new to the table
               self._n += 1 # increase overall map size
    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+repr(k))
        del bucket[k]
    
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

import csv
STD = TableMap()
with open('student.csv','r',encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    studentlist = list(reader) #change to list
    
    for i in range(len(studentlist)):
        STD[studentlist[i][0]] = studentlist[i][1]
        
    STDChain = ChainHashMap()
    for j in range(len(studentlist)):
         STDChain[studentlist[j][0]] = studentlist[j][1]

STD["62070505235"]
STDChain["62070505209"]





