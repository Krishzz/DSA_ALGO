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

    def display_all_nodes(self):
        self.find_all_nodes(self.root)

    def find_all_nodes(self, node):
        print(node.data, end=", ")
        for child in node.children:
            parentNode = self.find_all_nodes(child)


tree = Tree()
tree.add(2)

tree.add(5, 2)
tree.add(3, 2)
tree.add(4, 2)
tree.add(6, 5)
tree.add(5, 7)
tree.display_all_nodes()
