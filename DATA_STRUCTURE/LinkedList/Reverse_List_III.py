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

    def reverseList_mn(self,head:ListNode,m:int,n:int)->ListNode:
        if m==1:
            return self.reverseList_n(head,n)
        head.next = self.reverseList_mn(head.next,m-1,n-1)
        return head

data = [1,2,3,4,5,6]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)
l.PrintList(i)

res = s.reverseList_mn(i,3,4)
l.PrintList(res)