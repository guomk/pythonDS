class TreeNode():
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def __str__(self):
        return str(self.item)

# DF Traversal
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.item, end=' ')
    inorder(root.right)

def preorder(root):
    if not root:
        return

    print(root.item, end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.item, end=' ')

# BF Traversal
def dfs(root):
    q = []
    q.append(root)
    while q:
        temp = q.pop(0)
        print(temp.item, end=' ')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

# Insertion: insert at the first avaliable location
def insert(root, item):
    q = []
    q.append(root)
    while q:
        temp = q.pop(0)
        if not temp.left:
            temp.left = TreeNode(item)
            return
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = TreeNode(item)
            return
        else:
            q.append(temp.right)
    return

# Deletion: delete the node and replace with the last element in the tree
def delete(root, key):
    parent = None
    def deleteDeepest(root, keyPtr):
        q = []
        q.append(root)

        while q:
            temp = q.pop()
            if temp.left:
                if temp.left == keyPtr:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)
            if temp.right:
                if temp.right == keyPtr:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            parent = temp

    q = []
    q.append(root)
    target = None
    parent = None
    while q:
        temp = q.pop(0)
        if temp.item == key:
            target = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    target.item = temp.item
    deleteDeepest(root, temp)
    return root









n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

root = n1
print('preorder: ')
preorder(root)
print()
print('inorder: ')
inorder(root)
print()
print('postorder: ')
postorder(root)
print()
print('dfs')
dfs(root)
print()

# Insertion Test
print('Insertion Test')
insert(root, 6)
insert(root, 7)
print('dfs')
dfs(root)

# Deletion Test
print()
print('Deletion Test')
root = delete(root, 7)
print('dfs')
dfs(root)



