class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
print("Preorder:  ", end=""); preorder(root)    # 1 2 4 5 3
print("\nInorder:   ", end=""); inorder(root)   # 4 2 5 1 3
print("\nPostorder: ", end=""); postorder(root) # 4 5 2 3 1