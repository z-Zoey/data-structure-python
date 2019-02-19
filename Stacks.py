# Stack implementation (LIFO)
class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Queue implementation (FIFO)
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Deque implementation (Add and remove items from either end)
class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# Return a boolean checking the input string of parenthesis is balanced and open and closing parenthesis is in correct order in the correct order
def parentheses_check(s):
    open_par = set('({[')
    matched_par = set([('(', ')'), ('{', '}'), ('[', ']')])
    open_stack = []

    if len(s) % 2 != 0:
        return False

    for par in s:
        if par in open_par:
            open_stack.append(par)
        else:
            if len(open_stack) == 0:
                return False
            if (open_stack.pop(), par) not in matched_par:
                return False

    return len(open_stack) == 0


# Implement a queue using two stacks
class Queue2Stacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
