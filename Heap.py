import heapq


class Heap:
    '''
    implementation of min-heap (zero indexed)
    '''

    def __init__(self, list):
        self.length = 0
        self.last_index = -1
        self.heap = []
        for i in list:
            self.insert(i)

    def insert(self, item):
        self.heap.append(item)
        self.length += 1
        self.last_index += 1
        self.swim()

    def delMin(self):
        self.heap[0], self.heap[self.last_index] = self.heap[self.last_index], self.heap[0]
        rst = self.heap.pop()
        self.length -= 1
        self.last_index -= 1
        self.sink(0)
        return rst

    def swim(self):
        current = self.last_index
        parent = self.__getParent(current)
        if parent == None:
            return
        while parent != None and parent >= 0 and self.heap[parent] > self.heap[current]:
            print('{}  {}'.format(current, parent))
            self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
            current = parent
            parent = self.__getParent(current)

    def sink(self, index):
        while 2 * (index + 1) <= self.last_index:
            if self.heap[2 * index + 1] > self.heap[2 * index + 2]:
                smaller_child = 2 * index + 2
            else:
                smaller_child = 2 * index + 1
            if self.heap[index] < self.heap[smaller_child]:
                break
            self.heap[smaller_child], self.heap[index] = self.heap[index], self.heap[smaller_child]
            index = smaller_child
        return

    def __getParent(self, index):
        if index == 0:
            return None

        return (index - 1) // 2

    def __str__(self):
        return str(self.heap)


l = [5, 4, 3, 2, 1]
h = Heap(l)
print(h)
print(h.delMin())
print(h)
print(h.delMin())
print(h)
print(h.delMin())
print(h)
