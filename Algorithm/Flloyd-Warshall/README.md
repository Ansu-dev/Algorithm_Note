## 플로이드-워셜 알고리즘

---

플로이드-워셜 알고리즘은 가중치가 있는 그래프에서 모든 정점 쌍 간의 최단 경로를 찾는 알고리즘입니다. 
이 알고리즘은 다이나믹 프로그래밍(Dynamic Programming)을 기반으로 하며, 
모든 정점 쌍 간의 최단 거리를 효율적으로 계산할 수 있습니다.

* 모든 정점 쌍의 최단 경로를 한 번에 계산할 수 있습니다.
* 음의 가중치를 처리할 수 있으나, 음의 사이클(Negative Cycle)이 존재하지 않아야 합니다.
* 시간 복잡도는 O(V³) (V는 정점의 수)로, 밀집 그래프에서 효율적입니다.

````text
💡 Tip
1. 거리 행렬 초기화
   - 각 정점 쌍 간의 직접 연결된 가중치를 거리로 설정합니다.
   - 직접 연결되지 않은 정점 쌍은 무한대(inf)로 초기화합니다.
   - 자기 자신으로의 거리는 0으로 설정합니다.

2. 경유 정점을 하나씩 고려하며 거리 업데이트
   - 모든 정점을 하나씩 경유 정점(k)으로 설정합니다.
   - 각 경유 정점 k를 통해서 정점 i에서 정점 j로 가는 경로가 기존의 경로보다 짧으면, 거리를 업데이트합니다.

3. 모든 정점 쌍에 대해 반복:
   - 모든 정점 쌍 (i, j)에 대해 위 과정을 반복하여 최단 거리를 찾습니다.
````


### 예제
````python
# 그래프 예시 (0은 연결되지 않음을 의미)
# 각 행은 출발 정점을, 각 열은 도착 정점을 나타냅니다.
# 예: graph[0][1] = 5는 정점 0에서 정점 1로 가는 가중치가 5임을 의미
    graph = [
        [0, 5, 0, 8],
        [7, 0, 9, 0],
        [2, 0, 0, 4],
        [0, 0, 3, 0],
    ]
````

#### 플로이드-워셜 시각화
````scss
0
├── 1 (5)
├── 3 (8)
1
├── 0 (7)
├── 2 (9)
2
├── 0 (2)
├── 3 (4)
3
├── 2 (3)
````


플로이드-워셜 알고리즘은 모든 정점 쌍 (i, j)에 대해 최단 거리를 찾기 위해 경유 정점 k를 하나씩 고려하면서 거리를 업데이트합니다. 다음은 단계별로 알고리즘이 어떻게 동작하는지를 설명한 것입니다.

**초기 거리 행렬**
````markdown
    0   1   2   3
0   0   5   ∞   8
1   7   0   9   ∞
2   2   ∞   0   4
3   ∞   ∞   3   0
````
* ∞는 정점 간 직접 연결되지 않았음을 의미합니다.\

**경유 정점 k = 0**\
모든 정점 쌍 (i, j)에 대해 i -> 0 -> j 경로를 고려하여 거리를 업데이트합니다.
* 예: 1 -> 0 -> 1 경로는 7 + 5 = 12인데, 기존 거리 0보다 크므로 업데이트하지 않음.
* 2 -> 0 -> 1 경로는 2 + 5 = 7으로, 기존 거리 ∞에서 7로 업데이트.



업데이트된 거리 행렬:

````markdown
    0   1   2   3
0   0   5   ∞   8
1   7   0   9   ∞
2   2   7   0   4
3   ∞   ∞   3   0
````

**경유 정점 k = 1**\
모든 정점 쌍 (i, j)에 대해 i -> 1 -> j 경로를 고려하여 거리를 업데이트합니다.

* 0 -> 1 -> 2 경로는 5 + 9 = 14으로, 기존 거리 ∞에서 14로 업데이트.
* 2 -> 1 -> 3 경로는 7 + ∞ = ∞으로, 업데이트하지 않음.



업데이트된 거리 행렬:
````markdown
    0   1   2   3
0   0   5   14  8
1   7   0   9   ∞
2   2   7   0   4
3   ∞   ∞   3   0
````

**경유 정점 k = 2**\
모든 정점 쌍 (i, j)에 대해 i -> 2 -> j 경로를 고려하여 거리를 업데이트합니다.

* 1 -> 2 -> 3 경로는 9 + 4 = 13으로, 기존 거리 ∞에서 13으로 업데이트.
* 3 -> 2 -> 1 경로는 3 + 7 = 10으로, 기존 거리 ∞에서 10으로 업데이트.



업데이트된 거리 행렬:

````markdown
    0   1   2   3
0   0   5   14  8
1   7   0   9   13
2   2   7   0   4
3   ∞   10  3   0
````

**경유 정점 k = 3**\
모든 정점 쌍 (i, j)에 대해 i -> 3 -> j 경로를 고려하여 거리를 업데이트합니다.

* 0 -> 3 -> 2 경로는 8 + 3 = 11으로, 기존 거리 14에서 11로 업데이트.
* 1 -> 3 -> 2 경로는 13 + 3 = 16으로, 기존 거리 9보다 크므로 업데이트하지 않음.
* 2 -> 3 -> 1 경로는 4 + 10 = 14으로, 기존 거리 7보다 크므로 업데이트하지 않음.


최종 거리 행렬:

````markdown
    0   1   2   3
0   0   5   11  8
1   7   0   9   13
2   2   7   0   4
3   ∞   10  3   0
````


#### 최종 거리 행렬 해석
* 정점 0에서 정점 1로 가는 최단 거리는 5.
* 정점 0에서 정점 2로 가는 최단 거리는 11.
* 정점 0에서 정점 3으로 가는 최단 거리는 8.
* 정점 1에서 정점 0으로 가는 최단 거리는 7.
* 정점 1에서 정점 2로 가는 최단 거리는 9.
* 정점 1에서 정점 3으로 가는 최단 거리는 13.
* 정점 2에서 정점 0으로 가는 최단 거리는 2.
* 정점 2에서 정점 1으로 가는 최단 거리는 7.
* 정점 2에서 정점 3으로 가는 최단 거리는 4.
* 정점 3에서 정점 1으로 가는 최단 거리는 10.
* 정점 3에서 정점 2로 가는 최단 거리는 3.



#### 플로이드-워셜 알고리즘의 추가 설명
* 모든 정점 쌍의 최단 경로를 한 번에 계산할 수 있습니다.
* 다이나믹 프로그래밍을 기반으로 하므로, 작은 문제를 해결하고 이를 통해 큰 문제를 해결하는 접근 방식을 사용합니다.
* 음의 가중치를 처리할 수 있으며, 단 음의 사이클이 없는 그래프에 적용할 수 있습니다.

````text
❔ 활용 예

지도 및 내비게이션 시스템: 모든 지점 간의 최단 경로를 미리 계산하여 빠른 길 찾기에 활용합니다.

네트워크 라우팅: 데이터 패킷이 최적의 경로로 전달되도록 라우팅 테이블을 생성합니다.

소셜 네트워크 분석: 사용자 간의 연결 강도를 기반으로 최단 연결 경로를 찾습니다.

운영 연구: 자원 배분, 경로 계획 등 다양한 최적화 문제에 활용됩니다.
````