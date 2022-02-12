# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ):
    n = len( theSeq ) - 1
    # Perform n-1 bubble operations on the sequence
    for i in range( n , 0 , -1 ) :
        # Bubble the largest item to the end.
        for j in range(i) :
            if theSeq[j] > theSeq[j + 1] : # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq
