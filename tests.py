from datastructures.LinkedList import LinkedList
from datastructures.BinarySearchTree import BinarySearchTree
from datastructures.AVLTree import AVLTree

tree = AVLTree()
tree.insert(10)
tree.insert(5)
tree.insert(11)
tree.insert(-4)

dir(tree.root)

print(tree)
input()

