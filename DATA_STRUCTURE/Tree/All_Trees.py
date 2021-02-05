class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None
    
class Treeoperation:
    def reverseTree(self,root:TreeNode):
        if(root==None):
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.reverseTree(root.left)
        self.reverseTree(root.right)