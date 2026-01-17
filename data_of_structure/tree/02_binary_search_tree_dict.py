from typing import Self
from dataclasses import dataclass, asdict


@dataclass
class Node:
    value: int | None = None
    left: Self | None = None
    right: Self | None = None

    def __init__(self, value: int):
        self.value = value


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def insert(self, value: int):
        newNode = Node(value=value)
        if self.root is None:
            self.root = newNode
            return None
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    currentNode = currentNode.right

    def lookup(self, value: int):
        currentNode = self.root
        while currentNode:
            if value <= currentNode.value:
                if currentNode.value == value:
                    return currentNode
                currentNode = currentNode.left
            else:
                if currentNode.value == value:
                    return currentNode
                currentNode = currentNode.right

    def showAll(self):
        binary = asdict(self)
        print(binary)


#       9
#   4       20
# 1   6   15   170

binarySearchTree = BinarySearchTree()
binarySearchTree.insert(9)
binarySearchTree.insert(4)
binarySearchTree.insert(20)
binarySearchTree.insert(1)
binarySearchTree.insert(6)
binarySearchTree.insert(15)

print(binarySearchTree.showAll())
print()
print(binarySearchTree.lookup(20))
print(binarySearchTree.lookup(4))
print(binarySearchTree.lookup(200))
print(binarySearchTree.lookup(6))
print(binarySearchTree.lookup(15))
print(binarySearchTree.lookup(9))
