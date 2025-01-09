from collections import deque

# 상, 하, 좌, 우 탐색을 위한 방향 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, grid):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()
        print(f"방문 위치: ({current_x}, {current_y})")

        # 현재 위치에서 인접한 위치 탐색
        for d in range(4):
            nx, ny = current_x + dx[d], current_y + dy[d]

            # 배열 범위 안에 있고 방문하지 않았으며, 이동 가능한 경로라면 큐에 추가
            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                not visited[nx][ny] and
                grid[nx][ny] == 1):
                queue.append((nx, ny))
                visited[nx][ny] = True

def main():
    # 2차원 배열 예제 (1은 갈 수 있는 경로, 0은 갈 수 없는 경로)
    grid = [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
    ]

    # 방문 정보 초기화
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # 예시로 (0, 0)부터 탐색 시작
    bfs(0, 0, visited, grid)


main()