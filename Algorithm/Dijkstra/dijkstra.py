import heapq

# 그래프를 인접 리스트로 표현 (딕셔너리 내 딕셔너리 형태)
graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}

def dijkstra(graph, start):
    # 모든 정점의 최단 거리를 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 정점의 거리는 0

    # 우선순위 큐에 (거리, 정점) 튜플을 추가
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 최단 거리가 확정된 경우 건너뜀
        if current_distance > distances[current_node]:
            continue

        # 현재 정점의 인접 정점들을 탐색
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 새로 계산된 거리가 기존 거리보다 짧으면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    start_node = "A"
    shortest_distances = dijkstra(graph, start_node)
    print(f"최단 거리 결과 from {start_node}: {shortest_distances}")