from __future__ import annotations

from typing import Any, Optional, Tuple


class Node:
    def __init__(self, value: int, data: Any = None, left: Node = None, right: Node = None) -> None:
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.value:>4} {self.data:>4}'


class Tree:
    def __init__(self) -> None:
        self._root: Optional[Node] = None

    def find(self, key: int) -> Optional[Node]:
        current = self._root
        while current.value != key:
            if key < current.value:
                current = current.left
            elif key > current.value:
                current = current.right

            if current.value is None:
                return None
        return current

    def insert(self, value: int, data: Any = None) -> None:
        new_node = Node(value, data)
        if self._root is None:
            self._root = new_node
            return

        current = self._root
        while True:
            if new_node.value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

    def _find_for_delete(self, key: int) -> Optional[Tuple[Node, Node]]:
        current, parrent = self._root, self._root
        while current.value != key:
            if key < current.value:
                parent = current
                current = current.left
                if current is None:
                    return None
            elif key > current.value:
                parent = current
                current = current.right
                if current is None:
                    return None
        return parent, current

    def _delete_zero(self, parent: Node, current: Node) -> bool:
        if parent.left is current:
            parent.left = None
        else:
            parent.right = None
        return True

    def _delete_one(self, parent: Node, current: Node) -> bool:
        if parent.left is current:
            parent.left = current.left if current.left is not None else current.right
        else:
            parent.right = current.right if current.right is not None else current.left
        return True

    def _get_successor(self, del_node: Node) -> Node:
        successor, successor_parent, current = del_node, del_node, del_node.right
        while current is not None:
            successor_parent, successor, current = successor, current, current.left
        if successor != del_node.right:
            successor_parent.left = successor.right
            successor.right = del_node.right
        return successor

    def _delete_two(self, parent: Node, current: Node) -> bool:
        successor = self._get_successor(current)
        if parent.left is current:
            parent.left = successor
        else:
            parent.right = successor
        return True

    def delete(self, key) -> bool:
        del_node_tuple = self._find_for_delete(key)
        if del_node_tuple is None:
            return False
        parent, current = del_node_tuple

        if current.left is None and current.right is None:
            return self._delete_zero(parent, current)
        elif current.left is None or current.right is None:
            return self._delete_one(parent, current)
        else:
            return self._delete_two(parent,current)



