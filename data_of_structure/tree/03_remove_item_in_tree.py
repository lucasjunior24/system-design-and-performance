from typing import Self
from pydantic import BaseModel


class Node(BaseModel):
    value: int
    left: Self | None = None
    right: Self | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

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
            if value < currentNode.value:
                currentNode = currentNode.left
            elif currentNode.value == value:
                return currentNode
            else:
                currentNode = currentNode.right

    def remove(self, value: int):
        if self.root is None:
            return False
        else:
            currentNode = self.root
            parentNode = None
            while currentNode:
                if value < currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                elif currentNode.value == value:
                    if currentNode.right is None:
                        if parentNode is None:
                            self.root = currentNode.left
                        else:
                            self.validate_parent(
                                currentNode, parentNode, currentNode.left
                            )

                    elif currentNode.right.left is None:
                        if parentNode is None:
                            self.root = currentNode.left
                        else:
                            currentNode.right.left = currentNode.left
                            self.validate_parent(
                                currentNode, parentNode, currentNode.right
                            )
                    else:
                        leftmost: Node = currentNode.right.left
                        leftmostParent: Node = currentNode.right
                        while leftmost.left is not None:
                            leftmostParent = leftmost
                            leftmost = leftmost.left

                        leftmostParent.left = leftmost.right
                        leftmost.left = currentNode.left
                        leftmost.right = currentNode.right

                        if parentNode is None:
                            self.root = leftmost
                        else:
                            self.validate_parent(currentNode, parentNode, leftmost)

                    return True

    @staticmethod
    def validate_parent(currentNode: Node, parentNode: Node, new_value: Node):
        if currentNode.value < parentNode.value:
            parentNode.left = new_value
        elif currentNode.value > parentNode.value:
            parentNode.right = new_value


#       9
#   4       20
# 1   6   15   170
binarySearchTree = BinarySearchTree()
binarySearchTree.insert(9)
binarySearchTree.insert(4)
binarySearchTree.insert(6)
binarySearchTree.insert(20)
binarySearchTree.insert(170)
binarySearchTree.insert(15)
binarySearchTree.insert(1)
print(binarySearchTree.root)
print()
print(binarySearchTree.remove(0))
print(binarySearchTree.remove(170))
# print(binarySearchTree.remove(4))
print(binarySearchTree.root)
