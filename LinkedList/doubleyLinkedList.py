"""
This file contains the implementation of a doubly linked list data structure.
"""

class Node():
    """
    Represents a node in a doubly linked list.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList():
    """
    Represents a doubly linked list.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the DoublyLinkedList class.

        Args:
            value: The value to be stored in the first node of the list.
        """
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value: The value to be stored in the new node.
        """
        newNode = Node(value)
        
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        """
        Prepends a new node with the given value to the beginning of the list.

        Args:
            value: The value to be stored in the new node.
        """
        newNode = Node(value)

        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        self.length += 1

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the list.

        Args:
            index: The index at which the new node should be inserted.
            value: The value to be stored in the new node.
        """
        if index >= self.length:
            return self.append(value)
        if index <= 0:
            return self.prepend(value)
        else:
            newNode = Node(value)

            nodeBeforeInsert = self.lookUp(index - 1)
            nodeAfterInsert = nodeBeforeInsert.next
            nodeBeforeInsert.next = newNode
            newNode.previous = nodeBeforeInsert
            nodeAfterInsert.previous = newNode
            newNode.next = nodeAfterInsert
        self.length += 1

    def lookUp(self, index):
        """
        Returns the node at the specified index in the list.

        Args:
            index: The index of the node to be returned.

        Returns:
            The node at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= self.length:
            raise IndexError("Index out of range")
        currentNode = self.head
        counter = 0

        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def remove(self, index):
        """
        Removes the node at the specified index from the list.

        Args:
            index: The index of the node to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
        else:    
            nodeBeforeTarget = self.lookUp(index - 1)
            targetNode = nodeBeforeTarget.next
            nodeAfterTarget = targetNode.next
            nodeBeforeTarget.next = nodeAfterTarget
            if nodeAfterTarget:
                nodeAfterTarget.previous = nodeBeforeTarget
        self.length -= 1

    def printList(self):
        """
        Prints the values of all nodes in the list.
        """
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=' ')
            currentNode = currentNode.next
        print()


dblLinked = DoublyLinkedList(10)

dblLinked.append(5)
dblLinked.append(30)
dblLinked.prepend(27)
dblLinked.insert(1, 48)
print(dblLinked.length)
dblLinked.remove(2)
print(dblLinked.length)
dblLinked.printList()

