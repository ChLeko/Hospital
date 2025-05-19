class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RegularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        temp = self.front
        if temp is None:
            print("Regular Queue is empty!")
        else:
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None or self.front.data < data:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next and temp.next.data >= data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        if self.front is None:
            print("Priority Queue is empty!")
            return
        temp = self.front
        self.front = self.front.next
        return temp.data

    def display(self):
        temp = self.front
        if temp is None:
            print("Priority Queue is empty!")
        else:
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

# Create both queues
regular_queue = RegularQueue()
priority_queue = PriorityQueue()

# Enqueue test data
regular_queue.enqueue("Patient A")
regular_queue.enqueue("Patient B")
regular_queue.enqueue("Patient C")

priority_queue.enqueue("Emergency X")
priority_queue.enqueue("Emergency Y")
priority_queue.enqueue("Emergency Z")

# Display both queues
print("Regular Queue:")
regular_queue.display()

print("\nPriority Queue:")
priority_queue.display()

# Combine both queues (first priority patients, then regular patients)
combined_queue = RegularQueue()  # Using regular queue for simplicity
while priority_queue.front:
    combined_queue.enqueue(priority_queue.dequeue())
while regular_queue.front:
    combined_queue.enqueue(regular_queue.dequeue())

print("\nCombined Queue (Emergency Patients First):")
combined_queue.display()
