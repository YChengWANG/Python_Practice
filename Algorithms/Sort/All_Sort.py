from Cal_Time import execute_time

@execute_time
def bubble_sort(li):    # O(n^2)
    for i in range(len(li)-1):
        sign = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                sign = True
        if sign == False:
            return

@execute_time
def select_sort(li):   # O(n^2)
    for i in range(len(li)-1):
        tmp = i
        for j in range(i+1,len(li)):
            if li[j]<li[tmp]:
                tmp = j
        li[i],li[tmp] = li[tmp],li[i]

@execute_time
def insert_sort(li):    # O(n^2)
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j -= 1
        li[j+1] = tmp


def partition(li,left,right):
    tmp = li[left]
    while left<right:
        while left<right and li[right]>=tmp:
            right -= 1
        li[left] = li[right]
        while left<right and li[left]<=tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left
        
    
def _quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

@execute_time
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)        
    

def sift(li,low,high):
    i = low
    j = 2*i + 1
    tmp = li[low]
    while j<=high:
        if j+1<=high and li[j+1]>li[j]: # right child exit and greater than the left child
            j += 1
        if li[j]>tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            break
    li[i] = tmp
    
@execute_time
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1)
    for i in range(n-1,-1,-1):
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1)

def merge(li,low,mid,high):
    i = low
    j = mid+1
    litmp = []
    while i <= mid and j <= high:
        if li[i]<li[j]:
            litmp.append(li[i])
            i += 1
        else:
            litmp.append(li[j])
            j += 1
    while i <= mid:
        litmp.append(li[i])
        i += 1
    while j <= high:
        litmp.append(li[j])
        j += 1
    return litmp

def _merge_sort(li,low,high):
    if low<high:
        mid = (low+high)//2
        _merge_sort(li,low,mid)
        _merge_sort(li,mid+1,high)
        merge(li,low,mid,high)
        
@execute_time
def merge_sort(li):
    _merge_sort(li,0,len(li)-1)