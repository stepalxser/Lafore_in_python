from __future__ import annotations

from typing import Optional, List


class Node:
    def __init__(self):
        self.counter: int = 0
        self.parent: Optional[Node] = None
        self.child_array: List[Optional[Node]] = [None, None, None, None]
        self.data_array: List[Optional[int]] = [None, None, None]

    def __len__(self) -> int:
        return self.counter

    def __str__(self) -> str:
        result = '|'.join(f'{item:>2}' if item is not None else '  ' for item in self.data_array)
        return ''.join(('|', result, '|'))

    @property
    def if_leaf(self) -> bool:
        return True if self.child_array[0] is None else False

    @property
    def is_full(self) -> bool:
        return len(self) == 3

    def find_item(self, key: int) -> int:
        return self.data_array.index(key) if key in self.data_array else -1

    def insert_item(self, value: int) -> int:
        self.counter += 1
        self.data_array[2] = value
        self.data_array.sort(key=lambda x: (x is None, x))
        return self.data_array.index(value)

    def remove_item(self) -> int:
        result, self.data_array[self.counter-1] = self.data_array[self.counter-1], None
        self.counter -= 1
        return result

    def connect_child(self, child_index: int, child: Node) -> None:
        self.child_array[child_index] = child
        if child is not None:
            child.parent = self

    def disconnect_child(self, child_index: int) -> Node:
        result, self.child_array[child_index] = self.child_array[child_index], None
        return result

    def get_child(self, child_index: int) -> Node:
        return self.child_array[child_index]


class Tree234:
    def __init__(self) -> None:
        self._root = Node()

    def find(self, key: int) -> int:
        current_node = self._root
        while True:
            result = current_node.find_item(key)
            if result != -1:
                return result
            elif current_node.if_leaf:
                return -1
            else:
                current_node = self.get_next_child(current_node, key)

    def insert(self, value) -> None:
        current_node = self._root
        while True:
            if current_node.is_full:
                self.split(current_node)
                current_node = current_node.parent
            elif current_node.if_leaf:
                break
            else:
                current_node = self.get_next_child(current_node, value)
        current_node.insert_item(value)

    def get_next_child(self, current_node, value) -> Node:
        for index in range(len(current_node)):
            if value < current_node.data_array[index]:
                return current_node.child_array[index]
        return current_node.child_array[len(current_node)]

    def split(self, current_node):
        item_c = current_node.remove_item()
        item_b = current_node.remove_item()
        child_2 = current_node.disconnect_child(2)
        child_3 = current_node.disconnect_child(3)
        new_right_node = Node()

        if current_node is self._root:
            root = Node()
            parent = root
            root.connect_child(0, current_node)
        else:
            parent = current_node.parent
        parent_index = parent.insert_item(item_b)

        for index in range(len(parent), parent_index-1, -1):
            parent.connect_child(index, parent.disconnect_child(index-1))
        parent.connect_child(parent_index, new_right_node)

        new_right_node.insert_item(item_c)
        new_right_node.connect_child(0, child_2)
        new_right_node.connect_child(1, child_3)

    def display(self) -> None:
        global_stack, blanks, is_row_empty = [self._root], 48, False
        print(48 * '*')

        while not is_row_empty:
            local_stack = []
            for elem in global_stack:
                is_row_empty = elem.if_leaf
                for data in elem.child_array:
                    if data is not None:
                        local_stack.append(data)
                print(f'{str(elem):^{blanks}}', end='')
            blanks //= 2
            global_stack = local_stack
            print()
        print(48 * '*')


if __name__ == '__main__':
   tree = Tree234()
   tree.insert(70)
   tree.insert(50)
   tree.display()
   tree.insert(30)
   tree.display()
   tree.insert(40)
   tree.display()
