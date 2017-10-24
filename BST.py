class node:
    def __init__(self, data, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root.data)

    def addI(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            p = self.root
            while True:
                if data < p.data:
                    if p.left is None:
                        p.left = node(data)
                        break
                    else:
                        p = p.left
                else:
                    if p.right is None:
                        p.right = node(data)
                        break
                    else:
                        p = p.right

    def add(self, data):
        self.root = BST._add(self.root, data)

    def _add(root, data):
        if root is not None:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        else:
            return node(data)
        return root

    def inOrder(self):
        print('InOrder: ', end='')
        BST._inOrder(self.root)
        print()

    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def preOrder(self):
        print('PreOrder: ', end='')
        BST._preOrder(self.root)
        print()

    def _preOrder(root):
        if root is not None:
            print(root.data, end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        print('PostOrder: ', end='')
        BST._postOrder(self.root)
        print()

    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=' ')

    def printSideWay(self):
        BST._printSideWay(self.root, 0)

    def _printSideWay(root, lvl):
        if root is not None:
            BST._printSideWay(root.right, lvl + 1)
            print(lvl * '   ', root.data)
            BST._printSideWay(root.left, lvl + 1)

    def search(self, data):
        p = self.root
        while True:
            if p is None:
                return None
            else:
                if data == p.data:
                    return p
                elif data < p.data:
                    p = p.left
                else:
                    p = p.right

    def path(self, data):
        if self.root is None:
            print('There is no Root!')
        else:
            p = self.root
            path = ''
            while True:
                if p is None:
                    print('No Data')
                    break
                elif data == p.data:
                    path = path + str(p.data)
                    print('Path of', data, ':', path)
                    break
                elif data < p.data:
                    path = path + str(p.data) + ' -(Left)-> '
                    p = p.left
                else:
                    path = path + str(p.data) + ' -(Right)-> '
                    p = p.right

    def deL(self, data):
        # p = node , f = parent , suc = successor , p_suc = successor's parent
        if self.root is None:
            print('There is no Root!')
        else:
            p = self.root
            while True:
                if p is None:
                    print('No Data')
                    break
                elif data == p.data:
                    if p.left is None and p.right is None:
                        if p.data < f.data:
                            f.left = None
                        else:
                            f.right = None
                    elif p.left is None and p.right is not None:
                        if p.data < f.data:
                            f.left = p.right
                        else:
                            f.right = p.right
                    elif p.left is not None and p.right is None:
                        if p.data < f.data:
                            f.left = p.left
                        else:
                            f.right = p.left
                    else:
                        # Case : p have Left and Right Subtree
                        print('Todo')
                    break
                elif data < p.data:
                    f = p
                    p = p.left
                else:
                    f = p
                    p = p.right


l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
r = BST()
for data in l:
    r.add(data)

r.printSideWay()
r.inOrder()
r.preOrder()
r.postOrder()
print(20 * '--')
r.addI(8)
r.inOrder()
r.add(10)
r.inOrder()
r.printSideWay()
print('Search 8 :', r.search(8))
print('Search 2 :', r.search(2))
r.path(8)
