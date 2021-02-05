from LinkedList import ListNode,LinkList

class solution:
    def reverseList(self,head:ListNode)->ListNode:
        if(head.next==None): return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

data = [1,2,3,4,5,6]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)

res = s.reverseList(i)
l.PrintList(res)