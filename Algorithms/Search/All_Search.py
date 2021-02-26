def linearsearch(li,val):
    for ind,v in enumerate(li):
        if v==val:
            return ind
    else:
        return None

def binarysearch(li,val):
    left = 0
    right = len(li)-1
    while left<=right:
        mid = (left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]<val:
            left = mid+1
        elif li[mid]>val:
            right = mid-1
    return None

