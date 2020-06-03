from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, left: Node = None, right: Node = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)


# programming project 8.1
class TreeString:
    def __init__(self) -> None:
        self._root: Optional[Node] = None

    def insert_string(self, data: str) -> None:
        array = [Node(char) for char in data]
        self._root = Node(value='+', right=array.pop())
        current = self._root
        while len(array) > 1:
            current.left = Node(value='+', right=array.pop())
            current = current.left
        current.left = array.pop()

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


# 8.2 programming project
class TreeBalanceString:
    def __init__(self) -> None:
        self._root: Optional[Node] = None

    def insert_string(self, data: str) -> None:
        array = [Node(char) for char in data]
        length = len(array)
        self._root = Node('+')
        global_stack, local_stack = [self._root], []
        level_counter = 2
        while length > level_counter:
            while len(global_stack) != 0:
                temp = global_stack.pop()
                temp.left, temp.right = Node('+'), Node('+')
                local_stack.extend((temp.left, temp.right))
            while len(local_stack) != 0:
                global_stack.append(local_stack.pop())
            level_counter *= 2

        iter_data = iter(array)
        for elem in reversed(global_stack):
            try:
                elem.left = next(iter_data)
                elem.right = next(iter_data)
            except StopIteration:
                break

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
        global_stack, blanks, is_row_empty = [self._root], 64, False
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


# 8.3 programming project
class TreeFullString:
    def __init__(self) -> None:
        self._root: Optional[Node] = None

    def insert_string(self, data: str) -> None:
        array = [Node(char) for char in data[::-1]]
        self._root = array.pop()
        global_stack, local_stack =[self._root], []
        while len(array) != 0:
            while len(global_stack) != 0:
                elem = global_stack.pop()
                if len(array) >= 2:
                    elem.left = array.pop()
                    elem.right = array.pop()
                    local_stack.extend((elem.left, elem.right))
                elif len(array) == 1:
                    elem.left = array.pop()
                    break
            global_stack, local_stack = local_stack, global_stack
            global_stack.reverse()

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
        global_stack, blanks, is_row_empty = [self._root], 64, False
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
    print('Project 8.1')
    tree = TreeString()
    tree.insert_string('ABCDE')
    tree.display()

    print('Project 8.2')
    tree = TreeBalanceString()
    tree.insert_string('ABCDE')
    tree.display()

    print('Project 8.3')
    tree = TreeFullString()
    tree.insert_string('ABCDEFGHIJ')
    tree.display()


