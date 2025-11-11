class LinkedList:
    def __init__(self, value: int):
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value: int):
        new_node = {"value": value, "next": None}

        self.tail["next"] = new_node
        print("head: ", self.head)
        self.tail = new_node
        self.length += 1

    def preppend(self, value: int):
        new_node = {"value": value, "next": self.head}
        self.head = new_node
        self.length += 1


myLinkedList = LinkedList(value=10)
print(myLinkedList.tail)
myLinkedList.append(2)
myLinkedList.append(16)
myLinkedList.preppend(17)
# myLinkedList.append(18)
print()
print(myLinkedList.head)
print(myLinkedList.tail)
print(myLinkedList.length)
