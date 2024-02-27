class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
        self.length+=1
   
    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node
        self.length-=1

    def get_length(self):
        return self.length

    def is_empty(self):
        return (self.length==0)

    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=' ')
            node = node.next
        print()

    def print_reverse_list(self):
        node = self.tail    #O(1)
        if self.is_empty(): #O(1)
            print()
            return
        else:
            print(node.data, end=' ')
            while node != self.head:                # O(N^2)
                prevnode = self.head
                while prevnode.next != node:        
                    prevnode = prevnode.next
                node = prevnode
                print(node.data, end=' ')
        print()