from LinkedList import ListNode,LinkList

class Traverse:
    def isPalindrome(self,head:ListNode)->bool:
        self.left = head
        return self.traverse(head)
        
    def traverse(self,right:ListNode)->bool:
        if(right==None):
            return True
        res = self.traverse(right.next)
        #后续遍历
        res = res and (self.left.val==right.val)
        self.left = self.left.next
        return res


data = [0,1,2,2,1,0]
l = LinkList()
s = Traverse()
i = l.LinkedList(data=data)
#l.PrintList(i)

res = s.isPalindrome(i)
print(res)