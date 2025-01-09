import heapq
import math

# 간선을 나타내는 클래스
class Edge:
    def __init__(self, to, weight):
        # 간선의 목적지 노드와 가중치를 초기화
        self.to = to
        self.weight = weight

# 그래프를 나타내는 클래스
class Graph:
    def __init__(self):
        # 노드와 간선을 저장할 딕셔너리 초기화
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        # 노드를 추가하고, 해당 노드의 간선 리스트를 초기화
        self.nodes[node] = True
        self.edges[node] = []

    def add_edge(self, from_node, to_node, weight):
        # 간선을 추가 (양방향 그래프)
        self.edges[from_node].append(Edge(to_node, weight))
        self.edges[to_node].append(Edge(from_node, weight))

    def dijkstra(self, start):
        # 다익스트라 알고리즘을 사용하여 최단 거리를 계산
        distances = {node: math.inf for node in self.nodes}
        distances[start] = 0

        # 우선순위 큐 초기화 (힙)
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        while priority_queue:
            current_weight, current_node = heapq.heappop(priority_queue)

            # 현재 노드의 거리가 이미 더 짧은 경우 무시
            if current_weight > distances[current_node]:
                continue

            # 인접한 노드들에 대해 거리 갱신
            for edge in self.edges[current_node]:
                distance = current_weight + edge.weight
                if distance < distances[edge.to]:
                    distances[edge.to] = distance
                    heapq.heappush(priority_queue, (distance, edge.to))

        return distances

def main():
    # 그래프 생성
    my_graph = Graph()
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")
    my_graph.add_node("D")
    my_graph.add_node("E")

    # 간선 추가
    my_graph.add_edge("A", "B", 5)
    my_graph.add_edge("B", "C", 3)
    my_graph.add_edge("C", "D", 1)
    my_graph.add_edge("D", "E", 2)
    my_graph.add_edge("A", "E", 8)

    # 최단 경로 계산
    start_node = "A"
    shortest_distances = my_graph.dijkstra(start_node)

    # 결과 출력
    for node, distance in shortest_distances.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")

main()