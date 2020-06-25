from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.value: int = value

    def __str__(self) -> str:
        return str(self.value)


class TreeHeap:
    def __init__(self) -> None:
        self._root: Optional[Node] = None
        self._counter: int = 0

    def insert(self, value) -> None:
        new_node = Node(value)
        self._counter += 1
        if self._root is None:
            self._root = new_node
            return

        current_node = self._root
        insert_path = bin(self._counter)[3:]
        for way in insert_path[:-1]:
            current_node = current_node.right if int(way) else current_node.left

        if int(insert_path[-1]):
            current_node.right = new_node
        else:
            current_node.left = new_node
        self._trickle_up(insert_path)

    def remove(self) -> Optional[int]:
        if self._counter > 1:
            result = self._root.value

            current_node = self._root
            insert_path = bin(self._counter)[3:]
            for way in insert_path[:-1]:
                current_node = current_node.right if int(way) else current_node.left
            if int(insert_path[-1]):
                self._root.value = current_node.right.value
                current_node.right = None
            else:
                self._root.value = current_node.left.value
                current_node.left = None
            self._counter -= 1
            self._trickle_down()
            return result
        elif self._counter == 1:
            result = self._root.value
            self._root = None
            self._counter -= 1
            return result
        else:
            return None

    def change(self, old_value, new_value) -> bool:
        pass

    def _trickle_up(self, path: str) -> None:
        current = self._root
        path_nodes = [current]
        for way in path:
            if int(way):
                current = current.right
            else:
                current = current.left
            path_nodes.append(current)

        new_node_value = current.value
        path_nodes.reverse()
        for parent_node in path_nodes:
            if new_node_value > parent_node.value:
                current.value = parent_node.value
                current = parent_node

        current.value = new_node_value

    def _trickle_down(self, path: str = '') -> None:
        current_node = self._root
        new_node_value = current_node.value
        insert_path = path
        for way in insert_path:
            current_node = current_node.right if int(way) else current_node.left

        while new_node_value <= current_node.value:
            if current_node.right is not None and current_node.left is not None:
                if current_node.right.value > current_node.left.value:
                    current_node.value = current_node.right.value
                    current_node = current_node.right
                else:
                    current_node.value = current_node.left.value
                    current_node = current_node.left
            elif current_node.left is not None and current_node.left.value > new_node_value:
                current_node.value = current_node.left.value
                current_node = current_node.left
            else:
                break

        current_node.value = new_node_value

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
    data = TreeHeap()
    for item in [70, 40, 50, 20, 60, 100, 80, 30, 10, 90]:
        data.insert(item)
    data.insert(110)
    data.display()
    data.remove()
    data.display()
    data.insert(54)
    data.display()
    data.insert(56)
    data.display()
    data.remove()
    data.display()