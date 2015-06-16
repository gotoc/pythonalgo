'''
Created on Jun 16, 2015

@author: Dmitry Marcautsan
'''
class BinarySearchTree(object):
    """Implementation of a Binary Search Tree data structure"""

    class Node(object):
        """Class for a single node in binary search tree"""
         
        def __init__(self, data, parent_node):
            self.data = data
            self.parent = parent_node
            self.left = None
            self.right = None

    def __init__(self, root_data=None):
        self.root = None
        if root_data is not None: self.root = self.Node(root_data, None)

    def insert(self, data):
        data_node = self.Node(data, None)

        if self.root is None:
            self.root = data_node
            return

        current = self.root
        next = current.left if current.data > data else current.right

        while next is not None:
            current = next
            next = current.left if current.data > data else current.right

        data_node.parent = current
        if current.data > data:
            current.left = data_node 
        else: 
            current.right = data_node

    def traverse_inorder(self, apply):
        if self.root is None:
            return

        self._visit_inorder(self.root, apply)
        
    def _visit_inorder(self, node, apply):
        if node.left is None and node.right is None:
            apply(node.data)
        elif node.left is None:
            apply(node.data)
            self._visit_inorder(node.right, apply)
        else:
            self._visit_inorder(node.left, apply)
            apply(node.data)
            if node.right is not None:
                self._visit_inorder(node.right, apply)

    def __str__(self):
        if self.root is None:
            return ""
        else:
            array = []
            self.traverse_inorder(array.append)

        return str(array)




