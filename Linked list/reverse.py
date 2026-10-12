# Singly Linear linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            # Fixed the typo here: changed nexr to next
            new_node.next = self.head  
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1 and temp:
                temp = temp.next
                p += 1
            
            if temp:
                new_node.next = temp.next
                temp.next = new_node

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            nextnode = curr.next  # Fixed here: step to the next node before breaking the link
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev

    def print(self):
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(output) if output else "Empty List")


# --- Execution ---
list1 = SLL()
n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
print("Original List:")
list1.print()  # Output: 10 -> 20 -> 30 -> 40

print("\nAfter Inserting 34 at Position 1:")
list1.insert(Node(34), 1)
list1.print()  # Output: 34 -> 10 -> 20 -> 30 -> 40

print("\nAfter Reversing:")
list1.reverse()
list1.print()  # Output: 40 -> 30 -> 20 -> 10 -> 34
