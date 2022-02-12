# Sorts a sequence in ascending order using the selection sort algorithm.
def selectionSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ):
        smallNdx = i
        for j in range( i + 1, n ):
            if theSeq[j] < theSeq[smallNdx] :
                smallNdx = j
        if smallNdx != i :
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq

seq = [1,6,78,9,10]
