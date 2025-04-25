import logging
from typing import Optional
import logging.config
import array as arr

logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s")

class Node:
    def __init__(self, value, left: Optional['Node'] = None, right: Optional['Node']=None):
        self.data=value
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self, root_value):
        self.root=Node(root_value)
    
    def _insert(self,value):
        new_node=Node(value)
        queue=[self.root]
        
        while queue:
            current=queue.pop(0)
            if current.left is None:
                current.left=new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right=new_node
                return
            else:
                queue.append(current.right)
        queue.clear()

    def _BFSTree(self):
        queue=[self.root]
        tree_arr=[]
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.pop(0)
                tree_arr.append(node)
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
        return tree_arr

    
## Below Logic is not working properly    
    # def _generate_tree_array(self):
    #     curr=self.root
    #     result=[]
    #     node_list=[(self.root.data, 0)]
    #     i=0
    #     c_l, c_r= 0,0
    #     if not self.root:
    #         return []
    #     result.append((self.root.data, 0))
    #     while (curr.left) or (curr.right):
    #         c_l, c_r=2*i+1, 2*i+2
    #         result.append((curr.left.data, c_l)) if curr.left else result.append((None, c_l))
    #         result.append((curr.right.data, c_r)) if curr.left else result.append((None, c_r))
    #         i+=1
    #         curr=curr.left if curr.left else curr.right
    #     return result







Root=BinaryTree('A')
Root._insert('F')
Root._insert('B')
Root._insert('D')
Root._insert('C')
Root._insert('E')


# logging.info("Left Nodes traversed from root are")
# logging.info(f"{Root.root.data}->{Root.root.left.data}->{Root.root.left.left.data}")

tree_arr=Root._BFSTree()
for _ in tree_arr:
    print(_.data)
# temp=[(1,2), (3,4)]
# x,y=temp.pop(0)
# print(x,y)