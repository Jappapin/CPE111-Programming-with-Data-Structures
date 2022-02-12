import random
import time
import matplotlib.pyplot as plt
def quick_sort(seq): 
    if len(seq) < 2 : return seq 
    mid = len(seq)//2 
    pi = seq[mid] 
    seq = seq[:mid] + seq[mid+1:] 
    lo = [x for x in seq if x <= pi] 
    hi = [x for x in seq if x > pi] 
    return quick_sort(lo) + [pi] + quick_sort(hi) 
num = [100, 200,400,500,600,700,800,900,1000,2000,4000,5000,6000,7000,8000,9000,10000]
Average = []
Best = []
Worst = []
for j in num :
    seq = [] 
    for i in range(0 , j ):
        seq.append(random.randint( 1, j ))
        
    start_A = time.time( )
    A = quick_sort(seq)
    end_A = time.time( )
    elapsed_A = end_A - start_A
    
    Average.append(elapsed_A)
    
    start_B = time.time( )
    B = quick_sort(A)
    end_B = time.time( )
    elapsed_B = end_B - start_B
    
    Best.append(elapsed_B)

    B_reversed = reversed(B)
    start_W = time.time( )
    W = quick_sort(list(B_reversed))
    end_W = time.time( )
    elapsed_W = end_W - start_W
    
    Worst.append(elapsed_W)
    

plt.plot(Average, label = 'Average')
plt.plot(Worst, label = 'Worst')
plt.plot(Best, label = 'Best')
plt.title('Quick Sort', fontsize = 25)
plt.xlabel("number of sequence")
plt.ylabel("Time")
plt.plot(num, Average,'g',num, Best,'b',num, Worst,'r')
plt.legend()
plt.show()




