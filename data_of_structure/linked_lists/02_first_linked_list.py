from typing import Self


class Node:
    def __init__(self, value: int):
        self.value = value
        self._next: Node | None = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value: Self | None):
        self._next = value

    def __str__(self):
        return str({"value": self.value, "next": self.next})


class LinkedList:
    def __init__(self, value: int):
        node = Node(value)
        self.head: Node = node
        self.tail: Node = self.head
        self.length = 1

    def append(self, value: int):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def preppend(self, value: int):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def printList(self):
        lists = []
        currentNode = self.head
        while currentNode != None:
            lists.append(currentNode.value)
            currentNode = currentNode.next
        print(lists)

    def getByValue(self, value: int):
        currentNode = self.head
        while currentNode != None:
            if currentNode.value == value:
                break
            currentNode = currentNode.next

    def getByIndex(self, index: int):
        countIndex = 0
        currentNode = self.head
        while currentNode != None:
            if countIndex == index:
                break
            currentNode = currentNode.next
            countIndex += 1
        return currentNode

    def insert(self, index: int, value: int):
        if index >= self.length:
            self.append(value)
            return

        if index == 0:
            self.preppend(value)
            return

        newNode = Node(value)
        leaderWithPassNode = self.getByIndex(index - 1)

        newNode.next = leaderWithPassNode.next
        leaderWithPassNode.next = newNode

        self.length += 1


myLinkedList = LinkedList(value=10)
print("tail: ", myLinkedList.tail)
myLinkedList.append(18)
myLinkedList.append(1)
myLinkedList.append(16)
myLinkedList.preppend(17)
print()
print(myLinkedList.head)
print(myLinkedList.tail)
print(myLinkedList.length)
myLinkedList.printList()
myLinkedList.getByValue(16)
print()
print(myLinkedList.getByIndex(1))
# print(myLinkedList.getByIndex(3))
myLinkedList.insert(200, 4)
myLinkedList.printList()
myLinkedList.insert(2, 100)
print(myLinkedList.length)
myLinkedList.printList()
