# Python Program to flatten list with 
# next and child pointers

class Node:
    def __init__(self, new_value):
        self.data = new_value
        self.next = None
        self.child = None

# function that flattens 
# a multilevel linked list
def flatten_list(head):

    # Base case
    if head is None:
        return

    # Find tail node of first level
    tail = head
    while tail.next is not None:
        tail = tail.next

    # traverse through all nodes of first level 
    curr = head

    while curr != None:

        # If current node has a child
        if curr.child is not None:

            # then append the child at the end of current list
            tail.next = curr.child

            # and update the tail to new last node
            tmp = curr.child
            while tmp.next is not None:
                tmp = tmp.next
            tail = tmp

            # Remove link between curr and child node
            curr.child = None

        # Change current node
        curr = curr.next

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
  	#Linked List - 
  	# 1 -> 2 -> 3
	# |    |   
	# 4 -> 5   6
	# |
	# 7
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.child = Node(4)
    head.child.next = Node(5)
    head.next.next.child = Node(6)
    head.child.child = Node(7)

    flatten_list(head)
    print_list(head)