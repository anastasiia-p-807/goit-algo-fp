import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def rgb_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def generate_color_sequence(total_steps):
    colors = []
    for i in range(total_steps):
        intensity = int(255 * (i / total_steps))
        colors.append(rgb_hex(intensity, intensity, 255))
    return colors

def dfs(tree_root):
    stack = [tree_root]
    visited = []
    colors = generate_color_sequence(sum(1 for _ in nodes(tree_root)))
    
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            stack.extend(n for n in [node.right, node.left] if n)
            current_colors = [colors[i] if nodes(tree_root)[i] in visited else "#cccccc" for i in range(len(nodes(tree_root)))]
            draw_tree(tree_root, current_colors)

def bfs(tree_root):
    queue = [tree_root]
    visited = []
    colors = generate_color_sequence(sum(1 for _ in nodes(tree_root)))
    
    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            visited.append(node)
            queue.extend(n for n in [node.left, node.right] if n)
            current_colors = [colors[i] if nodes(tree_root)[i] in visited else "#cccccc" for i in range(len(nodes(tree_root)))]
            draw_tree(tree_root, current_colors)

def nodes(tree_root):
    queue = [tree_root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node)
            queue.extend([node.left, node.right])
    return result


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("\n\nDFS:\n")
dfs(root)

print("\n\nBFS:\n")
bfs(root)
