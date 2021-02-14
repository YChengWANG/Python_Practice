from LinkedList import ListNode,LinkList

class solution:
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

data = [1,2,3,4,5,6]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)

res = s.reverseList_iter(i)
l.PrintList(res)