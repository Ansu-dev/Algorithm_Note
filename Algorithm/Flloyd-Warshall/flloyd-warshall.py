def floyd_warshall(graph):
    """
    플로이드-워셜 알고리즘을 사용하여 모든 정점 쌍 간의 최단 거리를 계산합니다.

    :param graph: 2차원 리스트로 표현된 가중치 그래프 (0은 연결되지 않음을 의미)
    :return: 모든 정점 쌍 간의 최단 거리 행렬
    """
    num_vertices = len(graph)
    # 거리 행렬 초기화
    distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != 0:
                distances[i][j] = graph[i][j]

    # 플로이드-워셜 알고리즘 수행
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances


def print_distances(distances):
    """
    거리 행렬을 보기 좋게 출력합니다.

    :param distances: 최단 거리 행렬
    """
    num_vertices = len(distances)
    print("최단 거리 행렬:")
    for i in range(num_vertices):
        for j in range(num_vertices):
            if distances[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(int(distances[i][j]), end="\t")
        print()


def main():
    # 그래프 예시 (0은 연결되지 않음을 의미)
    # 각 행은 출발 정점을, 각 열은 도착 정점을 나타냅니다.
    # 예: graph[0][1] = 5는 정점 0에서 정점 1로 가는 가중치가 5임을 의미
    graph = [
        [0, 5, 0, 8],
        [7, 0, 9, 0],
        [2, 0, 0, 4],
        [0, 0, 3, 0],
    ]

    # 모든 정점 쌍 간의 최단 거리 계산
    shortest_distances = floyd_warshall(graph)

    # 결과 출력
    print_distances(shortest_distances)


main()
