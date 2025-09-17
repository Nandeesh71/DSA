
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
    
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        result = self.front.data
        self.front = self.front.next
        if self.front is None:
         
            self.rear = None
        return result


    def isEmpty(self):
        return self.front is None


    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()           

    print("Dequeued:", q.dequeue())  
    q.display()           
    print("Is Empty?", q.isEmpty()) 
