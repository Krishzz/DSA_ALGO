"""Tree DS"""


class TreeNode:
    """Nodes for the Tree DS"""

    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    """Design a Tree DS"""

    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, val, parentdata=None):
        node = TreeNode(val)
        if not self.root:
            self.root = node
            return
        parentNode = self.findnode(parentdata, self.root)
        if not parentNode:
            print('Parent Node not found in the Tree')
            return
        parentNode.children.append(node)

    def findnode(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            parentNode = self.findnode(data, child)
            return parentNode
        return None

    def display_all_nodes(self, depth=0, node=None):
        if not self.root:
            self.depth = 0
            print('Tree is empty')
            return
        if not node:
            node = self.root
        self.depth = max(self.depth, depth)
        print(" " * depth, node.data)
        for child in node.children:
            self.display_all_nodes(depth + 1, child)

    def max_depth_of_tree(self):
        return self.depth

    def remove_node(self, data):
        if not self.root:
            print('Tree is empty')
            return
        if self.root.data == data:
            self.root = None
            return
        parent_node = self.findParentNode(data, self.root)
        if parent_node:
            for child in parent_node.children:
                if child.data == data:
                    parent_node.children.remove(child)
                    return
        else:
            print('given value is not found in the Tree')

    def findParentNode(self, data, node):
        for child in node.children:
            if child.data == data:
                return node
            node_found = self.findParentNode(data, child)
            if node_found:
                return node_found
            return


tree = Tree()
tree.add(2)
tree.add(5, 2)
tree.add(3, 2)
tree.add(4, 2)
tree.add(6, 5)
tree.add(5, 7)
tree.display_all_nodes()
print('depth: ', tree.max_depth_of_tree())
tree.remove_node(6)
tree.remove_node(5)
tree.display_all_nodes()
print('depth: ', tree.max_depth_of_tree())

tree.remove_node(2)
tree.display_all_nodes()
print('depth: ', tree.max_depth_of_tree())
