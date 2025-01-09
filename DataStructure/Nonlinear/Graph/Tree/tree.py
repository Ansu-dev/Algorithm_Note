class TreeNode:
    def __init__(self, value):
        """
        새로운 TreeNode를 생성합니다.
        :param value: 노드의 값 (문자열)
        """
        # TreeNode의 값과 자식 노드를 초기화
        self.value = value
        self.children = []

    def add_child(self, child):
        """
        자식 노드를 추가합니다.
        :param child: 추가할 자식 TreeNode 인스턴스
        """
        # 자식 노드 리스트에 새로운 자식 추가
        self.children.append(child)

    def __str__(self):
        """
        트리를 문자열로 반환합니다.
        """
        return self.string_with_indent(0)

    def string_with_indent(self, indent):
        """
        들여쓰기를 포함하여 트리를 문자열로 반환합니다.
        :param indent: 현재 노드의 들여쓰기 수준
        """
        indent_str = "\t"
        indentation = indent_str * indent

        # 현재 노드의 값과 개행 문자 추가
        result = f"{indentation}{self.value}\n"
        # 모든 자식 노드에 대해 재귀적으로 문자열 생성
        for child in self.children:
            result += child.string_with_indent(indent + 1)

        return result


def main():
    # 트리 생성
    root = TreeNode("Root")

    # 자식 노드 추가
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    child11 = TreeNode("Child 1.1")
    child12 = TreeNode("Child 1.2")

    child1.add_child(child11)
    child1.add_child(child12)

    # 트리 출력
    print(root)


main()