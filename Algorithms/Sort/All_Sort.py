def bubble_sort(li):    # O(n^2)
    for i in range(len(li)-1):
        sign = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                sign = True
        if sign == False:
            return


def select_sort(li):   # O(n^2)
    for i in range(len(li)-1):
        tmp = i
        for j in range(i+1,len(li)):
            if li[j]<li[tmp]:
                tmp = j
        li[i],li[tmp] = li[tmp],li[i]


def insert_sort(li):    # O(n^2)
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j -= 1
        li[j+1] = tmp

