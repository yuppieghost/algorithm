from collections import deque


class Graph:
    def __init__(self, v_num: int):
        self.v_num = v_num
        self.adj_tbl = [[] for _ in range(v_num)]

    def add_edge(self, s: int, t: int) -> None:
        self.adj_tbl[s].append(t)
        self.adj_tbl[t].append(s)

    def _generate_path(self, s: int, t: int, prev):
        # 递归结束条件: 找不到前驱结点或s == t
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s, t):
        if s == t:
            return
        visited = [False] * self.v_num
        # error
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self.v_num
        # 队列不为空代表还有相邻节点没去到
        # 结束条件为 tmp = t
        while q:
            cur = q.popleft()
            for neighbor in self.adj_tbl[cur]:
                if not visited[neighbor]:
                    # error cur as q
                    prev[neighbor] = cur
                    visited[neighbor] = True
                    q.append(neighbor)
                    if neighbor == t:
                        print("final prev:", list(enumerate(prev)))
                        print("->".join(self._generate_path(s, t, prev)))
                        return

    def dfs(self, s, t):
        """
        Print out a path from Vertex s to Vertex t using dfs.
        """
        found = False
        visited = [False] * self.v_num
        prev = [None] * self.v_num

        def _dfs(frm):
            nonlocal found
            if found: return
            visited[frm] = True
            if frm == t:
                found = True
                return
            for neighbour in self.adj_tbl[frm]:
                if not visited[neighbour]:
                    prev[neighbour] = frm
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
# 0->1->2->5->7
# 0->1->2->5->4->6->7
