from LinkedList import ListNode,LinkList

class solution:
    def reverseList_n(self,head:ListNode,n:int)->ListNode:
        global successor
        if(n==1):
            successor = head.next
            return head
        last = self.reverseList_n(head.next,n-1)
        head.next.next = head
        head.next = successor
        return last


data = [1,2,3,4,5,6]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)
l.PrintList(i)

res = s.reverseList_n(i,2)
l.PrintList(res)