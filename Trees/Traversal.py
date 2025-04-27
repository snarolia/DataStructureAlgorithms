from typing import Optional, List
import logging

from v3_BinaryTree import TreeNode, _build_binary_tree_from_array, _print_tree_level_order

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")


def _inorder_traversal(tree_arr:list)->list:
    treeObj=_build_binary_tree_from_array(tree_arr)
    arrViewOfTree=_print_tree_level_order(treeObj)

    stack=[]
    current=treeObj
    result=[]

    while stack or current:
        while current is not None:
            stack.append(current)
            current=current.left
        current=stack.pop()
        result.append(current.val)
        current=current.right
    return result

def _inorder_recursive(treeObj:TreeNode)->List:
    #treeObj=_build_binary_tree_from_array(tree_arr)
    """The tree object needs to be created outside the function because, otherwise array is called again and again and the actual traversal is using node.left and node.right, not array"""
    #arrViewOfTree=_print_tree_level_order(treeObj)

    result=[]
    if treeObj is None:
        return result
    result.extend(_inorder_recursive(treeObj.left))
    result.append(treeObj.val)
    result.extend(_inorder_recursive(treeObj.right))
    return result

def _preorder_traversal():
    pass

if __name__=="__main__":
    testTree_1=[1,2,3,4,5,None,8,None,None,6,7,9]
    print(_inorder_traversal(testTree_1))

    testTree_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, None]
    logging.info(_inorder_traversal(testTree_2))
    logging.info("In order traversal using recursion")
    testTree_Obj = _build_binary_tree_from_array(testTree_2)
    logging.info(_inorder_recursive(testTree_Obj))