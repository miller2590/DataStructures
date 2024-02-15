class Graph():
    """
    This class represents an undirected graph.

    Attributes:
        numberOfNodes (int): The number of nodes in the graph.
        adjacentList (dict): A dictionary representing the adjacency list of the graph.

    Methods:
        addVertex(node): Adds a vertex to the graph.
        addEdge(node1, node2): Adds an edge between two nodes in the graph.
        showConnections(): Prints the connections between nodes in the graph.
    """

    def __init__(self) -> None:
        """
        Initializes an empty graph with zero nodes and an empty adjacency list.
        """
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node): # O(1)
        """
        Adds a vertex to the graph.

        Args:
            node: The node to be added.

        Returns:
            None
        """
        if node is not None:
            self.adjacentList[node] = []
            self.numberOfNodes += 1
        return None

    def addEdge(self, node1, node2): # O(1)
        """
        Adds an edge between two nodes in the graph.

        Args:
            node1: The first node.
            node2: The second node.

        Raises:
            KeyError: If either of the nodes is not found in the graph.

        Returns:
            None
        """
        # Undirected Graph
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
        else:
            raise KeyError("Nodes not found")

    def showConnections(self): # O(v + e)
        """
        Prints the connections between nodes in the graph.

        Returns:
            None
        """
        allNodes = dict.keys(self.adjacentList)

        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            
            for vertex in nodeConnections:
                connections += str(vertex) + " "
            
            print(node + "-->" + connections)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
myGraph.showConnections()
