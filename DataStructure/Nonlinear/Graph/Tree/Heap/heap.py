class MinHeap:
    def __init__(self):
        # 최소 힙의 내부 리스트 초기화
        self.heap = []

    def push(self, value):
        # 최소 힙에 원소 추가
        self.heap.append(value)
        n = len(self.heap) - 1
        # 새로운 원소를 힙의 제자리로 이동하여 최소 힙 속성 유지
        while n > 0:
            parent = (n - 1) // 2
            if self.heap[n] < self.heap[parent]:
                self.heap[n], self.heap[parent] = self.heap[parent], self.heap[n]
                n = parent
            else:
                break

    def extract_min(self):
        # 최소 힙에서 최솟값 추출
        if not self.heap:
            return -1  # 힙이 비어있을 경우 -1 반환 또는 에러 처리
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            # 힙의 루트에서부터 아래로 이동하여 최소 힙 속성 유지
            n = 0
            size = len(self.heap)
            while True:
                left = 2 * n + 1
                right = 2 * n + 2
                smallest = n

                if left < size and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < size and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == n:
                    break

                self.heap[n], self.heap[smallest] = self.heap[smallest], self.heap[n]
                n = smallest

        return min_val

    def display(self):
        # 최소 힙 출력
        print(self.heap)


def main():
    # 최소 힙 생성
    my_heap = MinHeap()

    # 데이터 삽입
    my_heap.push(5)
    my_heap.push(3)
    my_heap.push(8)
    my_heap.push(1)
    my_heap.push(10)

    # 힙 출력
    my_heap.display()  # 출력: [1, 3, 8, 5, 10]

    # 최소값 추출
    min_val = my_heap.extract_min()
    print("Extracted min value:", min_val)  # 출력: Extracted min value: 1

    # 힙 출력
    my_heap.display()  # 출력: [3, 5, 8, 10]


main()