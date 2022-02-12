#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random
import time
import matplotlib.pyplot as plt
def merge(left, right, seq): 
        i = j = 0 
        while i + j < len(seq): 
            if j == len(right) or (i < len(left) and left[i] < right[j]): 
                seq[i+j] = left[i] # copy ith element of left as next item of seq 
                i += 1 
            else: 
                seq[i+j] = right[j] # copy jth element of right as next item of seq 
                j += 1  
        return seq 
                
def merge_sort(seq): 
    n = len(seq) 
    if n < 2: 
        return # list is already sorted 
    # divide 
    mid = n // 2 
    left = seq[0:mid] # copy of first half 
    right = seq[mid:n] # copy of second half 
    # conquer (with recursion) 
    merge_sort(left) # sort copy of first half 
    merge_sort(right) # sort copy of second half 
    # merge results 
    seq = merge(left, right, seq) 
    return seq 

num = [100, 200,400,500,600,700,800,900,1000,2000,4000,5000,6000,7000,8000,9000,10000]
Average = []
Best = []
Worst = []
for j in num :
    seq = [] 
    for i in range(0 , j ):
        seq.append(random.randint( 1, j ))
        
    start_A = time.time( )
    A = merge_sort(seq)
    end_A = time.time( )
    elapsed_A = end_A - start_A
    
    Average.append(elapsed_A)
    
    start_B = time.time( )
    B = merge_sort(A)
    end_B = time.time( )
    elapsed_B = end_B - start_B
    
    Best.append(elapsed_B)

    B_reversed = reversed(B)
    start_W = time.time( )
    W = merge_sort(list(B_reversed))
    end_W = time.time( )
    elapsed_W = end_W - start_W
    
    Worst.append(elapsed_W)
    
plt.plot(Average, label = 'Average')
plt.plot(Worst, label = 'Worst')
plt.plot(Best, label = 'Best')
plt.title('Merge Sort', fontsize = 25)
plt.xlabel("number of sequence")
plt.ylabel("Time")
plt.plot(num, Average,'g',num, Best,'b',num, Worst,'r')
plt.legend()
plt.show()


# In[ ]:




