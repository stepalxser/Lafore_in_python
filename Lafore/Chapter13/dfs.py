from typing import List

from Lafore.Chapter05.adt import Stack


class Vertex:
    def __init__(self, label: str) -> None:
        self.label: str = label
        self.is_visited: bool = False

    def __str__(self) -> str:
        return self.label


class Graph:
    def __init__(self) -> None:
        self._vertex_list: List[Vertex] = []
        self._matrix: List[List[bool]] = []

    def add_vertex(self, label: str) -> None:
        new_vertex = Vertex(label)
        self._vertex_list.append(new_vertex)
        for ratio in self._matrix:
            ratio.append(False)
        self._matrix.append([False for _ in range(len(self._matrix) + 1)])

    def add_edge(self, start: int, end: int) -> None:
        self._matrix[start][end] = True
        self._matrix[end][start] = True

    def _get_unvisited_vertex(self, index: int) -> int:
        for vetrex_index in range(len(self._vertex_list)):
            if self._matrix[index][vetrex_index] and not self._vertex_list[vetrex_index].is_visited:
                return vetrex_index
        else:
            return -1

    def dfs(self) -> None:
        stack = Stack()
        self._vertex_list[0].is_visited = True
        print(self._vertex_list[0], end=' ')
        stack.push(0)
        while not stack.is_empty:
            index = self._get_unvisited_vertex(stack.peek())
            if index == -1:
                stack.pop()
            else:
                self._vertex_list[index].is_visited = True
                print(self._vertex_list[index], end=' ')
                stack.push(index)

        for elem in self._vertex_list:
            elem.is_visited = False
        print()


if __name__ == '__main__':
    graph = Graph()
    for symbol in 'ABCDE':
        graph.add_vertex(symbol)

    for start, end in zip(range(4), range(1,5)):
        graph.add_edge(start, end)

    graph.dfs()

