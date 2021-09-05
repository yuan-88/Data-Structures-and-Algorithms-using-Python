# Graph implementation
# Author: Y.

# Create a Adjacency list
class AdjacencyList(object):

    # Create an empty graph ( O(Nodes + Edge) )
    def __init__(self):
        super(AdjacencyList, self).__init__()
        self.list = {}

    # Add edge to graph
    def add_edge(self, from_node, to_node):
        if from_node in self.list.keys():
            self.list[from_node].append(to_node)
        else:
            self.list[from_node] = [to_node]
    
    # Remove edge from graph
    def remove_edge(self, from_node, to_node):
        for i, node in enumerate(self.list[from_node]):
            if to_node == node:
                self.list[from_node].pop(i)
                return
        print("No corresponding edge!")
    
    # Print graph
    def print_graph(self):
        for i in self.list.keys():
            print(i, '->', ' -> '.join([str(j) for j in self.list[i]]))
    
    # DFS
    def dfs(self, graph=None, start=None, visited=None):
        if graph is None:
            graph = self.list
        if visited is None:
            visited = []
        visited.append(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(graph=graph, start=neighbor, visited=visited)
        return visited

    # BFS
    def bfs(self, graph=None, start=None, visited=None):
        if graph is None:
            graph = self.list
        if visited is None:
            visited = []
        
        visited.append(start)
        queue = [start] 

        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited



if __name__=="__main__":

    print("\nTest add edge")
    al = AdjacencyList()
    al.add_edge('0', '1')
    al.add_edge('0', '4')
    al.add_edge('4', '1')
    al.add_edge('4', '3')
    al.add_edge('1', '0')
    al.add_edge('1', '4')
    al.add_edge('1', '3')
    al.add_edge('1', '2')
    al.add_edge('2', '3')
    al.add_edge('3', '4')
    al.print_graph()

    print("\nTest remove edge")
    al.remove_edge('1', '4')
    al.remove_edge('1', '5')
    al.print_graph()

    graph = {
        '0': ['1', '2', '3'],
        '1': ['0', '2'],
        '2': ['0', '1', '4'],
        '3': ['0'],
        '4': ['2'],
        }

    print(al.dfs(graph=graph, start='0'))
        
    print(al.bfs(graph=graph, start='0'))