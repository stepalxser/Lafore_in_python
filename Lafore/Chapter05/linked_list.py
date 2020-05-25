from typing import Any, Optional


class Link:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[Link] = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.first: Optional[Link] = None

    def __str__(self) -> str:
        display_array, current = [], self.first
        while current is not None:
            display_array.append(current)
            current = current.next
        return ' '.join(str(item) for item in display_array)

    def insert_first(self, link_data: Any) -> None:
        new_link = Link(link_data)
        new_link.next = self.first
        self.first = new_link

    def delete_first(self) -> Link:
        result = self.first
        self.first = self.first.next
        return result

    def find(self, key: Any) -> Optional[Link]:
        current = self.first
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None

    def delete(self, key: Any) -> Optional[Link]:
        current = self.first
        previous = self.first
        while current is not None:
            if current.data == key:
                previous.next = current.next
                return current
            previous = current
            current = current.next
        return None

    @property
    def is_empty(self):
        return True if self.first is None else False


class TwoWayLinkedList:
    def __init__(self):
        self.first: Optional[Link] = None
        self.last: Optional[Link] = None

    def __str__(self) -> str:
        display_array, current = [], self.first
        while current is not None:
            display_array.append(current)
            current = current.next
        return ' '.join(str(item) for item in display_array)

    def insert_first(self, key) -> None:
        new_link = Link(key)
        if self.is_empty:
            self.last = new_link
        new_link.next = self.first
        self.first = new_link

    def insert_last(self, key) -> None:
        new_link = Link(key)
        if self.is_empty:
            self.first = new_link
            self.last = new_link
        self.last.next = new_link
        self.last = new_link

    def delete_first(self) -> Any:
        result = self.first
        self.last = None if self.first is None else self.last
        self.first = None if self.first is None else self.first.next
        return result

    @property
    def is_empty(self):
        return True if self.first is None else False


class SortedList:
    def __init__(self, first=None):
        self.first: Optional[Link] = first

    def __str__(self) -> str:
        display_array, current = [], self.first
        while current is not None:
            display_array.append(current)
            current = current.next
        return ' '.join(str(item) for item in display_array)

    def insert(self, link_data: Any) -> None:
        new_link = Link(link_data)
        previous = None
        current = self.first

        while current is not None and link_data > current.data:
            previous = current
            current = current.next
        if previous is None:
            self.first = new_link
        else:
            previous.next = new_link
        new_link.next = current

    def find(self, key: Any) -> Optional[Link]:
        current = self.first
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None

    def delete(self) -> Optional[Link]:
        result = self.first
        self.first = self.first.next
        return result

    @property
    def is_empty(self):
        return True if self.first is None else False


# programming project 5.3
class LoopList:
    def __init__(self):
        self.current: Optional[Link] = None

    def __str__(self) -> str:
        display_array, current = [], self.current
        while current is not None and current.next is not self.current:
            display_array.append(current)
            current = current.next
        display_array.append(current)
        return ' '.join(str(item) for item in display_array)

    def insert(self, link_data: Any) -> None:
        new_link = Link(link_data)
        if self.current is None:
            self.current = new_link
            new_link.next = new_link
            return

        current = self.current
        while current.next is not self.current:
            current = current.next
        current.next = new_link
        new_link.next = self.current
        self.current = new_link

    def find(self, key) -> Optional[Link]:
        current = self.current
        while current.next is not self.current:
            if current.data == key:
                return current
            current = current.next
        if current.data == key:
            return current
        return None

    def delete_key(self, key) -> Optional[Link]:
        current = self.current
        previous = self.current
        while previous.next is not current:
            previous = previous.next
        while current.next is not self.current:
            if current.data == key:
                self.current = current.next
                previous.next = current.next
                return current
            previous = current
            current = current.next
        if current.data == key:
            self.current = current.next
            previous.next = current.next
            return current
        return None

    def delete(self) -> Optional[Link]:
        if self.current is self.current.next:
            result = self.current
            self.current = None
            return result
        previous = self.current
        while previous.next is not self.current:
            previous = previous.next
        previous.next = self.current.next
        result = self.current
        self.current = self.current.next
        return result

    def step(self) -> None:
        self.current = self.current.next

    @property
    def is_empty(self):
        return self.current is None


if __name__ == '__main__':
    print('LinkedList tests')
    linked_list = LinkedList()
    for value in range(10, 60, 10):
        linked_list.insert_first(value)
    print(linked_list)

    linked_list.delete_first()
    print(linked_list)

    print(linked_list.find(20))

    linked_list.delete(20)
    print(linked_list, end='\n\n')

    print('TwoWayLinkedList tests')
    linked_list = TwoWayLinkedList()
    for value in range(10, 60, 10):
        linked_list.insert_last(value)
    print(linked_list)
    for value in range(10, 60, 10):
        linked_list.insert_first(value)
    print(linked_list)

    for _ in range(5):
        print(linked_list.delete_first())
    print(linked_list, end='\n\n')

    print('SortedList tests')
    sorted_list = SortedList()
    for value in range(10, 110, 10):
        sorted_list.insert(value)
    print(sorted_list)

    for value in range(5, 105, 10):
        sorted_list.insert(value)
    print(sorted_list)

    for _ in range(10):
        print(sorted_list.delete())
    print(sorted_list, end='\n\n')

    print('LoopList tests')
    loop_list = LoopList()
    for value in range(10):
        loop_list.insert(value)
    print(loop_list)

    for value in range(10, 60, 10):
        loop_list.insert(value)
    print(loop_list)
    print(loop_list.find(50))
    print(loop_list.find(0))
    print(loop_list.find(10))
    print(loop_list.find(54))
    print(loop_list)

    print(loop_list.delete())
    print(loop_list.delete())
    print(loop_list.delete())
    print(loop_list.delete())
    print(loop_list)

    print(loop_list.step())
    print(loop_list.step())
    print(loop_list.step())
    print(loop_list)
