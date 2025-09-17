class StackUnderflowError(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.isEmpty():
            raise StackUnderflowError("Stack underflow: Cannot pop from an empty stack.")
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        if self.isEmpty():
            raise StackUnderflowError("Stack underflow: Cannot peek into an empty stack.")
        print(f"Top item is {self.stack[-1]}")
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):", self.stack[::-1])


if __name__ == "__main__":
    s = Stack()
    try:
        s.pop()  
    except StackUnderflowError as e:
        print(e)

    s.push(10)
    s.push(20)
    s.push(30)

    s.display()
    s.peek()
    s.pop()
    s.display()

    while not s.isEmpty():
        s.pop()

    try:
        s.peek()  
    except StackUnderflowError as e:
        print(e)
