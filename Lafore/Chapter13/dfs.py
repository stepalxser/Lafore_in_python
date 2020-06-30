from pprint import pprint
from typing import List

from Lafore.Chapter05.adt import Stack, Queue


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
        if start != end:
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

    def bfs(self) -> None:
        queue = Queue()
        self._vertex_list[0].is_visited = True
        print(self._vertex_list[0], end=' ')
        queue.insert(0)

        while not queue.is_empty:
            temp = queue.remove()
            temp_neighbor = self._get_unvisited_vertex(temp)
            while temp_neighbor != -1:
                self._vertex_list[temp_neighbor].is_visited = True
                print(self._vertex_list[temp_neighbor], end=' ')
                queue.insert(temp_neighbor)
                temp_neighbor = self._get_unvisited_vertex(temp)

        for elem in self._vertex_list:
            elem.is_visited = False
        print()

    def mst(self) -> None:
        stack = Stack()
        self._vertex_list[0].is_visited = True
        stack.push(0)
        while not stack.is_empty:
            current_vertex = stack.peek()
            temp = self._get_unvisited_vertex(current_vertex)
            if temp == -1:
                stack.pop()
            else:
                self._vertex_list[temp].is_visited = True
                stack.push(temp)
                print(self._vertex_list[current_vertex], self._vertex_list[temp], sep='', end=' ')
        print()


class DirectedGraph(Graph):
    def mst(self) -> None:
        raise NotImplemented('Not working for directed graph')

    def add_edge(self, start: int, end: int) -> None:
        if start != end:
            self._matrix[start][end] = True

    def delete_vertex(self, label: str) -> None:
        for vertex in self._vertex_list:
            if vertex.label == label:
                vertex_index = self._vertex_list.index(vertex)
                break
        else:
            raise ValueError('Uncorrect label')

        del self._vertex_list[vertex_index]
        del self._matrix[vertex_index]
        for vertex_ratio in self._matrix:
            del vertex_ratio[vertex_index]

    def _no_successors(self) -> int:
        for vertex_ratio in self._matrix:
            if not any(vertex_ratio):
                return self._matrix.index(vertex_ratio)
        else:
            return -1

    def topo(self) -> None:
        temp_vertex_list = self._vertex_list.copy()
        temp_matrix = self._matrix.copy()
        result = []
        while self._vertex_list:
            current_vertex = self._no_successors()
            if current_vertex == -1:
                raise ValueError('Graph have cycles')
            result.append(self._vertex_list[current_vertex].label)
            self.delete_vertex(result[-1])

        print(*reversed(result))
        self._vertex_list = temp_vertex_list
        self._matrix = temp_matrix


if __name__ == '__main__':
    print('Tests standart graph')
    graph = Graph()
    for symbol in 'ABCDE':
        graph.add_vertex(symbol)

    for start_index in range(4):
        for end_index in range(1, 5):
            graph.add_edge(start_index, end_index)
    graph.dfs()
    graph.bfs()
    graph.mst()
    print()

    print('Test topology sort')
    graph_2 = DirectedGraph()
    for symbol in 'ABCDEFGH':
        graph_2.add_vertex(symbol)
    for start_index, end_index in zip('00123456', '34456677'):
        graph_2.add_edge(int(start_index), int(end_index))
    graph_2.dfs()
    graph_2.topo()
    print()
