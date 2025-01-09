import heapq

class IntHeap:
    def __init__(self):
        # IntHeap의 내부 힙 리스트 초기화
        self.heap = []

    def __len__(self):
        # 힙의 크기를 반환
        return len(self.heap)

    def push(self, item):
        # 힙에 새로운 원소 추가
        heapq.heappush(self.heap, item)

    def pop(self):
        # 힙에서 최솟값 추출
        return heapq.heappop(self.heap)

    def peek(self):
        # 힙에서 최솟값 조회 (제거하지 않고)
        if self.heap:
            return self.heap[0]
        return None

    def traverse(self):
        # 힙을 순회하며 모든 원소를 추출하고 출력
        while self.heap:
            element = self.pop()
            print(element)


def main():
    # 빈 우선순위 큐 생성
    my_priority_queue = IntHeap()

    # 우선순위 큐에 원소 추가
    my_priority_queue.push(5)
    my_priority_queue.push(2)
    my_priority_queue.push(8)

    # 우선순위 큐에서 최솟값 추출
    min_value = my_priority_queue.pop()
    print(f"추출된 최솟값: {min_value}")

    # 우선순위 큐에서 최솟값 조회 (제거하지 않고)
    min_value_peek = my_priority_queue.peek()
    print(f"현재 최솟값 (조회만 함): {min_value_peek}")

    # 원소를 추가하지 않고 최솟값 조회
    min_value_peek_again = my_priority_queue.peek()
    print(f"현재 최솟값 (다시 조회): {min_value_peek_again}")

    # 우선순위 큐 순회(iteration)
    print("우선순위 큐의 모든 원소를 순회하며 출력:")
    my_priority_queue.traverse()

main()