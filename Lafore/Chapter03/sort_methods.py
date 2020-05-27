from typing import Union, Tuple
import statistics

from Lafore.Chapter02.array import Array


class ArrayWithSort(Array):
    def bubble_sort(self) -> None:
        for unsorted_length in range(self._length-1, 0, -1):
            for index in range(unsorted_length):
                if self._state[index] > self._state[index+1]:
                    self._state[index], self._state[index+1] = self._state[index+1], self._state[index]

    def selection_sort(self) -> None:
        for unsorted_length in range(self._length):
            min_index = unsorted_length
            for index in range(unsorted_length+1, self._length):
                min_index = min_index if self._state[min_index] < self._state[index] else index
            self._state[unsorted_length], self._state[min_index] = self._state[min_index], self._state[unsorted_length]

    def insertion_sort(self) -> None:
        for unsorted_length in range(1, self._length):
            insert_elem = self._state[unsorted_length]
            insert_index = unsorted_length
            while insert_index > 0 and self._state[insert_index] >= insert_elem:
                self._state[insert_index] = self._state[insert_index-1]
                insert_index -= 1
            self._state[insert_index] = insert_elem

    # Chapter 3 programming project 1
    def bubble_two_way_sort(self) -> None:
        start_unsort_index, end_unsort_index = 0, self._length - 1
        while end_unsort_index > start_unsort_index:
            for index in range(start_unsort_index, end_unsort_index):
                if self._state[index] > self._state[index+1]:
                    self._state[index], self._state[index+1] = self._state[index+1], self._state[index]
            end_unsort_index -= 1
            for index in range(end_unsort_index, start_unsort_index, -1):
                if self._state[index] < self._state[index - 1]:
                    self._state[index], self._state[index - 1] = self._state[index - 1], self._state[index]
            start_unsort_index += 1

    # Chapter 3 programming project 2
    def median(self) -> Union[float, int]:
        self.insertion_sort()
        if self._length % 2 == 0:
            middle_index = self._length // 2
            return (self._state[middle_index - 2] + self._state[middle_index - 1]) / 2

        return self._state[self._length // 2]

    # Chapter 3 programming project 4
    def odd_even_sort(self) -> None:
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for index in range(1, self._length-1, 2):
                if self._state[index] > self._state[index + 1]:
                    self._state[index], self._state[index + 1] = self._state[index + 1], self._state[index]
                    is_sorted = False
            for index in range(0, self._length-1, 2):
                if self._state[index] > self._state[index + 1]:
                    self._state[index], self._state[index + 1] = self._state[index + 1], self._state[index]
                    is_sorted = False

    def insertion_sort_with_counter(self) -> Tuple[int, int]:
        for unsorted_length in range(1, self._length):
            insert_elem = self._state[unsorted_length]
            insert_index = unsorted_length
            copy_counter, comparison_counter = 0, 0
            while insert_index > 0:
                comparison_counter += 1
                if self._state[insert_index] >= insert_elem:
                    self._state[insert_index] = self._state[insert_index - 1]
                    copy_counter += 1
                insert_index -= 1
            self._state[insert_index] = insert_elem
        return copy_counter, comparison_counter


if __name__ == '__main__':
    data = ArrayWithSort(10)
    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    data.bubble_sort()
    assert str(data) == str(sorted(data._state))

    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    data.selection_sort()
    assert str(data) == str(sorted(data._state))

    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    data.insertion_sort()
    assert str(data) == str(sorted(data._state))

    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    data.bubble_two_way_sort()
    assert str(data) == str(sorted(data._state))

    # Chapter 3 programming project 2
    assert statistics.median(data._state) == data.median()

    # Chapter 3 programming project 4
    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    data.odd_even_sort()
    assert str(data) == str(sorted(data._state))

    # Chapter 3 programming project 5
    data._state = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(data.insertion_sort_with_counter())
    assert str(data) == str(sorted(data._state))