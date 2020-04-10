f = open('input.txt', 'r')
input = lambda: f.readline().rstrip()


class Node:
    def __init__(self, value=None):
        self.value = value
        self.after = None
        self.before = None


class DoubleLinkedList:

    def __init__(self):
        self.length = 0
        self.head = self.tail = Node(0)
        self.head.after = self.tail
        self.head.before = self.head

    def find(self, index):
        now = self.head
        for _ in range(index + 1):
            now = now.after
        return now

    def connect(self, value):
        self.length += 1
        new = Node(value)
        self.tail.after = new
        new.before = self.tail
        self.tail = new

    def insert(self, index):
        self.length += 1
        left = self.find(index-1)
        now = self.find(index)
        if not left.value:
            lval = self.head.after.value
        else:
            lval = left.value
        if not now:
            nval = self.head.after.value
        else:
            nval = now.value
        new = Node(lval + nval)
        new.after = now
        new.before = left
        left.after = new
        if now:
            now.before = new
        else:
            self.tail = new

    def print_all(self):
        string = ''
        now = self.head.after
        for _ in range(self.length):
            string += str(now.value) + ' '
            now = now.after
        print(string)

    def print_reverse(self):
        string = ''
        now = self.tail
        for _ in range(min(10, self.length)):
            string += str(now.value) + ' '
            now = now.before
        print(string)


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    l_list = DoubleLinkedList()
    for value in map(int, input().split()):
        l_list.connect(value)

    index = 0
    for _ in range(K):
        index = (index + M)
        if index > l_list.length:
            index %= l_list.length
        l_list.insert(index)

    print('#%d'%tc,end=' ')
    l_list.print_reverse()


