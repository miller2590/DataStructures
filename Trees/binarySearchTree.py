class Node():
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
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
        pass

    def printTree(self, node, level=0):
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
print(tree.lookup(171))
print(tree.lookup(1))