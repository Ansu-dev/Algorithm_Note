from collections import deque

def main():
    # 빈 큐 생성
    my_queue = deque()

    # 큐에 원소 추가
    my_queue.append(6)
    my_queue.append(7)

    # 큐에서 원소 추출
    if my_queue:
        popped_element = my_queue.popleft()
        print(popped_element)  # 출력: 6

    # 큐의 가장 앞의 원소 조회 (제거하지 않고)
    if my_queue:
        peek_element = my_queue[0]
        print(peek_element)  # 출력: 7

    # 큐가 비어있는지 확인
    is_empty = len(my_queue) == 0
    print(is_empty)  # 출력: False

    # 큐 순회(iteration)
    for element in my_queue:
        print(element)  # 출력: 7


main()