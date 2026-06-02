from collections import deque
import heapq

class SearchAlgorithms:

    @staticmethod
    def bfs(graph, start, goal):

        queue = deque([[start]])
        visited = set()

        node_expansions = 0

        while queue:

            path = queue.popleft()
            node = path[-1]
            node_expansions += 1

            if node == goal:
                return path, node_expansions

            if node not in visited:

                visited.add(node)

                for neighbor in graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return None

    @staticmethod
    def dfs(graph, start, goal):

        stack = [[start]]
        visited = set()

        node_expansions = 0

        while stack:

            path = stack.pop()
            node = path[-1]

            node_expansions += 1

            if node == goal:
                return path, node_expansions

            if node not in visited:

                visited.add(node)

                for neighbor in graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

        return None, node_expansions

    @staticmethod
    def ucs(graph, start, goal):

        priority_queue = [(0, start, [start])]
        visited = set()

        while priority_queue:

            cost, node, path = heapq.heappop(priority_queue)

            if node == goal:
                return path, cost, len(visited)

            if node not in visited:

                visited.add(node)

                for neighbor, edge_cost in graph[node]:

                    new_cost = cost + edge_cost

                    heapq.heappush(
                        priority_queue,
                        (
                            new_cost,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None, 0, len(visited)

    @staticmethod
    def greedy(graph, heuristic, start, goal):

        priority_queue = [(heuristic[start], start, [start])]
        visited = set()

        while priority_queue:

            _, node, path = heapq.heappop(priority_queue)

            if node == goal:
                return path, len(visited)

            if node not in visited:

                visited.add(node)

                for neighbor in graph[node]:
                    heapq.heappush(
                        priority_queue,
                        (
                            heuristic[neighbor],
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None, len(visited)

    @staticmethod
    def astar(graph, heuristic, start, goal):

        priority_queue = [(0, start, [start], 0)]
        visited = set()

        while priority_queue:

            f, node, path, g = heapq.heappop(priority_queue)

            if node == goal:
                return path, g, len(visited)

            if node not in visited:

                visited.add(node)

                for neighbor, cost in graph[node]:

                    new_g = g + cost
                    h = heuristic[neighbor]
                    new_f = new_g + h

                    heapq.heappush(
                        priority_queue,
                        (
                            new_f,
                            neighbor,
                            path + [neighbor],
                            new_g
                        )
                    )

        return None, 0, len(visited)