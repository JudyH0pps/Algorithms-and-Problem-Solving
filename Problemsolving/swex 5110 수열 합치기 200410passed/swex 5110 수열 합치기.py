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
        self.head = self.tail = Node(float('inf'))
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

    def merge(self, new_list):
        new_top = new_list.head.after
        if self.length == 0:
            self.head.after = new_top
            new_top.before = self.head
            self.tail = new_list.tail
            self.length += new_list.length
            return
        for i in range(self.length):
            now = self.find(i)
            if now.value > new_top.value:
                left = self.find(i - 1)
                new_top.before = left
                now.before = new_list.tail
                new_list.tail.after = now
                left.after = new_top
                break
        else:
            new_top.before = self.tail
            self.tail.after = new_top
            self.tail = new_list.tail
        self.length += new_list.length

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
    N, M = map(int, input().split())
    l_list = DoubleLinkedList()
    for _ in range(M):
        new_list = DoubleLinkedList()
        for node in map(int, input().split()):
            new_list.connect(node)
        l_list.merge(new_list)

    print('#%d' % tc, end=' ')
    l_list.print_reverse()
