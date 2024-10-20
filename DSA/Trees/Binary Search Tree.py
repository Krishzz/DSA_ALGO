class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = BSTNode(data)
        self.add_node_recursively(data, self.root)

    def add_node_recursively(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.add_node_recursively(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.add_node_recursively(data, node.right)

    def display_nodes(self):
        result = []
        self.inorder_transversal(self.root, result)
        print(result)
        result = []
        self.preorder_transversal(self.root, result)
        print(result)
        result = []
        self.postorder_transversal(self.root, result)
        print(result)

    def inorder_transversal(self, node, result):
        if not node:
            return
        self.inorder_transversal(node.left, result)
        result.append(node.data)
        self.inorder_transversal(node.right, result)

    def preorder_transversal(self, node, result):
        if not node:
            return
        result.append(node.data)
        self.inorder_transversal(node.left, result)
        self.inorder_transversal(node.right, result)

    def postorder_transversal(self, node, result):
        if not node:
            return
        self.inorder_transversal(node.left, result)
        self.inorder_transversal(node.right, result)
        result.append(node.data)


bst = BinarySearchTree()
bst.add_node(5)
bst.add_node(3)
bst.add_node(6)
bst.add_node(4)
bst.add_node(1)
bst.display_nodes()
