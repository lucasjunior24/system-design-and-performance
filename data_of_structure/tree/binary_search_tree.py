from typing import Self
from pydantic import BaseModel


class Node(BaseModel):
    value: int
    right: Self | None = None
    left: Self | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value: int):
        node = Node(value=value)
        if self.root is None:
            self.root = node
            return

        if self.root.left is None:
            self.root.left = node
            return

        if self.root.right is None:
            self.root.right = node
            return

    def insertB(self, value: int):
        newNode = Node(value=value)
        # while node != None:
        node = self.getNode(self.root, newNode)
        # node = node.right

    @staticmethod
    def getNode(node: Node, newNode: Node):
        if node is None:
            node = newNode
            return node

        if node.left is None:
            node.left = newNode
            return node

        if node.right is None:
            node.right = newNode
            return node

    def lookup(self, value: int): ...


#       9
#   4       20
# 1   6   15   170
binarySearchTree = BinarySearchTree()
binarySearchTree.insert(9)
binarySearchTree.insert(4)
binarySearchTree.insert(20)
binarySearchTree.insert(1)
print(binarySearchTree.root)
