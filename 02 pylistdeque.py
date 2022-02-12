
class Deque :
    def __init__(self):
        self._dlist = list()
    def isEmpty( self ):
        return len( self._dlist ) == 0
    def __len__( self ):
        return len( self._dList )
    def DeleteRear( self ):
        assert not self.isEmpty(), "Cannot delete from an empty deque"
        return self._dlist.pop()
    def DeleteFirst( self ):
        assert not self.isEmpty(), "Cannot delete from an empty deque"
        return self._dlist.pop(0)
    def AddFirst( self, item ):
        self._dlist.insert(0 , item)
    def AddRear( self, item ):
        self._dlist.append(item)
    def First( self):
        return self._dlist[0]
    def Rear( self):
        return self._dlist[-1]
    def __repr__(self):
        s = '[ '
        for x in self._dlist:
            s = s + str(x) + ' ,'
        s = s[:-2] + ' ]'
        return s





