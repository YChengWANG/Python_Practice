from LinkedList import ListNode,LinkList

class reverse():
    def reverseList(self,head:ListNode)->ListNode:
        if(head.next==None): return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
    
    def reverseList_iter(self,head:ListNode)->ListNode:
        pre = None
        nxt = head
        cur = head
        while(cur!=None):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
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

    def reverseList_iter_ab(self,a:ListNode,b:ListNode)->ListNode:
        pre = b
        cur = a
        nxt = a
        while(cur != b):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre