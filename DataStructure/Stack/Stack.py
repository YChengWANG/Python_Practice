class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def is_empty(self):
        return len(self.stack)-1 == 0

    def print(self):
        for i in range(len(self.stack)):
            print(self.stack[i],end=' ')

