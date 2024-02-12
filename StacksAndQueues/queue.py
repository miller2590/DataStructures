
class Node():
    """
    Represents a node in a queue.
    """

    def __init__(self, value) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class Queue():
    """
    Represents a queue data structure.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Queue class.
        """
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """
        Returns the value of the first element in the queue without removing it.

        Returns:
            The value of the first element in the queue, or None if the queue is empty.
        """
        if self.isEmpty():
            return None
        return self.first.value

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        Args:
            value: The value to be added to the queue.

        Returns:
            The updated queue.
        """
        newNode = Node(value)

        if self.isEmpty():
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
                
        self.length += 1
        return self

    def dequeue(self):
        """
        Removes and returns the first element in the queue.

        Returns:
            The value of the first element in the queue, or None if the queue is empty.
        """
        if self.isEmpty():
            return None
    
        dequeueNode = self.first

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = dequeueNode.next

        self.length -= 1
        return dequeueNode.value

    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        if self.length == 0:
            return True
        else:
            return False

    def showQueue(self):
        """
        Prints the elements in the queue.
        """
        if self.isEmpty():
            return None
        
        currentNode = self.first

        while currentNode != None:
            print(currentNode.value, end= " ")
            currentNode = currentNode.next
        print()


myQueue = Queue()
myQueue.enqueue("Jake")
myQueue.enqueue("George")
myQueue.enqueue("Sam")
myQueue.enqueue("Gage")
myQueue.showQueue()
print(myQueue.dequeue())
myQueue.showQueue()
print(f'Your queue has {myQueue.length} item(s)')