class Node():
    """
    Represents a node in a binary search tree.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    """
    Represents a binary search tree.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BinarySearchTree class.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.

        Args:
            value: The value to be inserted.
        """
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    else:
                        currentNode = currentNode.right

    def lookup(self, value):
        """
        Searches for a value in the binary search tree.

        Args:
            value: The value to be searched.

        Returns:
            True if the value is found, False otherwise.
        """
        if self.root is None:
            return False
        
        currentNode = self.root

        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
  
    def remove(self, value):
        """
        Removes a value from the binary search tree.

        Args:
            value: The value to be removed.

        Returns:
            True if the value is successfully removed, False otherwise.
        """
        if self.root is None:
            return False

        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # Case 1: No children
                if currentNode.left is None and currentNode.right is None:
                    if parentNode is None:
                        self.root = None
                    elif parentNode.left == currentNode:
                        parentNode.left = None
                    else:
                        parentNode.right = None
                    return True

                # Case 2: One child
                if currentNode.left is None:
                    if parentNode is None:
                        self.root = currentNode.right
                    elif parentNode.left == currentNode:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right
                    return True
                elif currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    elif parentNode.left == currentNode:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.right = currentNode.left
                    return True

                # Case 3: Two children
                successor = currentNode.right
                successorParent = currentNode
                while successor.left:
                    successorParent = successor
                    successor = successor.left

                if successorParent.left == successor:
                    successorParent.left = successor.right
                else:
                    successorParent.right = successor.right

                if parentNode is None:
                    self.root = successor
                elif parentNode.left == currentNode:
                    parentNode.left = successor
                else:
                    parentNode.right = successor

                successor.left = currentNode.left
                successor.right = currentNode.right
                return True

        return False
        
    def printTree(self, node, level=0):
        """
        Prints the binary search tree in an in-order traversal.

        Args:
            node: The root node of the tree.
            level: The current level of the node (used for indentation).
        """
        if node is None:
            return

        self.printTree(node.right, level + 1)
        print("    " * level + str(node.value))
        self.printTree(node.left, level + 1)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.printTree(tree.root)
tree.remove(20)
tree.printTree(tree.root)
print(tree.lookup(171))
print(tree.lookup(1))