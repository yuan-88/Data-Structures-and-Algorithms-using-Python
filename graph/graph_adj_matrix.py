# Graph implementation
# Author: Y.

# Create a Adjacency list
class AdjacencyMatrix(object):

    # Create an empty matrix ( O(Nodes^2) )
    def __init__(self, size):
        super(AdjacencyMatrix, self).__init__()
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for i in range(size)])
        self.size = size

    # Add edge to graph
    def add_edge(self, from_node, to_node):
        if from_node == to_node:
            print(f"Same nodes {from_node} and {to_node} ")
        self.matrix[from_node][to_node] = 1
        self.matrix[to_node][from_node] = 1

    # Remove edge from graph
    def remove_edge(self, from_node, to_node):
        if self.matrix[from_node][to_node] == 0:
            print(f"No edges between {from_node} and {to_node} ")
        self.matrix[from_node][to_node] = 0
        self.matrix[to_node][from_node] = 0

    # Print graph
    def print_graph(self):
        for row in self.matrix:
            for col in row:
                print(f'{col}', end=' ')
            print()

    # DFS
    def dfs(self, graph, start, visited):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)

        for next in graph[start] - visited:
            self.dfs(graph. next, visited)
        return visited
    

if __name__=="__main__":
    
    print("\nTest add edge")
    am = AdjacencyMatrix(6)
    am.add_edge(0, 1)
    am.add_edge(0, 4)
    am.add_edge(4, 1)
    am.add_edge(4, 3)
    am.add_edge(1, 0)
    am.add_edge(1, 4)
    am.add_edge(1, 3)
    am.add_edge(1, 2)
    am.add_edge(2, 3)
    am.add_edge(3, 4)
    am.print_graph()




    print("\nTest remove edge")
    am.remove_edge(1, 4)
    am.remove_edge(1, 5)
    am.print_graph()