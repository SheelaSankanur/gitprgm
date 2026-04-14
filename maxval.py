def max_value(root):
    if root is None:
        return float('-inf')   # very small number
    return max(root.val,
               max_value(root.left),
               max_value(root.right))

print("Max value:", max_value(root))  # 5