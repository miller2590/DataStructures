
class listStack():
    """
    This class represents a stack implemented using a list.
    """

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        self.array = []

    def peek(self): # O(1)
        """
        Returns the top element of the stack without removing it.
        If the stack is empty, returns None.
        """
        if self.isEmpty():
            return None
        return self.array[len(self.array) - 1]

    def push(self, value): # O(1)
        """
        Adds an element to the top of the stack.
        Returns the updated stack.
        """
        self.array.append(value)
        return self
            
    def pop(self): # O(1)
        """
        Removes and returns the top element of the stack.
        If the stack is empty, returns None.
        """
        if self.isEmpty():
            return None
        return self.array.pop()
        
    def isEmpty(self): # O(1)
        """
        Checks if the stack is empty.
        Returns True if the stack is empty, False otherwise.
        """
        if len(self.array) == 0:
            return True
        else:
            return False
    
    def showStack(self): # O(n)
        """
        Prints the elements of the stack.
        """
        print(self.array)    

myStack = listStack()

myStack.push(5)
myStack.push(47)
myStack.push(23)
myStack.push(62)
print(myStack.peek())
print(myStack.pop())
myStack.showStack()
print(f'Your stack has {len(myStack.array)} item(s)')
