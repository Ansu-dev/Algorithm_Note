def main():
    # 빈 리스트 생성
    my_slice = []

    # 원소를 포함한 리스트 생성
    my_slice_with_elements = [1, 2, 3, 4, 5]

    # 리스트의 길이(크기) 확인
    _ = len(my_slice_with_elements)

    # 리스트의 앞쪽에 원소 추가 (덱의 appendleft와 유사)
    my_slice = [0] + my_slice

    # 리스트의 뒤쪽에 원소 추가 (덱의 append와 유사)
    my_slice.append(6)

    # 리스트의 앞쪽 원소 추출 (덱의 popleft와 유사)
    _ = my_slice[0]
    my_slice = my_slice[1:]

    # 리스트의 뒤쪽 원소 추출 (덱의 pop과 유사)
    rear = my_slice[-1]
    _ = rear
    my_slice = my_slice[:-1]

    # 리스트 순회(iteration)
    for element in my_slice_with_elements:
        print(element)

    # 리스트의 특정 원소 인덱스 찾기
    search_value = 3
    index = -1
    for i, element in enumerate(my_slice_with_elements):
        if element == search_value:
            index = i
            break

    print("Index of 3:", index)