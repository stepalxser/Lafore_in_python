from typing import Any, Optional


class DoubleLink:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional[DoubleLink] = None
        self.previous: Optional[DoubleLink] = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinked:
    def __init__(self) -> None:
        self.first: Optional[DoubleLink] = None
        self.last: Optional[DoubleLink] = None
        self.pointer = self.first

    def __str__(self) -> str:
        display_array, current = [], self.first
        while current is not None:
            display_array.append(current)
            current = current.next
        return ' '.join(str(item) for item in display_array)

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current
            current = current.next

    @property
    def is_empty(self) -> bool:
        return self.first is None

    def insert_first(self, data: Any) -> None:
        new_link = DoubleLink(data)
        if self.is_empty:
            self.last = new_link
        else:
            self.first.previous = new_link
        new_link.next = self.first
        self.first = new_link

    def insert_last(self, data: Any) -> None:
        new_link = DoubleLink(data)
        if self.is_empty:
            self.first = new_link
        else:
            self.last.next = new_link
            new_link.previous = self.last
        self.last = new_link

    def delete_first(self) -> DoubleLink:
        if self.is_empty:
            raise ValueError('List is empty')
        temp: DoubleLink = self.first
        if self.first.next is None:
            self.last = None
        else:
            self.first.next.previous = None
            self.first = self.first.next
        return temp

    def delete_last(self) -> DoubleLink:
        if self.is_empty:
            raise ValueError('List is empty')
        temp: DoubleLink = self.last
        if self.first.next is None:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        return temp

    def insert_after(self, key: Any, data: Any) -> bool:
        if self.is_empty:
            raise ValueError('List is empty')
        current = self.first
        while current.data != key:
            current = current.next
            if current is None:
                return False

        new_link = DoubleLink(data)

        if current is self.last:
            new_link.next = None
            self.last = new_link
        else:
            new_link.next = current.next
            current.next.previous = new_link
        new_link.previous = current
        current.next = new_link
        return True

    def delete(self, key: Any) -> Optional[DoubleLink]:
        if self.is_empty:
            raise ValueError('List is empty')

        current = self.first
        while current.data != key:
            current = current.next
            if current is None:
                return None

        if current is self.first:
            current = current.next
        else:
            current.previous.next = current.next

        if current is self.last:
            self.last = current.previous
        else:
            current.next.previous = current.previous

        return current


if __name__ == '__main__':
    data = DoublyLinked()
    data.insert_first(22)
    data.insert_first(44)
    data.insert_first(66)
    print(data)

    data.insert_last(11)
    data.insert_last(33)
    data.insert_last(55)
    print(data)

    data.delete_first()
    data.delete_last()
    data.delete(11)
    print(data)

    data.insert_after(22, 77)
    data.insert_after(33, 88)
    print(data)

    for item in data:
        print(item)
    for item in data:
        print(item)