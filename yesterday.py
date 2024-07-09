class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()

for i in "yesterday":
    stack.push(i)

yesterday = ""

while stack.size():
    yesterday += stack.pop()

print(yesterday)


list1 = [1, 2, 3, 4, 5]

for i in list1:
    stack.push(i)

list2 = []

while stack.size():
    list2.append(stack.pop())

print(list2)
