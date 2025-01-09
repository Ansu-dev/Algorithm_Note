class TrieNode:
    def __init__(self):
        # TrieNode의 자식 노드를 저장할 딕셔너리 초기화
        self.children = {}
        # 단어의 끝을 표시하는 플래그
        self.is_end = False


class Trie:
    def __init__(self):
        # Trie의 루트 노드를 초기화
        self.root = TrieNode()

    def insert(self, word):
        # 단어를 Trie에 삽입하는 메서드
        node = self.root
        for char in word:
            # 현재 문자에 해당하는 자식 노드가 없으면 새로 생성
            if char not in node.children:
                node.children[char] = TrieNode()
            # 현재 노드를 해당 자식 노드로 이동
            node = node.children[char]
        # 단어의 끝을 표시
        node.is_end = True

    def search(self, word):
        # 단어가 Trie에 존재하는지 검색하는 메서드
        node = self.root
        for char in word:
            # 현재 문자에 해당하는 자식 노드가 없으면 단어는 존재하지 않음
            if char not in node.children:
                return False
            # 현재 노드를 해당 자식 노드로 이동
            node = node.children[char]
        # 단어의 끝이 맞는지 확인
        return node.is_end


def main():
    # Trie 생성
    my_trie = Trie()

    # 단어 삽입
    my_trie.insert("apple")
    my_trie.insert("app")
    my_trie.insert("banana")

    # 단어 검색
    print("Search 'apple':", my_trie.search("apple"))   # 출력: True
    print("Search 'app':", my_trie.search("app"))       # 출력: True
    print("Search 'banana':", my_trie.search("banana")) # 출력: True
    print("Search 'grape':", my_trie.search("grape"))   # 출력: False


main()