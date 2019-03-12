class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = None

    # Traverse and Print Linkedlist
    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.item, end='->')
            ptr = ptr.next
        print()

    def insertNode(self, position, item):
        if position == 0:
            newNode = Node(item)
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            ptr = self.head
            while ptr and position > 1:
                position -= 1
                ptr = ptr.next
            if not ptr:
                print('invalid insertion')
                return
            newNode = Node(item)
            prev = ptr
            next = ptr.next
            prev.next = newNode
            newNode.next = next
            return

    def removeNode(self, key):
        prev = cur = self.head
        while cur:
            if cur.item == key:
                break
            if cur != self.head:
                prev = prev.next
            cur = cur.next
        if not cur:
            print('invalid deletion')
            return
        if cur == prev:
            self.head = cur.next
            return
        prev.next = cur.next
        return



list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2
e2.next = e3


print('after insertion')
list.insertNode(4, 'test')
list.printList()

print('after deletion')
list.removeNode('test')
list.printList()