# Task 1: BFS Traversal of a Graph using Add Edge Function & Parameters

class Graph:
    def __init__(self):
        # Parallel lists to store graph data without using direct dict assignment
        self.nodes = []
        self.adj_list = []

    # Function parameter ke zariye graph mein edges add karna
    def add_edge(self, u, v):
        # Vertex 'u' ko check aur add karna
        u_exists = False
        u_index = -1
        for i in range(len(self.nodes)):
            if self.nodes[i] == u:
                u_exists = True
                u_index = i
                break

        if not u_exists:
            self.nodes.append(u)
            self.adj_list.append([v])
        else:
            self.adj_list[u_index].append(v)

        # Undirected graph ke liye 'v' ko bhi 'u' ke saath connect karna
        v_exists = False
        v_index = -1
        for i in range(len(self.nodes)):
            if self.nodes[i] == v:
                v_exists = True
                v_index = i
                break

        if not v_exists:
            self.nodes.append(v)
            self.adj_list.append([u])
        else:
            self.adj_list[v_index].append(u)

    def bfs_traversal(self, start_node):
        # 1. Start node exist karta hai ya nahi check karna (Manual Loop Check)
        node_exists = False
        for node in self.nodes:
            if node == start_node:
                node_exists = True
                break

        if not node_exists:
            print("Error: Start node not found in graph.")
            return

        # 2. Pure List Data Structures (No set, no deque)
        visited = []
        queue = []
        traversal_order = []

        # Start node ko enqueue aur visited mark karna
        queue.append(start_node)
        visited.append(start_node)

        while len(queue) > 0:
            # Queue ke front se node nikalna (FIFO) - Manual pop(0)
            current_vertex = queue.pop(0)
            traversal_order.append(current_vertex)

            # Connected neighbors ko manually fetch karna
            neighbors = []
            for i in range(len(self.nodes)):
                if self.nodes[i] == current_vertex:
                    neighbors = self.adj_list[i]
                    break

            # Unvisited neighbors ko queue mein add karna
            for neighbor in neighbors:
                # Manual visited check (No 'in' operator / No set)
                already_visited = False
                for v in visited:
                    if v == neighbor:
                        already_visited = True
                        break

                if not already_visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        # 3. Traversal Order String Output (No " -> ".join())
        formatted_output = ""
        for i in range(len(traversal_order)):
            if i == len(traversal_order) - 1:
                formatted_output += str(traversal_order[i])
            else:
                formatted_output += str(traversal_order[i]) + " -> "

        print("BFS Traversal Order:", formatted_output)


# --- Execution ---
my_graph = Graph()

# Function parameters ke zariye Graph Data add karna
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 4)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(1, 4)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)

# Execution
my_graph.bfs_traversal(0)