dirs = [
    lambda x,y: (x-1,y),
    lambda x,y: (x,y+1),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1)
]

stack = []
stack.append((2,2))
print(stack[-1])