class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Total nodes:", count_nodes(root))  # 5