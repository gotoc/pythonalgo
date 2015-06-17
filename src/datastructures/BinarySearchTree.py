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
        next_node = current.left if current.data > data else current.right

        while next_node is not None:
            current = next_node
            next_node = current.left if current.data > data else current.right

        data_node.parent = current
        if current.data > data:
            current.left = data_node 
        else: 
            current.right = data_node
            
        self._after_insert_hook(data_node)
        
    def delete(self, data):
        found_node = self._find_node(data, self.root)
        self._delete_node(found_node)
    
    def _delete_node(self, node):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            if self.root is node:
                self.root = None
            else:
                self._replace_subtree(node, None)
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right
            self._replace_subtree(node, child_node)
        else:
            child_node = self._find_min_node(node.right)
            
            self._delete_node(child_node)
            self._replace_subtree(node, child_node)
            
            child_node.left = node.left
            child_node.right = node.right
            if child_node.left is not None:
                child_node.left.parent = child_node
            if child_node.right is not None:
                child_node.right.parent = child_node
        
        node.parent = node.left = node.right = None
        
        self._after_delete_hook(node)
        return node   

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
                
    def _after_insert_hook(self, node):
        pass
    
    def _after_delete_hook(self, node):
        pass

    def _find_node(self, data, subtree_root):              
        if subtree_root is None:
            return None
        elif subtree_root.data == data:
            return subtree_root
        else:
            return self._find_node(data, subtree_root.left if data < subtree_root.data else subtree_root.right)
        
    def _find_min_node(self, subtree_root):
        if subtree_root.left is None:
            return subtree_root
        else:
            return self._find_min_node(subtree_root.left)
    
    def _replace_subtree(self, subtree_root, replace_root):
        if subtree_root.parent is not None:
            if subtree_root.parent.left is subtree_root:
                subtree_root.parent.left = replace_root
            else:
                subtree_root.parent.right = replace_root
                
        if replace_root is not None:   
            replace_root.parent = subtree_root.parent   

    def __str__(self):
        if self.root is None:
            return ""
        else:
            array = []
            self.traverse_inorder(array.append)

        return str(array)




