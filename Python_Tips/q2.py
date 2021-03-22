n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split())) 

A_set = set(A)
B_set = set(B)

li1 = [li1 for li1 in A_set]
li2 = [li2 for li2 in B_set]

x = 0

if li1[0]%m<li2[0]%m:
    x = li2[0]%m-li1[0]%m
else:
    x =li2[0]%m + m -li1[0]%m

print(x)
    