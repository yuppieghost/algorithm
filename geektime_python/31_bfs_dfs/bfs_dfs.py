"""
    Breadth-first search and depth-first search.

    Author: Wenru Dong
"""

from typing import List, Optional, Generator, IO
from collections import deque


class Graph:
    """Undirected graph."""

    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int) -> IO[str]:
        """Print out the path from Vertex s to Vertex t
        using bfs.
        """
        if s == t: return
        # initialize
        # 两个数组 一个队列
        visited = [False] * self._num_vertices
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self._num_vertices

        while q:
            #  取出头部顶点
            v = q.popleft()
            # 在图中查找该点的相邻顶点,并且从visited中判断是否已经访问过
            for neighbour in self._adjacency[v]:
                # 如果是新的顶点
                if not visited[neighbour]:
                    # 记录该点的前驱结点为v
                    prev[neighbour] = v
                    visited[neighbour] = True
                    q.append(neighbour)
                    # 如果该点即t, 递归打印路径
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return

    def dfs(self, s: int, t: int) -> IO[str]:
        """Print out a path from Vertex s to Vertex t
        using dfs.
        """
        found = False
        visited = [False] * self._num_vertices
        prev = [None] * self._num_vertices

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))


if __name__ == "__main__":
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)
