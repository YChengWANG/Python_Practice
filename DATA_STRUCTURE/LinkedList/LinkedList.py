class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def LinkedList(self,data):
        self.head = ListNode(data[0])
        Head = self.head
        Tail = self.head
        for i in data[1:]:
            node = ListNode(i)
            Tail.next = node
            Tail = Tail.next
        return Head
    
    def PrintList(self,head):
        if head==None: return 
        node = head
        while node != None:
            print(node.val,end="->")
            node = node.next
        print("null")