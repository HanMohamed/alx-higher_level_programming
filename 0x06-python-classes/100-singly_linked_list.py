#!/usr/bin/python3
"""_summary_

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
"""
    

class Node:
    """ a class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """_summary_

        Args:
            data (_type_): _description_
            next_node (_type_, optional): _description_. Defaults to None.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
    
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list """
    
    def __init__(self):
        self.__head = None

    def __str__(self):
        curr = self.__head
        str_rep = ""
        while curr:
            str_rep += str(curr.data)
            if curr.next_node is not None:
                str_rep += "\n"
            curr = curr.next_node
        return str_rep

    def sorted_insert(self, value):
        new_node = Node(value, None)
        prev_curr = None
        curr_node = self.__head
        if self.__head is None or curr_node.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        while curr_node:
            if curr_node.data < new_node.data:
                prev_curr = curr_node
                curr_node = curr_node.next_node
            else:
                break
        prev_curr.next_node = new_node
        new_node.next_node = curr_node
        