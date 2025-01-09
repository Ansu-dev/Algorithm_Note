def main():
    # 빈 리스트 생성
    my_list = []

    # 원소를 포함한 리스트 생성
    my_list_with_elements = [1, 2, 3, 4, 5]

    # 다차원 리스트 생성
    multi_dimensional_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # 리스트의 길이(크기) 확인
    length = len(my_list_with_elements)
    print(f"리스트의 길이: {length}")  # 출력: 리스트의 길이: 5

    # 리스트의 특정 원소에 접근
    third_element = my_list_with_elements[2]  # 3번째 원소에 접근 (인덱스는 0부터 시작)
    print(f"3번째 원소: {third_element}")  # 출력: 3번째 원소: 3

    # 리스트의 원소 변경
    my_list_with_elements[0] = 10  # 첫 번째 원소를 10으로 변경
    print(f"변경된 리스트: {my_list_with_elements}")  # 출력: 변경된 리스트: [10, 2, 3, 4, 5]

    # 리스트에 원소 추가
    my_list.append(6)  # 리스트에 6을 추가
    print(f"원소 추가된 리스트: {my_list}")  # 출력: 원소 추가된 리스트: [6]

    # 리스트의 원소 삭제
    index_to_delete = 2
    if 0 <= index_to_delete < len(my_list_with_elements):
        del my_list_with_elements[index_to_delete]
    print(f"원소 삭제된 리스트: {my_list_with_elements}")  # 출력: 원소 삭제된 리스트: [10, 2, 4, 5]

    # 리스트 순회(iteration)
    print("리스트 순회:")
    for element in my_list_with_elements:
        print(element)
    # 출력:
    # 리스트 순회:
    # 10
    # 2
    # 4
    # 5

    # 리스트의 특정 원소 인덱스 찾기
    search_value = 4
    try:
        index = my_list_with_elements.index(search_value)
    except ValueError:
        index = -1
    print(f"값 {search_value}의 인덱스: {index}")  # 출력: 값 4의 인덱스: 2

    # 리스트 슬라이싱
    start_index = 1
    end_index = 4
    sub_list = my_list_with_elements[start_index:end_index]  # 2번째부터 4번째 원소까지 슬라이싱
    print(f"슬라이스된 리스트: {sub_list}")  # 출력: 슬라이스된 리스트: [2, 4, 5]