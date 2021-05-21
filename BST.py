class BS: #initialisation class, node initialised with 12 and both childs set to null
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None



    def __repr__(self): #This method returns the string representation of the object.
        return str(self.key)

    def insert(self,data): #insertion method
        if self.key is None:
            self.key == data
            return data
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BS(data)
            return data
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BS(data)
            return data


    def delete(self, data): #deletion method
        if self.key is None:
            print("tree is empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Element not present")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Element not present")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
            return self
def inorder(root): #inorder traversal
    if root:
        inorder(root.lchild)
        print(root.key)
        inorder(root.rchild)







root = BS(12) #refering to the BS class with entry=12
list1 = [10, 20, 4, 30, 4, 1, 5, 6] #creating an array of elements to be inserted
for i in list1:
    root.insert(i) #calling the insert function

inorder(root) #calling the inorder function

print("The root is", root)
d=int(input("enter element to delete"))
root.delete(d) #calling the delete function
inorder(root)






