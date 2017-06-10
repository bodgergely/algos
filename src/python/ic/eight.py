"""
decide if a binary tree is super-balanced (difference of depth of any two leaf nodes is no greater than 1)
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

import random


def build_random_binary_search_tree(node_count):
    root = BinaryTreeNode(random.randint(0, 100))
    for i in range(node_count-1):
        newnode = BinaryTreeNode(random.randint(0, 100))
        node = root
        while True:
            if newnode.value <= node.value:
                if node.left == None:
                    node.left = newnode
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = newnode
                    break
                else:
                    node = node.right

    return root

def build_random_binary_tree(node_count):
    root = BinaryTreeNode(random.randint(0, 100))
    for i in range(node_count-1):
        newnode = BinaryTreeNode(random.randint(0, 100))
        node = root
        while True:
            side = random.randint(0,1)
            if side == 0:
                if not node.left:
                    node.left = newnode
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = newnode
                    break
                else:
                    node = node.right
    return root

def height(root):
    if root == None:
        return 0
    else:
        left_count = 1 + height(root.left)
        right_count = 1 + height(root.right)
        return max(left_count, right_count)

def leaf_diff(root):
    def traverse(root,level, diff):
        if root == None:
            if level < diff['min_leaf']:
                diff['min_leaf'] = level
            if level > diff['max_leaf']:
                diff['max_leaf'] = level
            return
        traverse(root.left, level+1, diff)
        traverse(root.right, level+1, diff)
    diff = {'min_leaf':float('inf'), 'max_leaf':float('-inf')}
    traverse(root, 0, diff)
    print "max_leaf: ", diff['max_leaf'], " min_leaf: ", diff['min_leaf']
    return diff['max_leaf'] - diff['min_leaf']

def is_super_balanced(root):
    def traverse(root, level, diffs):
        if diffs['max_leaf'] - diffs['min_leaf'] > 1:
            return False
        if root == None:
            if level < diffs['min_leaf']:
                diffs['min_leaf'] = level
            if level > diffs['max_leaf']:
                diffs['max_leaf'] = level
            return True
        return traverse(root.left, level+1, diffs) and traverse(root.right, level+1, diffs)
    diffs = {'min_leaf':float('inf'), 'max_leaf':float('-inf')}
    return traverse(root, 0, diffs)
                
                

def preorder_traversal(node):
    if node == None:
        return
    print node.value
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print node.value
    inorder_traversal(node.right)    

if __name__ == "__main__":
    root = build_random_binary_search_tree(10)
    inorder_traversal(root)
    print "Height: ", height(root)
    print "Diff: ", leaf_diff(root)
    print "Is super balanced: ", is_super_balanced(root)