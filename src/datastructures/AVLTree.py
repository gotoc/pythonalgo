'''
Created on Jun 16, 2015

@author: Dmitry Marcautsan
'''
from datastructures.BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    '''Implementation of an AVL binary search tree'''
    class Node(BinarySearchTree.Node):
        def __init__(self, data, parent_node):
            BinarySearchTree.Node.__init__(self, data, parent_node)
    
    def __init__(self, root_data=None):
        BinarySearchTree.__init__(self, root_data)
        