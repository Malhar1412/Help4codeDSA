# class Graph:
#     def __init__ (self):
#         self.adjancey_list={}  #dict

#     def add_Vertex(self, vertex):
#        if vertex not in self.adjancey_list.keys():
#         self.adjancey_list[vertex]=[]
#         return True
#        else:    
#         return False

#     def add_edge(self,vertex1, vertex2): 
#         if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():
#             self.adjancey_list[vertex1].append(vertex2)




#     #ddisply graph
#     def display_graph(self):
#         for vertex in self.adjancey_list.keys():
#             print(vertex,":",self.adjancey_list[vertex])    

    
# graph=Graph()
# #pass the num of vertex
# graph.add_Vertex('A')
# graph.add_Vertex('B')
# graph.add_Vertex('C')
# graph.add_Vertex('D')
# graph.add_Vertex('E')


# graph.add_edge('A','B')  #A:[AB]
# graph.add_edge('A','C')  #A:[ABC]
# graph.add_edge('A','D')  #A:[ABCD]

# graph.add_edge('B','A')  
# graph.add_edge('B','D')

# graph.add_edge('C','A')  
# graph.add_edge('C','E')

# graph.add_edge('D','E')  
# graph.add_edge('D','B')
# graph.add_edge('D','A')

# graph.add_edge('E','C')  
# graph.add_edge('E','D')



# graph.display_graph()










##########################################################################################################




class Graph:
    def __init__(self):
        self.adjancey_list = {}  # dictionary

    def add_Vertex(self, vertex):
        if vertex not in self.adjancey_list.keys():
            self.adjancey_list[vertex] = []
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():
            self.adjancey_list[vertex1].append(vertex2)
            return True
        return False

    # Delete Vertex
    def remove_vertex(self, vertex):
        if vertex in self.adjancey_list.keys():

            # Remove the vertex itself
            del self.adjancey_list[vertex]

            # Remove this vertex from all other vertices
            for other_vertex in self.adjancey_list:
                if vertex in self.adjancey_list[other_vertex]:
                    self.adjancey_list[other_vertex].remove(vertex)

            return True

        return False

    # Delete Edge
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():

            if vertex2 in self.adjancey_list[vertex1]:
                self.adjancey_list[vertex1].remove(vertex2)
                return True

        return False

    # Display Graph
    def display_graph(self):
        for vertex in self.adjancey_list.keys():
            print(vertex, ":", self.adjancey_list[vertex])


graph = Graph()

graph.add_Vertex('A')
graph.add_Vertex('B')
graph.add_Vertex('C')
graph.add_Vertex('D')
graph.add_Vertex('E')
graph.add_Vertex('F')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')

graph.add_edge('B', 'A')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')

graph.add_edge('C', 'A')
graph.add_edge('C', 'E')

graph.add_edge('D', 'B')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')

graph.add_edge('E', 'C')
graph.add_edge('E', 'D')
graph.add_edge('E', 'F')

graph.add_edge('F', 'D')
graph.add_edge('F', 'E')


print("Original Graph:")
graph.display_graph()


print("\nAfter deleting edge B -> E:")
graph.remove_edge('B', 'E')
graph.display_graph()


print("\nAfter deleting vertex E:")
graph.remove_vertex('E')
graph.display_graph()

