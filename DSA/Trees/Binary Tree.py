class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        self.add_node_recursively(data, self.root)

    def add_node_recursively(self, data, node):
        if not node.left:
            node.left = TreeNode(data)
        elif not node.right:
            node.right = TreeNode(data)
        else:
            self.add_node_recursively(data, node.left)

    def display_the_tree(self, depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth, node.data)
        if node.left:
            self.display_the_tree(depth + 1, node.left)
        if node.right:
            self.display_the_tree(depth + 1, node.right)

    def remove_nodes(self, data):
        if not self.root:
            print('binary tree is empty')
            return
        if self.root.data == data:
            self.root = None
            return
        self.recursive_remove(data, self.root)

    def recursive_remove(self, data, node):
        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return
        if node.left:
            self.recursive_remove(data, node.left)
        if node.right:
            self.recursive_remove(data, node.right)

    def search_nodes(self, data):
        node_found = self.recursive_search(data, self.root)
        return node_found != None

    def recursive_search(self, data, node):
        if not node or node.data == data:
            return node
        return self.recursive_search(data, node.left) or self.recursive_search(data, node.right)


tree = BinaryTree()
for i in range(10):
    tree.add_node(i)
tree.display_the_tree()
tree.remove_nodes(6)
tree.add_node(10)
tree.display_the_tree()
print(tree.search_nodes(2))
