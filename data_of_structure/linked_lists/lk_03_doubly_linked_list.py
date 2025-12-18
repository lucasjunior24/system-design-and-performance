class DoublyNode:
    def __init__(self, value: int):
        self.value = value
        self.next: DoublyNode | None = None
        self.previous: DoublyNode | None = None


class DoublyLinkedList:
    def __init__(self, value: int):
        node = DoublyNode(value)
        self.head: DoublyNode = node
        self.tail: DoublyNode = self.head
        self.length = 1

    def append(self, value: int):
        node = DoublyNode(value)
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        self.length += 1

    def preppend(self, value: int):
        node = DoublyNode(value)
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

    def printListPrevious(self):
        lists = []
        currentNode = self.tail

        while currentNode != None:
            lists.append(currentNode.value)
            currentNode = currentNode.previous

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

        newNode = DoublyNode(value)
        leaderWithPassNode = self.getByIndex(index - 1)
        newNode.next = leaderWithPassNode.next

        leaderWithPassNode.next = newNode

        self.length += 1

    def remove(self, index: int):
        if index == 0:
            firstNode = self.head
            self.head = firstNode.next
            self.length -= 1
            return
        leaderWithPassNode = self.getByIndex(index - 1)
        if leaderWithPassNode.next == None:
            print("Este index não existe")
            return
        else:
            removedNode = leaderWithPassNode.next
            if removedNode.next == None:
                self.tail = leaderWithPassNode
            leaderWithPassNode.next = removedNode.next
            self.length -= 1


myLinkedList = DoublyLinkedList(value=10)

myLinkedList.append(18)
myLinkedList.append(1)
myLinkedList.append(16)
myLinkedList.preppend(17)
print()

myLinkedList.printList()
print(myLinkedList.getByIndex(1).value)
# print(myLinkedList.getByIndex(3))
myLinkedList.insert(200, 4)
myLinkedList.printList()
myLinkedList.insert(2, 100)
print(myLinkedList.length)
myLinkedList.printList()
print()
myLinkedList.remove(0)
myLinkedList.printList()
print("Previous")
myLinkedList.printListPrevious()
