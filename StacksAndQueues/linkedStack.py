
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

class Stack():
    """
    Represents a stack data structure implemented using a linked list.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Stack class.
        """
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self): # O(1)
        """
        Returns the value of the top element in the stack without removing it.

        Returns:
            The value of the top element in the stack, or None if the stack is empty.
        """
        if self.isEmpty():
            return None
        else:
            return self.top.value

    def push(self, value): # O(1)
        """
        Adds a new element to the top of the stack.

        Args:
            value: The value to be added to the stack.
        
        Returns:
            The updated stack.
        """
        newNode = Node(value)
        
        if self.isEmpty():
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self
            
    def pop(self): # O(1)
        """
        Removes and returns the top element from the stack.

        Returns:
            The value of the top element in the stack, or None if the stack is empty.
        """
        if self.isEmpty():
            return None
        
        poppedNode = self.top

        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1
        return poppedNode.value


    def isEmpty(self): # O(1)
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        if self.length == 0:
            return True
        else:
            return False
    
    def showStack(self): # O(n)
        """
        Prints the elements of the stack.
        """
        currentNode = self.top

        while currentNode != None:
            print(currentNode.value, end= " ")
            currentNode = currentNode.next
        print()    

myStack = Stack()

myStack.push(5)
myStack.push(29)
myStack.push(98)
myStack.push(49)
myStack.showStack()
print(myStack.peek())
print(myStack.pop())
myStack.showStack()
print(f'Your stack has {myStack.length} item(s)')
