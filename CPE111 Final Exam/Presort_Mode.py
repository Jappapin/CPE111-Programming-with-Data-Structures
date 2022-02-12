# Choose quick sort for sorting part
def quick_sort(seq): 
    if len(seq) < 2 : return seq 
    mid = len(seq)//2 
    pi = seq[mid] 
    seq = seq[:mid] + seq[mid+1:] 
    lo = [x for x in seq if x <= pi] 
    hi = [x for x in seq if x > pi] 
    return quick_sort(lo) + [pi] + quick_sort(hi) 

# Finds and returns a mode in sequence of orderable elements
def PresortMode(List):
    # Sort the list
    sorted_List = quick_sort(List)
    Mode_Freq = 0
    for i in range(len(sorted_List)):
        runlength = 1
        runvalue = sorted_List[i]
        while i + runlength <= len(sorted_List) - 1 and sorted_List[i + runlength] == runvalue :
            runlength += 1
        if runlength > Mode_Freq :
            Mode_Freq = runlength
            modevalue = runvalue
            i += runlength
    return modevalue

# Test case

# Implement List A
A = [2,3,4,4,5,3,2,6,16,5,6,7,10,12,12,6,6,2,3,4]
# Finds the Mode of List A
print(PresortMode(A))