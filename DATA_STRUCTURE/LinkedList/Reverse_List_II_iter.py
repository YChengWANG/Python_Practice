from LinkedList import ListNode,LinkList

class solution:
    def reverseList_iter_ab(self,a:ListNode,b:ListNode)->ListNode:
        pre = b
        cur = a
        nxt = a
        while(cur!=b):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)

res = s.reverseList_iter_ab(i,i.next.next.next)
l.PrintList(res)