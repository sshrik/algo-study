# O(log (m + n))안에서 두개의 정렬된 배열의 중간 값을 반환하라.
# m, n 은 1000 이하이고, 각각은 -10^6 ~ 10^6 사이의 숫자.
import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    n = int(inp[0])
    m = int(inp[1])

    n_list = []
    m_list = []

    inp = sys.stdin.readline().rstrip().split(" ")
    for i in range(0, n):
        n_list.append(int(inp[i]))
    
    inp = sys.stdin.readline().rstrip().split(" ")
    for i in range(0, m):
        m_list.append(int(inp[i]))

    # Make sure n_list is shorter then m_list
    if m < n:
        temp = m
        m = n
        n = temp

        temp = m_list
        m_list = n_list
        n_list = temp

    answer = 0;

    max_index = n
    min_index = 0
    half = (m + n + 1) // 2
    
    while min_index <= max_index:
        i = (min_index + max_index) // 2    # n_list의 첫 half 에 들어갈 갯수
        j = half - i    # m_list의 첫 half에 들어갈 갯수 ( 처음에는 계산해보면 m+1 /2 가 된다. )
        if i < max_index and m_list[j-1] > n_list[i]:
            # 만약 m_list 의 예상 중간값이 n_list의 예상 중간값 + 1 (index) 보다 크다면, 
            # n_list의 첫 half에는 더 많이 들어가야함. ( 최소 i + 1 만큼은 )
            min_index = i + 1
        elif i > min_index and n_list[i - 1] > m_list[j]:
            # 만약 n_list의 예상 중간값이 m_list의 예상 중간값 + 1 (index) 보다 크다면, 
            # n_list의 첫 half에는 더 적게 들거아야 함. ( 최대 i - 1 만큼만 )
            max_index = i - 1
        else :
            # 만약 half / half가 잘 나눠졌다면,
            max_left = 0
            if i == 0:
                # 만약 n_list 첫 half에 아무것도 들어가지 않았다면,
                # 가장 작은 왼쪽 value는 m_list의 마지막값
                max_left = m_list[j-1]
            elif j == 0:
                # 만약 m_list 첫 half에 아무것도 들어가지 않았다면,
                # 가장 작은 왼쪽 value는 n_list의 마지막값
                max_left = n_list[i-1]
            else:
                # 두 배열의 첫 half 값의 맨 마지막 값중 더 큰걸 max_left로 설정.
                max_left = max([n_list[i-1], m_list[j-1]])
            
            # 두 배열의 길이의 합이 홀수개라면, 여기서 break 해도 좋음.
            if (m + n) % 2 == 1:
                answer = [max_left]
                break

            # 두 배열의 길이의 합이 짝수개면, 다음도 진행해서 2개를 return.
            min_right = 0
            if i == n:
                # 만약 n_list의 첫번쨰에 들어갈 길이가 n개라면, ( 전부 m_list의 조정된 중간값보다 작다면)
                # 가장 작은 2번째 배열의 값은 m_list의 처음
                min_right = m_list[j]
            elif j == m:
                # 만약 m_list의 첫번쨰에 들어갈 길이가 m개라면, ( 전부 n_list의 조정된 중간값보다 작다면 )
                # 가장 작은 2번째 배열의 값은 n_list의 처음
                min_right = n_list[i]
            else:
                # 두 배열의 두번째 half 값의 맨 처음 값중 더 작은걸 min_right 으로 설정.
                min_right = min(m_list[j], n_list[i])
            
            # 짝수개 이므로 2개를 return.
            answer = [max_left, min_right]
            break

    print(answer)


'''
6 8
1 3 5 7 9 10
2 4 6 8 9 10 11 12
'''