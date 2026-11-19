#reverse queue using stack
#stack using linked list
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node  
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("Poped element: ",temp.data)  
            self.top=self.top.next
            temp=None

    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next
    #Linear Queue
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    
    def dequeue(self):
        if self.rear==None:
            return "Queue is empty"
        temp = self.front
        dequed_data = temp.data
        self.front = temp.next
        if self.front is None:
            self.rear = None
            print("Now queuw is empty")
        temp=None
        return dequed_data
    def is_empty(self):
        return self.front is None
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def reverse_queue(q1):
        st1=stack()
        while not q1.is_empty():
            st1.push(Node(q1.dequeue()))
        st1.print()
    def reverse_stack(s1):
        q1=Queue()
        while not s1.is_empty():
            q1.enqueue(Node(s1.pop()))
        q1.print()


# Create a queue
myQueue = Queue()
myQueue.enqueue(Node(15))
myQueue.enqueue(Node(16))
myQueue.enqueue(Node(17))
myQueue.print()
reverse_queue(que)
