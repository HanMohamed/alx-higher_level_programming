#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list by:
    - Private instance attribute: data:
        - property def data(self): to retrieve it
        - property setter def data(self, value): to set it:
            - data must be an integer, otherwise raise a TypeError exception
              with the message data must be an integer
    - Private instance attribute: next_node:
        - property def next_node(self): to retrieve it
        - property setter def next_node(self, value): to set it:
            - next_node can be None or must be a Node, otherwise raise a
              TypeError exception with the message:
              next_node must be a Node object
    - Instantiation with data and next_node:
      def __init__(self, data, next_node=None):
"""


class Node:
    """ a class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node

        Args:
            data (int): value
            next_node (Node, optional): Defaults to None.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data of node"""

        return self.__data

    @data.setter
    def data(self, value):
        """A setter function to set data of a node"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """A setter function to set next node of a node"""

        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" write a class SinglyLinkedList that defines a singly linked list by:
    - Private instance attribute: head (no setter or getter)
    - Simple instantiation: def __init__(self):
    - Should be printable:
        - print the entire list in stdout
        - one node number by line
    - Public instance method: def sorted_insert(self, value): that inserts a
      new Node into the correct sorted position in the list (increasing order)
"""


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """Initialize a new SinglyLinkedList"""

        self.__head = None

    def __str__(self):
        """print the entire list in stdout one node number by line"""

        curr = self.__head
        str_rep = ""
        while curr:
            str_rep += str(curr.data)
            if curr.next_node is not None:
                str_rep += "\n"
            curr = curr.next_node
        return str_rep

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)
        """

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
