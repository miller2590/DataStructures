"""
This file contains the implementation of a linked list data structure in Python.
"""

class Node():
    """
    Represents a node in a linked list.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList():
    """
    Represents a linked list data structure.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the LinkedList class.

        Args:
            value: The value to be stored in the first node of the linked list.
        """
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value): # O(1)
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be stored in the new node.
        """
        newNode = Node(value)

        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value): # O(1)
        """
        Prepends a new node with the given value to the beginning of the linked list.

        Args:
            value: The value to be stored in the new node.
        """
        newNode = Node(value)

        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index: int, value): # O(n)
        """
        Inserts a new node with the given value at the specified index in the linked list.

        Args:
            index: The index at which the new node should be inserted.
            value: The value to be stored in the new node.
        """
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        else:
            newNode = Node(value)
            nodeBeforeInsert = self.lookUp(index - 1)
            nodeAfterInsert = nodeBeforeInsert.next
            nodeBeforeInsert.next = newNode
            newNode.next = nodeAfterInsert
        self.length += 1

    def lookUp(self, index: int): # O(n)
        """
        Returns the node at the specified index in the linked list.

        Args:
            index: The index of the node to be returned.

        Returns:
            The node at the specified index.
        """
        currentNode = self.head
        counter = 0

        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode
    
    def remove(self, index: int): # O(n)
        """
        Removes the node at the specified index from the linked list.

        Args:
            index: The index of the node to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        else:    
            nodeBeforeTarget = self.lookUp(index - 1)
            targetNode = nodeBeforeTarget.next
            nodeBeforeTarget.next = targetNode.next
        self.length -= 1

    def printList(self): # O(n)
        """
        Prints the values of all nodes in the linked list.
        """
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end = ' ')
            currentNode = currentNode.next
        print()
    


myList = LinkedList(10)
myList.append(13)
myList.prepend(8)
myList.insert(2, 5)
myList.printList()
myList.remove(2)
myList.printList()

print(f'Length of Linked List is: {myList.length}')