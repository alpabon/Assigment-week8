class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []
        
    def print_heap(self):
        print("\nCurrent Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")
    
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            current_patient = self.data[index]
            parent_patient = self.data[parent_index]

            if current_patient.urgency < parent_patient.urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break
            
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        
        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value
            
    def peek(self):
        if not self.data:
            return None
        return self.data[0]
    
        
# Test your MinHeap class here including edge cases

heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)  
served = heap.remove_min()
print(served.name)  
heap.print_heap()

#Why is a tree appropriate for the doctor structure?
#a tree is appropiate for the doctor structure because it allows for hierarchical representation of relationships, this means each doctor can have direct reports just like a parent node can have child nodes. This structure makes it easier and faster the managemnet of the traversal of the team, making it easier to locate specific doctors and understand reporting lines.
#When might a software engineer use preorder, inorder, or postorder traversals?
#A software engineer might use preorder, inorder, or postorder traversals in various scenarios such as: Preorder traversal, it can be used to copy, export or display the hierarchy from top to bottom. Inorder traversal, is used to take data in a sorted order, especially in binary research. Postorder traversal is useful when you need to delete a tree or when you need to evaluate expressions in expression trees.
#How do heaps help simulate real-time systems like emergency intake?
#Heaps help to simulate real time systems like emergency intake by providing an efficient way to manage and prioritize tasks based on urgency. In a min-heap, the highest priority has the lowest value , and this can be accessed in constant timeor the lowest urgency value patient can be accessed in constant time. THis can help to make desicion based on the most urgent cases.
