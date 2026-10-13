class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def build(pre):
    if not pre:
        return None

    root = Node(pre[0])
    i = next((i for i,x in enumerate(pre) if x > root.data),len(pre))
    root.left = build(pre[1:i])
    root.right = build(pre[i:])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

pre = [1,10,5,8,21,82,91]
inorder(build(pre))