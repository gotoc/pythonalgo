from datastructures.LinkedList import LinkedList
from datastructures.BinarySearchTree import BinarySearchTree
from datastructures.AVLTree import AVLTree

tree = AVLTree(5)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(6)
tree.insert(8)
print(tree)

tree.delete(8)
print(tree)

tree.delete(7)
print(tree)

tree.delete(2)
print(tree)

input()

