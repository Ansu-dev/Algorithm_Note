class Node:
    def __init__(self, data):
        # Node의 데이터와 다음 노드를 초기화
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # LinkedList의 헤드를 초기화
        self.head = None

    def append(self, data):
        # LinkedList에 새로운 노드 추가
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def traverse(self):
        # LinkedList를 순회하며 데이터 출력
        current = self.head
        while current is not None:
            current = current.next


def main():
    # 빈 연결 리스트 생성
    my_linked_list = LinkedList()

    # 노드 추가
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    # 연결 리스트 순회
    my_linked_list.traverse()


main()