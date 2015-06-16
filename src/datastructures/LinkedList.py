'''
Created on Jun 16, 2015

@author: Dmitry Marcautsan
'''
class LinkedList(object):
    """Implementation of a linked list data structure"""

    class Node(object):
        """Class for a single node in linked list"""

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = self.Node(data)
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = self.Node(data)

    def __str__(self):
        if self.head is None:
            return ""
        else:
            array = []
            node = self.head
        
            while node is not None:
                array.append(node.data)
                node = node.next

        return str(array)
