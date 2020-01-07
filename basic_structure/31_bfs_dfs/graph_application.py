# -*- coding:utf-8 -*-

from collections import deque
from graph import Undigraph


def find_vertex_by_degree(graph, s, degree):
    if len(graph) <= 1:
        return []
    if degree == 0:
        return [s]
    queue = deque()
    prev = [None] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while queue:
        sz = len(queue)
        for i in range(sz):
            v = queue.popleft()
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    prev[adj_v] = v
                    visited[adj_v] = True
                    queue.append(adj_v)
        degree -= 1
        if degree == 0:
            return list(queue)


def my_find_vertex_by_degree(graph, s, degree):
    if len(graph) <= 1:
        return []
    if degree == 0:
        return [s]
    prev = [None] * len(graph)
    visited = [False] * len(graph)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        # 每层对应一度
        for i in range(len(q)):
            vertex = q.popleft()
            for j in graph[vertex]:
                if not visited[j]:
                    prev[j] = vertex
                    visited[j] = True
                    q.append(j)
        # 每层对应一度
        degree -= 1
        if degree == 0:
            return list(q)



if __name__ == '__main__':
    g = Undigraph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)

    #     0 - 1 - 2
    #     |   |   |
    #     3 - 4 - 5
    #         |   |
    #         6 - 7

    # print(find_vertex_by_degree(g, 0, 1))
    # print(find_vertex_by_degree(g, 0, 2))
    # print(find_vertex_by_degree(g, 0, 3))
    print(my_find_vertex_by_degree(g, 0, 1))
    print(my_find_vertex_by_degree(g, 0, 2))
    print(my_find_vertex_by_degree(g, 0, 3))
