class TreeSearch:
    def __init__(self):
        self.parents = []
        self.children = []

    # Tree mein nodes add karne ka function (Single string pass karne ke liye adjusted)
    def add_node(self, parent_node, child_node):
        # Space ya empty string ko ignore karna
        child_node = child_node.strip()
        
        if parent_node in self.parents:
            idx = self.parents.index(parent_node)
            if child_node:  # Agar child valid node hai
                self.children[idx].append(child_node)
        else:
            self.parents.append(parent_node)
            self.children.append([child_node] if child_node else [])

    # BFS search method with start_node and goal_node parameters
    def bfs_find_goal(self, start_node, goal_node):
        # 1. Start node exist karta hai ya nahi check karna
        if start_node not in self.parents:
            print("Error: Start node not found in tree.")
            return

        # 2. Tracking Lists
        visited = []
        queue = []
        traversal_path = []

        queue.append(start_node)
        visited.append(start_node)

        while len(queue) > 0:
            current = queue.pop(0)
            traversal_path.append(current)

            # Goal node check
            if current == goal_node:
                print("Goal node found!")
                
                # Path formatting
                path_str = " -> ".join(traversal_path)
                print("Traversal Path:", path_str)
                return traversal_path

            # Current node ke neighbors fetch karna
            neighbors = []
            for i in range(len(self.parents)):
                if self.parents[i] == current:
                    neighbors = self.children[i]
                    break

            # Unvisited neighbors ko queue mein add karna
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        print("Goal node not found.")


# --- Execution ---
search = TreeSearch()

# AAPKA WAHI DİYA HUA INPUT FORMAT:
search.add_node('A', 'B')
search.add_node('A', 'F')
search.add_node('A', 'D')
search.add_node('A', 'E')
search.add_node('B', 'K')
search.add_node('B', 'J')
search.add_node('F', ' ')
search.add_node('D', 'G')
search.add_node('E', 'C')
search.add_node('E', 'H')
search.add_node('E', 'I')
search.add_node('K', 'M')
search.add_node('K', 'N')
search.add_node('J', '')
search.add_node('G', '')
search.add_node('C', '')
search.add_node('H', '')
search.add_node('I', 'L')
search.add_node('N', '')
search.add_node('M', '')
search.add_node('L', '')

# Search function call
search.bfs_find_goal('A', 'G')