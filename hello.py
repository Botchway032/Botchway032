if root is None:
        return root
    if value < root.value:
        root.left = deleteNode(root.left, value)
    else if value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        // Node with only one child or no child
        if root.left is None:
            return root.right
        else if root.right is None:
            return root.left
        // Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    return root
function minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
return current

Question  3
Python Program to Insert and Delete a Node in a Constructed Tree
 Python implementation of a tree with insert and delete:
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
return node.left
             Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right) if node else []

 Example;
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print("Inorder traversal before deletion:", bst.inorder())
    bst.delete(20)
    print("Inorder traversal after deleting 20:", bst.inorder())
    bst.delete(30)
    print("Inorder traversal after deleting 30:", bst.inorder())
    bst.delete(50)
    print("Inorder traversal after deleting 50:", bst.inorder())


