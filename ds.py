
class Node:
 
    def __init__(self, data: tuple):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None	
        self.length = 0

    # Function to insert a new node at the beginning
    def push(self, new_data: Node):
        new_node = Node(new_data)
        
        if self.tail is None:
            self.tail = new_node
        
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node
        self.length += 1

    # Function to delete last node at list
    def delete_tail(self):
        if self.tail is None:
            return

        temp = self.tail
        if temp == self.head:
            self.head = None

        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        
        del temp

    def peek_at_tail(self):
        return self.tail

    # Utility function to print the linked LinkedList for debugging
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def values(self):
        temp = self.head.next
        vals = []
        while(temp):
            vals.append(temp.data)
            temp = temp.next
        return vals


