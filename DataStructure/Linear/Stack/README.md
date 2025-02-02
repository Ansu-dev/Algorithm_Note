## 스택

스택(Stack)은 LIFO(Last In, First Out), 
즉 후입선출 방식으로 동작하는 자료구조입니다. 
스택은 접시를 쌓는 것과 비슷한 구조로, 나중에 쌓은 접시가 먼저 나오는 것처럼, 
마지막에 추가된 원소가 가장 먼저 제거됩니다.


* 후입선출(LIFO): 가장 나중에 추가된 원소가 가장 먼저 제거됩니다.
* 단방향 접근: 스택의 가장 위에 있는 원소에만 접근할 수 있습니다.
* 기본 연산:
  * Push: 스택의 가장 위에 원소를 추가합니다.
  * Pop: 스택의 가장 위에 있는 원소를 제거하고 반환합니다.
  * Peek: 스택의 가장 위에 있는 원소를 제거하지 않고 반환합니다.
  * Is_empty: 스택이 비어있는지 확인합니다.
  * Size: 스택에 있는 원소의 개수를 반환합니다.
  * Traverse: 스택의 모든 원소를 순회합니다.


### 예제
1. 스택 생성 및 원소 추가
* 스택 생성: my_stack = Stack()
* 원소 추가: my_stack.push(6), my_stack.push(7)
````scss
스택 상태:
+-----+
|  7  | <- 가장 위
+-----+
|  6  |
+-----+
````
 
2. 원소 추출 (Pop)
* 추출된 원소: 7
* 스택 상태:
````scss
스택 상태:
+-----+
|  6  | <- 가장 위
+-----+
````

3. 원소 조회 (Peek)
* 조회된 원소: 6
* 스택 상태: 변경 없음
````scss
스택 상태:
+-----+
|  6  | <- 가장 위
+-----+
````

4. 스택 비어있는지 확인
* 결과: False (스택에 6이 남아 있음)


5. 스택 순회 (Traverse)
* 출력: 6