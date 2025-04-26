from typing import Optional, List

class TreeNode:
    def __init__(self, val=0 ,left=None ,right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode])->List[int]:
        if not root:
            return []
        else:
            stack=[]
            result=[]
            current=root

        while current or stack:
                while current:
                    stack.append(current)
                    current=current.left
                current=stack.pop(0)
                result.append(current.val)
                current=current.right
        return result

    

if __name__=="__main__":
    print("Hello World")
    root=[1, None,2,3]
    sol=Solution()
    print(sol.inorderTraversal(root=root))
