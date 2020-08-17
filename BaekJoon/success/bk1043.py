import sys

def contain_know_real(attendance, know_real):
    # 진실을 알고있는 사람이 있는지 return
    for i in range(0, len(attendance)):
        if know_real[attendance[i]]:
            return True
    return False

def check_attend_duplicate(attendance1, attendance2):
    # attendance1 에 있는 값이 2에도 있는지 확인.
    for a in attendance1:
        if a in attendance2:
            return True

    return False

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])  # 사람수
    M = int(inp[1])  # 파티수

    inp = sys.stdin.readline().rstrip().split(" ")
    A = int(inp[0])
    
    # 진실을 알고있는 사람의 리스트.
    know_real = [ False for _ in range(0, N) ]
    if A != 0:
        for i in range(1, len(inp)):
            know_real[int(inp[i]) - 1] = True
    
    # 참여 인원 정리.
    attendance = []
    for i in range(0, M):
        inp = sys.stdin.readline().rstrip().split(" ")
        attendance.append([ int(i) - 1 for i in inp[1:] ])
    
    # If party_graph (a, b) == True, 파티 a와 파티 b에는 같이 참석하는 사람이 있는 것.
    party_graph = [[False for _ in range(0, M)] for _ in range(0, M)]   # party_graph[i][i] 는 False로 둬서 나중에 체크하지 않도록 한다.

    # party_graph를 만든다.
    for i in range(0, M):
        for j in range(0, M):
            # 같이 참석하는 사람이 있는 경우에만 edge를 만들어줌.
            if i != j and not party_graph[i][j]:
                if check_attend_duplicate(attendance[i], attendance[j]):
                    party_graph[i][j] = True
                    party_graph[j][i] = True
    
    # graph들 중 진실을 알고있는 사람이 없는 graph 를 확인하자. graph 탐색만 하면 될듯.
    
    checked_party = [False for _ in range(0, M)] # 그래프 탐색 된 파티.
    lied_party = [True for _ in range(0, M)]    # 거짓말을 한 파티.
    party_queue = []

    # 거짓말 할 수 없는 파티들을 모두 확인.
    for i in range(0, M):
        if contain_know_real(attendance[i], know_real):
            party_queue.append(i)

    while len(party_queue) > 0:
        # 체크한 파티면 넘어간다.
        if checked_party[party_queue[0]]:
            del party_queue[0]
            continue

        # 연결되어 있는 파티는 모두 거짓말 불가능한 파티들.
        q_idx = party_queue[0]
        del party_queue[0]
        
        lied_party[q_idx] = False
        checked_party[q_idx] = True

        for i in range(0, M):
            if party_graph[q_idx][i] and not checked_party[i]:
                party_queue.append(i)

    answer = 0
    for i in range(0, M):
        if lied_party[i]:
            answer += 1
    print(answer)


'''
4 3
0
2 1 2
1 3
3 2 3 4

정답 : 3

9 6
1 1
4 1 2 3 7
3 2 3 4
3 2 3 5
2 5 6
2 7 8
2 1 9

정답 : 0

7 5
2 5 6
3 1 2 3
2 2 4
2 4 5
2 6 7
1 6


7 6
2 5 6
3 1 2 3
2 2 4
2 4 5
2 6 7
1 6
0 

1 4
1 1
0
0
0
0
'''