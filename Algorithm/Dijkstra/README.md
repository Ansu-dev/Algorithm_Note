## 다익스트라 알고리즘

---

다익스트라 알고리즘은 **가중치가 있는 그래프**에서 한 정점을 시작점으로 하여 다른 **모든 정점까지의 최단 경로를 찾는 알고리즘**입니다. 
이 알고리즘은 음의 가중치를 가지지 않는 그래프에 적용할 수 있으며, 다양한 분야에서 최단 경로를 찾는 데 널리 사용됩니다.


* 최단 경로 찾기: 시작 정점에서 다른 모든 정점까지의 최단 경로를 효율적으로 찾습니다.
* 우선순위 큐 사용: 현재까지 발견된 최단 거리를 기반으로 다음에 방문할 정점을 선택합니다.
* 비음수 가중치: 모든 간선의 가중치는 0 이상이어야 합니다.


````text
💡 Tip
1. 시작 정점을 선택하고, 시작 정점의 거리를 0으로 설정합니다. 다른 모든 정점의 거리는 무한대로 초기화합니다.
2. 우선순위 큐(최소 힙)를 사용하여 현재까지 발견된 최단 거리를 기준으로 정점을 관리합니다. 처음에는 시작 정점만 큐에 추가됩니다.
3. 큐에서 가장 거리가 짧은 정점을 꺼내어 처리합니다.
4. 현재 정점의 모든 인접 정점을 탐색하고, 현재 정점을 거쳐서 인접 정점으로 가는 거리가 기존에 기록된 거리보다 짧으면 거리를 업데이트하고 큐에 추가합니다.
5. 큐가 빌 때까지 3~4단계를 반복합니다.
6. 모든 정점의 최단 거리가 결정되면 알고리즘을 종료합니다.
````

### 예제
````python
# 그래프를 인접 리스트로 표현 (딕셔너리 내 딕셔너리 형태)
graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}
````

1. 그래프 표현:
그래프는 인접 리스트 형태로 표현되며, 각 정점은 딕셔너리로 표현됩니다.
예를 들어, "A": {"B": 8, "C": 1, "D": 2}는 정점 A가 B, C, D와 각각 가중치 8, 1, 2로 연결되어 있음을 의미합니다.

2. 거리 초기화:
모든 정점의 거리를 **무한대(float('inf'))**로 초기화하고, 시작 정점의 거리는 0으로 설정합니다.

3. 우선순위 큐:
Python의 heapq 모듈을 사용하여 최소 힙을 구현합니다.
우선순위 큐에는 (거리, 정점) 튜플을 저장하여, 현재까지 발견된 최단 거리가 짧은 정점부터 처리됩니다.

4. 최단 거리 계산:
큐에서 가장 거리가 짧은 정점을 꺼내고, 해당 정점의 인접 정점들을 탐색합니다.
현재 정점을 거쳐서 인접 정점으로 가는 거리가 기존에 기록된 거리보다 짧으면, 거리를 업데이트하고 큐에 추가합니다.

5. 결과 출력:
모든 정점의 최단 거리가 계산되면, 시작 정점으로부터 각 정점까지의 최단 거리를 출력합니다.


````scss
최단 거리 결과 from A: {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}


A
├── B (8)
├── C (1)
└── D (2)
    ├── E (3)
    └── F (5)
C
├── B (5)
└── D (2)
E
└── F (1)
F
└── A (5)
````


#### 단계별 탐색 과정
1. 시작점 A 설정:
A의 거리는 0으로 설정.
큐: [(0, 'A')]


2. A 방문:
현재 거리: 0, 현재 노드: A
A의 인접 노드: B (8), C (1), D (2)
B의 거리: 0 + 8 = 8 → 업데이트
C의 거리: 0 + 1 = 1 → 업데이트
D의 거리: 0 + 2 = 2 → 업데이트
큐: [(1, 'C'), (2, 'D'), (8, 'B')]


3. C 방문:
현재 거리: 1, 현재 노드: C
C의 인접 노드: B (5), D (2)
B의 거리: 1 + 5 = 6 → 업데이트 (8에서 6으로 감소)
D의 거리: 1 + 2 = 3 → 업데이트 (2에서 3으로 증가하지 않음)
큐: [(2, 'D'), (8, 'B'), (6, 'B')]


4. D 방문:
현재 거리: 2, 현재 노드: D
D의 인접 노드: E (3), F (5)
E의 거리: 2 + 3 = 5 → 업데이트
F의 거리: 2 + 5 = 7 → 업데이트
큐: [(5, 'E'), (6, 'B'), (8, 'B'), (7, 'F')]


5. E 방문:
현재 거리: 5, 현재 노드: E
E의 인접 노드: F (1)
F의 거리: 5 + 1 = 6 → 업데이트 (7에서 6으로 감소)
큐: [(6, 'B'), (6, 'F'), (8, 'B'), (7, 'F')]


6. B 방문:
현재 거리: 6, 현재 노드: B
B의 인접 노드: 없음
큐: [(6, 'F'), (7, 'F'), (8, 'B')]


7. F 방문:
현재 거리: 6, 현재 노드: F
F의 인접 노드: A (5)
A의 거리: 6 + 5 = 11 → 업데이트 불필요 (A의 현재 거리 0)
큐: [(7, 'F'), (8, 'B')]


8. F 방문 (반복):
현재 거리: 7, 현재 노드: F
이미 더 짧은 거리(6)가 기록됨 → 무시


9. 큐: [(8, 'B')]
B 방문 (반복):
현재 거리: 8, 현재 노드: B
이미 더 짧은 거리(6)가 기록됨 → 무시
큐: []


10. 탐색 종료:
큐가 비었으므로 알고리즘 종료.
최종 거리: {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}



#### 다익스트라의 추가 설명
* 효율성: 우선순위 큐를 사용하여 O((V + E) log V)의 시간 복잡도로 최단 경로를 찾을 수 있습니다.
* 단순성: 구현이 비교적 간단하며, 다양한 프로그래밍 언어에서 쉽게 적용할 수 있습니다.
* 정확성: 음의 가중치가 없는 그래프에서 정확한 최단 경로를 보장합니다.

````text
❔ 활용 예

지도 및 내비게이션 시스템: 최단 경로를 찾는 데 사용됩니다.

네트워크 라우팅: 데이터 패킷이 최적의 경로로 전달되도록 합니다.

게임 개발: 캐릭터의 이동 경로나 NPC의 경로 탐색에 사용됩니다.

운영 연구: 최적화 문제에서 자원 배분이나 경로 계획에 활용됩니다.
````