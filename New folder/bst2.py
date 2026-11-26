#o/p -
#level 1 - 100
#level 2 - 10, 450
#level 3 - 4,300,500
#level 4 - 2 7

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_levels(root):
    if root is None:
        return

    queue = [root]
    level = 1

    while queue:
        size = len(queue)

        print("Level", level, "-", end=" ")

        for i in range(size):
            temp = queue.pop(0)

            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        print()
        level += 1


# Creating Binary Tree
root = Node(100)

root.left = Node(10)
root.right = Node(450)

root.left.left = Node(4)
root.left.right = Node(300)
root.right.right = Node(500)

root.left.left.left = Node(2)
root.left.left.right = Node(7)

# Printing levels
print_levels(root)
