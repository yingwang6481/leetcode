import numpy as np
def quicksort(a,i,j):
    if i<j:
        p = partition(a,i,j)
        quicksort(a,i,p-1)
        quicksort(a,p+1,j)
    return a

def partition(a,i,j):
    key = a[i]
    low = i
    high = j
    while(low<high):
        while(a[high]>=key and high>low):
            high-=1
        a[low]=a[high]
        while(a[low]<=key and high>low):
            low+=1
        a[high]=a[low]
        a[low] = key
    return low
def bubblesort(a,i,j):
    for m in range(j-i):
        swap=False
        for n in range(i,j-m):
            if a[n]>a[n+1]:
                temp = a[n]
                a[n] = a[n+1]
                a[n+1] = temp
                swap = True
        if not swap:
            return a
def insertsort(a,i,j):
    count = j-i+1
    for m in range(i+1,j+1):
        temp = a[m]
        for n in range(m-1,i-1,-1):
            if a[n]>temp:
                a[n+1]=a[n]
                a[n] = temp
    return a
def shellsort(a):
    length = len(a)
    step = int(length/2)
    while(step>0):
        for i in range(step):
            j = i + step
            while(j<length):
                key = a[j]
                k = j-step
                while(k>=0):
                    if a[k]>key:
                        a[k+step] = a[k]
                        a[k] = key
                    else:
                        k -= step
                        break
                j += step
        step = int(step/2)
    return a
def mergesort(a,i,j):
    if j-i<=1:
        return a[i:j]
    mid = int((i+1+j)/2)
    left =mergesort(a,i,mid)
    right = mergesort(a,mid,j)
    return merge(left,right)
def merge(left,right):
    i,j,k=0,0,0
    ans = []
    while(i!=len(left) and j!=len(right)):
        if left[i]<right[j]:
            ans.append(left[i])
            i +=1
        else:
            ans.append(right[j])
            j +=1
    if i==len(left):
        for t in range(j,len(right)):
            ans.append(right[j])
    else:
        for t in range(i,len(left)):
            ans.append(left[i])
    return ans
def max_heap(heap,heapsize,root):
    left = root*2
    right = left +1
    smaller = root
    if left<=heapsize and heap[left]>heap[smaller]:
        smaller = left
    if right<=heapsize and heap[right]>heap[smaller]:
        smaller = right
    if smaller!=root:
        heap[smaller],heap[root]=heap[root],heap[smaller]
        max_heap(heap,heapsize,smaller)
        max_heap(heap, heapsize, root)
def buid_heap(heap):
    heapsize=len(heap)-1
    for i in range(heapsize//2,0,-1):
        max_heap(heap,heapsize,i)
def heap_sort(heap):
    heap = [0]+heap
    buid_heap(heap)
    for i in range(len(heap)-2):
        heap[1],heap[len(heap)-1-i]=heap[len(heap)-1-i],heap[1]
        max_heap(heap,len(heap)-i-2,1)
    return heap
a = np.random.randint(100,size=[10]).tolist()
print(a)
print(heap_sort(a)[1:])
print(quicksort(a,0,9))