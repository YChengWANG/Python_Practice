from All_Reverse import reverse
from LinkedList import ListNode,LinkList

class solution(reverse):
    def reverseK(self,head:ListNode,k:int)->ListNode:
        if(head == None):
            return None
        start,end = head,head
        for _ in range(0,k):
            if(end==None):
                return head
            end = end.next
        newhead = self.reverseList_iter_ab(start,end)
        start.next = self.reverseK(end,k)
        return newhead

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = LinkList()
s = solution()
i = l.LinkedList(data=data)

res = s.reverseK(i,2)
l.PrintList(res)