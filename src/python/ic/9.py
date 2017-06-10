"""
is the given binary tree a valid binary search tree?
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


def is_bst(node):
    def traverse(node, lower_bound, upper_bound):
        if node == None:
            return True
        if node.value >= lower_bound and node.value <= upper_bound:
            return traverse(node.left, lower_bound, node.value) and traverse(node.right, node.value, upper_bound)
        else:
            return False
    
    return traverse(node, float('-inf'), float('inf'))
            


from eight import build_random_binary_search_tree
from eight import  build_random_binary_tree
from eight import inorder_traversal

def is_superbalance():
    bst_bst_count = 0
    from_random_bst_count = 0
    test_count = 100000
    node_count = 7
    for i in range(test_count):
        if is_bst(build_random_binary_search_tree(node_count)):
            bst_bst_count+=1
        if is_bst(build_random_binary_tree(node_count)):
            from_random_bst_count+=1

    assert(bst_bst_count == test_count)
    print "Created bst from random trees %d times " % from_random_bst_count



def find_2nd_largest_in_bst(root):
    parent = root
    while root.right:
        parent = root
        root = root.right
    if parent:
        return parent.value

if __name__ == "__main__":
    root = build_random_binary_search_tree(10)
    inorder_traversal(root)
    print "second largest: ", find_2nd_largest_in_bst(root)
