class BinaryTree:
    def __init__(self,Rootobj):
        self.key = Rootobj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def breadthorder(self):
        q = list()
        q.append(self)
        while q:
            node = q.pop(0)
            print(node.key)
            if node.leftChild:
                q.append(node.leftChild)
            if node.rightChild:
                q.append(node.rightChild)
    

t = BinaryTree('A')
t.insertLeft('B')
t.insertRight('C')
t.getLeftChild().insertLeft('D')
t.getLeftChild().insertRight('E')
t.getLeftChild().getRightChild().insertLeft('H')
t.getRightChild().insertLeft('F')
t.getRightChild().insertRight('G')
t.getRightChild().getRightChild().insertLeft('I')
t.getRightChild().getRightChild().insertRight('J')
t.inorder()