#BST using Linked List- Insert, Delete, Inorder, Preorder, Postorder, Count, Findminmax, Search
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    cnt=0
    def __init__(self):
        self.root=None
        
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def del_node(self, rt, val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left, val)
        elif val>rt.data:
            rt.right=self.del_node(rt.right, val)
        else:
            if rt.left is None: #Node with right child only
                return rt.right
            if rt.right is None: #Node with left child only
                return rt.left
            #Node has both left and right children
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.del_node(rt.right, succ.data)
        return rt
    def get_successor(self, temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp
    
    def inorder(self, rt):
        if rt is None:
            return 
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)
    def count(self, rt):
        if rt is None:
            return 
        else:
            self.count(rt.left)
            self.cnt+=1
            self.count(rt.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def search(self, key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def find_minmax(self, rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\nMin value: ", temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\nMax value: ", temp.data)


b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(70))
b1.insert(Node(2))
b1.insert(Node(2000))
print("\nInorder: ")
b1.inorder(b1.root)
b1.inorder(b1.root)
# print("\nPreorder: ")
# b1.preorder(b1.root)
# print("\nPostorder: ")
# b1.postorder(b1.root)
# b1.find_minmax(b1.root)
# b1.del_node(b1.root,10)
# print("\n After Deletion: ", end=" ")
# b1.inorder(b1.root)
b1.count(b1.root.left)
print("\nTotal no of nodes in left subtree: ", b1.cnt)
if b1.search(90):
    print("\nFound the node")
else:
    print("\nNot found")



