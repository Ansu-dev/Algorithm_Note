class HashTable:
    def __init__(self, size):
        # 해시 테이블의 크기와 내부 테이블 초기화
        self.size = size
        self.table = {}

    def _hash_function(self, key):
        # 간단한 해시 함수: 키의 길이를 크기로 나눈 나머지
        return len(key) % self.size

    def insert(self, key, value):
        # Python의 dict는 이미 해시 충돌 처리를 내장하고 있으므로 별도로 리스트 등을 사용할 필요가 없습니다.
        self.table[key] = value

    def get(self, key):
        # 키가 존재하면 (값, True)를 반환하고, 없으면 (None, False)를 반환
        if key in self.table:
            return self.table[key], True
        else:
            return None, False

    def remove(self, key):
        # 키가 존재하면 해시 테이블에서 제거
        if key in self.table:
            del self.table[key]

    def display(self):
        # 해시 테이블의 모든 키-값 쌍을 출력
        for key, value in self.table.items():
            print(f"Key: {key}, Value: {value}")


def main():
    # 해시 테이블 생성
    my_hash_table = HashTable(10)

    # 데이터 삽입
    my_hash_table.insert("apple", 5)
    my_hash_table.insert("banana", 7)
    my_hash_table.insert("cherry", 3)

    # 데이터 조회
    value, found = my_hash_table.get("apple")
    if found:
        print("apple:", value)
    else:
        print("apple 키를 찾을 수 없습니다.")

    value, found = my_hash_table.get("banana")
    if found:
        print("banana:", value)
    else:
        print("banana 키를 찾을 수 없습니다.")

    value, found = my_hash_table.get("grape")
    if found:
        print("grape:", value)
    else:
        print("grape 키를 찾을 수 없습니다.")

    # 데이터 삭제
    my_hash_table.remove("apple")

    # 해시 테이블 출력
    my_hash_table.display()

main()
