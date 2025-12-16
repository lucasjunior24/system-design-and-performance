from typing import Any


class LinkedList:
    def __init__(self, value: int):
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value: int):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def preppend(self, value: int):
        new_node = {"value": value, "next": self.head}
        self.head = new_node
        self.length += 1

    def printList(self):
        lists = []
        currentNode = self.head
        while currentNode != None:
            lists.append(currentNode["value"])
            currentNode = currentNode["next"]
        print(lists)

    def getByValue(self, value: int):
        currentNode = self.head
        while currentNode != None:
            if currentNode["value"] == value:
                break
            currentNode = currentNode["next"]

    def getByIndex(self, index: int):
        countIndex = 0
        currentNode = self.head
        while currentNode != None:
            if countIndex == index:
                break
            currentNode = currentNode["next"]
            countIndex += 1
        return currentNode

    def insert(self, index: int, value: int):
        if index > self.length:
            raise Exception("index é maior que o total de itens na lista")
        print(
            "Before: 1 -> 10 -> 20 -> 2",
            "    Insert index '2' and value '5'   After: 1 -> 10 -> 5 -> 20 -> 2",
        )
        newNode = self.getByIndex(index - 1)
        newNodeEnd = {"value": value, "next": newNode["next"]}
        currentNode = self.head
        while currentNode != None:
            currentNode = currentNode["next"]
            if currentNode["value"] == newNode["value"]:
                currentNode["next"] = newNodeEnd
                break
        print(self.head)
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
myLinkedList.getByValue(1)
print()
print(myLinkedList.getByIndex(1))
# print(myLinkedList.getByIndex(3))
myLinkedList.insert(2, 5)
