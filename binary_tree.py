"""
                A
         /              \
        B                   C
    /       \           /       \
    D       E           F          G

Inorder traversal
print all nodes

Left-> Root -> Right

OP : D B E A F C G

TC : node is NULL


"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class CreateTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):

        if traversal_type == 'preorder':
            return self.preorder_traversal(self.root)

    def preorder_traversal(self, node):

        if node is None:
            return

        print(node.value, end=" ")
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

        return


tree = CreateTree('A')
tree.root.left = Node('B')
tree.root.right = Node('C')
tree.root.left.left = Node('D')
tree.root.left.right = Node('E')
tree.root.right.left = Node('F')
tree.root.right.right = Node('G')

print(tree.print_tree('preorder'))
