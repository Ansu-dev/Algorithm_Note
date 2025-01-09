class Stack:
    def __init__(self):
        # 스택의 내부 리스트 초기화
        self.stack = []

    def push(self, item):
        # 스택에 원소 추가
        self.stack.append(item)

    def pop(self):
        # 스택에서 원소 추출
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        # 스택의 가장 위 원소 조회
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        # 스택이 비어있는지 확인
        return len(self.stack) == 0

    def __len__(self):
        # 스택의 크기 반환
        return len(self.stack)

    def traverse(self):
        # 스택의 모든 원소 순회
        for element in self.stack:
            print(element)

def main():
    # 빈 스택 생성
    my_stack = Stack()

    # 스택에 원소 추가
    my_stack.push(6)
    my_stack.push(7)

    # 스택에서 원소 추출
    try:
        popped_element = my_stack.pop()
        print(popped_element)  # 출력: 7
    except IndexError as e:
        print(e)

    # 스택의 가장 위의 원소 조회 (제거하지 않고)
    peek_element = my_stack.peek()
    if peek_element is not None:
        print(peek_element)  # 출력: 6

    # 스택이 비어있는지 확인
    is_empty = my_stack.is_empty()
    print(is_empty)  # 출력: False

    # 스택 순회(iteration)
    my_stack.traverse()  # 출력: 6


main()
