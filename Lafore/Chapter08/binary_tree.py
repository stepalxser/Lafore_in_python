from __future__ import annotations

from typing import Any, Optional, Tuple


class Node:
    def __init__(self, value: int, data: Any = None, left: Node = None, right: Node = None) -> None:
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)


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
            return self._delete_two(parent, current)

    def _pre_order(self, local_root: Node) -> None:
        if local_root is not None:
            print(local_root.value, end=' ')
            self._pre_order(local_root.left)
            self._pre_order(local_root.right)

    def _in_order(self, local_root: Node) -> None:
        if local_root is not None:
            self._in_order(local_root.left)
            print(local_root.value, end=' ')
            self._in_order(local_root.right)

    def _post_order(self, local_root: Node) -> None:
        if local_root is not None:
            self._post_order(local_root.left)
            self._post_order(local_root.right)
            print(local_root.value, end=' ')

    def traverse(self, type: str) -> None:
        commands = {'pre': self._pre_order, 'in': self._in_order, 'post': self._post_order}
        commands[type](self._root)
        print()

    def display(self) -> None:
        global_stack,  blanks, is_row_empty = [self._root], 64, False
        print(64 * '*')

        while not is_row_empty:
            local_stack, is_row_empty = [], True
            while len(global_stack) != 0:
                temp = global_stack.pop()
                if temp is not None:
                    print(f'{temp.value:^{blanks}}', end='')
                    local_stack.extend((temp.left, temp.right))
                    is_row_empty = False if temp.left is not None or temp.right is not None else is_row_empty
                else:
                    print(f'{"--":^{blanks}}', end='')
                    local_stack.extend((None, None))
            print()
            blanks //= 2
            while len(local_stack) != 0:
                global_stack.append(local_stack.pop())
        print(64 * '*')


if __name__ == '__main__':
    tree = Tree()
    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(12)
    tree.insert(37)
    tree.insert(43)
    tree.insert(30)
    tree.insert(33)
    tree.insert(87)
    tree.insert(93)
    tree.insert(97)
    tree.traverse('in')
    tree.traverse('pre')
    tree.traverse('post')
    tree.display()
    tree.delete(33)
    tree.display()
    tree.delete(93)
    tree.display()
    tree.delete(25)
    tree.display()
