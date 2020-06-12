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
        return ''.join(('<', result, '>'))

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
                current_node = self.get_next_child(current_node, value)
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
        new_right_node = Node()
        new_right_node.insert_item(current_node.remove_item())
        new_right_node.connect_child(0, current_node.disconnect_child(2))
        new_right_node.connect_child(1, current_node.disconnect_child(3))

        item_b = current_node.remove_item()

        if current_node is self._root:
            self._root = Node()
            parent = self._root
            self._root.connect_child(0, current_node)
        else:
            parent = current_node.parent

        parent_index = parent.insert_item(item_b)

        for child_index in range(len(parent)-1, parent_index, -1):
            temp = parent.disconnect_child(child_index)
            parent.connect_child(child_index+1, temp)

        parent.connect_child(parent_index+1, new_right_node)

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

    # programming project 10.1
    def min(self) -> int:
        current_node = self._root
        while not current_node.if_leaf:
            current_node = current_node.child_array[0]
        return current_node.data_array[0]

    # programming project 10.2
    def in_order_traverse(self, node=None):
        node = self._root if node is None else node
        for index in range(4):
            if node.child_array[index] is not None:
                self.in_order_traverse(node=node.child_array[index])
            if index != 3 and node.data_array[index] is not None:
                print(node.data_array[index], end=' ')

    # programming project 10.3
    @classmethod
    def sorted(cls, data: List) -> List:
        temp = cls()
        for item in data:
            temp.insert(item)

        def array_traverse(node=None, data=None) -> List:
            data = [] if data is None else data
            node = temp._root if node is None else node
            for index in range(4):
                if node.child_array[index] is not None:
                    array_traverse(node=node.child_array[index], data=data)
                if index != 3 and node.data_array[index] is not None:
                    data.append(node.data_array[index])
            return data
        return array_traverse(node=temp._root)


if __name__ == '__main__':
    tree = Tree234()

    for index in range(10, 100, 10):
        tree.insert(index)
        tree.display()

    print(tree.min())
    tree.in_order_traverse()
    print()

    array = [item for item in range(10, 0, -1)]
    array_2 = Tree234.sorted(array)
    print(array_2)