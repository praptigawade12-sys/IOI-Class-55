class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def newNode(item):
    temp = Node(item)
    temp.key = item
    temp.left = temp.right = None
    return temp

def insert(root,key):
    if root is None:
        return newNode(key)

    if key > root.key:
        root.right = insert(root.right, key)
    if key < root.key:
        root.left = insert(root.left, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

root = None
root = insert(root,50)
insert(root,30)
insert(root,40)
insert(root,10)
insert(root,70)
insert(root,20)
insert(root,60)

inorder(root)