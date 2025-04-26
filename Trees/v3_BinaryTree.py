import os
from typing import Optional, List
from collections import deque
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


def _build_binary_tree_from_array(arr:list):
    if len(arr)==0:
        return None
    
    root=TreeNode(arr[0])
    stack=[root]
    i=1 # To iterate over array_items to sonfigure right and left of current node

    while stack and (i<len(arr)):
        current=stack.pop(0)
        if i<len(arr) and arr[i] is not None:
            current.left=TreeNode(val=arr[i])
            stack.append(current.left)
        i+=1

        if i<len(arr) and arr[i] is not None:
            current.right=TreeNode(val=arr[i])
            stack.append(current.right)
        i+=1
    
    return root

def _print_tree_level_order(root:TreeNode):
    if not root:
        return []
    stack=[root]
    result=[]
    while stack:
        node=stack.pop(0)
        if node:
            result.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result

if __name__=="__main__":
    logging.info("Starting the demo of Binary Tree setup and traversal")
    logging.info("Working for below input:")
    logging.info("[1, 2, 3, None, 4, 5]")
    
    tree_arr_1=[1, 2, 3, None, 4, 5]
    root=_build_binary_tree_from_array(tree_arr_1)
    curr=root
    # while curr:
    #     print(curr.val)
    #     curr=curr.left
    logging.info(f"The tree node are: {root}")
    logging.info(_print_tree_level_order(root))


    tree_arr_2 = [None, None, None]
    tree_arr_3 = [1, None, None, None]
    tree_arr_4 = [1,5,6,9,10,None,4, None]

    tree_list = [tree_arr_1, tree_arr_2, tree_arr_3, tree_arr_4]
    
    for _ in tree_list:
        temp_root=_build_binary_tree_from_array(_)
        logging.info(_print_tree_level_order(temp_root))