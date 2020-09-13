# 0 1 0 2 1 0 1 3 2 1 2 1 의 지형을 배열로 나타낸 것은
# 각각의 위치의 높이이다. 이 때, 담길 수 있는 물의 양을 채워보자.

import sys
import heapq

def get_raindrop(first_value, second_value, first_index, second_index, exist_height):
    small_index = first_index if first_index < second_index else second_index
    large_index = second_index if first_index < second_index else first_index

    add_up = second_value * (abs(first_index - second_index) - 1)

    for i in range(small_index + 1, large_index):
        add_up -= exist_height[i]
    
    return add_up

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    exist_height = []
    height_list = []

    # Make Max-Heap with multiply -1.
    for i in range(0, n):
        height = int(sys.stdin.readline().rstrip())
        exist_height.append(height)
        heapq.heappush(height_list, (-1 * height, i))
    
    raindrop = 0

    # 가장 높은 기둥, 가장 낮은 기둥을 
    (first_value, first_index) = heapq.heappop(height_list)
    (second_value, second_index) = heapq.heappop(height_list)
    raindrop = get_raindrop(first_value * -1, second_value * -1, first_index, second_index, exist_height)

    # 왼쪽부터 가장 큰 index
    left_top = first_index if first_index < second_index else second_index
    # 오른쪽부터 가장 큰 index
    right_top = second_index if first_index < second_index else first_index

    
    # 왼쪽 / 오른쪽 index 중 가장 큰 값을 계속 체크해 가면서 진행.
    while len(height_list) != 0:
        (poped_value, poped_index) = heapq.heappop(height_list)
        if poped_value == 0:
            continue
        if poped_index < left_top:
            # 만약 나온 값이 왼쪽 값중 가장 큰 값보다 더 왼쪽인가?
            raindrop += get_raindrop(exist_height[left_top], poped_value * -1, left_top, poped_index, exist_height)
            left_top = poped_index
        elif poped_index > right_top:
            # 만약 나온 값이 오른쪽 값중 가장 큰 값보다 더 오른쪽인가?
            raindrop += get_raindrop(exist_height[right_top], poped_value * -1, right_top, poped_index, exist_height)
            right_top = poped_index
        # 만약 나온 값이 지금까지 나왔던 값들 범위 안에 있다면 무시한다. ( 거기에 있는 빗물은 이미 계산 했으니깐 )
            
    print(raindrop)

'''
5
30
20
30
10
30
== 30
'''
'''
7
0
20
1
3
40
3
0
==36
'''
'''
14
0
20
1
3
40
3
0
0
20
1
3
40
3
0
==249
'''
'''
15
0
2
0
0
3
0
0
0
0
6
0
0
2
0
0
== 20
'''