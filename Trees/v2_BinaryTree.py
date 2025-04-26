import os
from typing import List, Optional
import logging
from random import random, randint

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


def build_tree_from_list():
    pass

# tree=TreeNode(4,5,6)
TreeList=[]
for _ in range(4):
    TreeList.append(TreeNode(randint(1,5), randint(5,10), randint(11,15)))

for _ in TreeList:
    logging.info(_.val)
    logging.info(_.left)
    logging.info(_.right)
