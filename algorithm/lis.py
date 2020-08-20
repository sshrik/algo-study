
def longest_increasing_subsequence_n_square(sequence):
    # sequence : 주어진 수열. 1차원 리스트의 형태이다. 최소 1개 이상임을 보장.
    D = [1 for _ in range(0, len(sequence))]
    D_contents = [str(s) for s in sequence]

    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                D[i] = D[j] + 1
                D_contents[i] = D_contents[j] + str(sequence[i])
    
    return max(D), D_contents[D.index(max(D))]

# 문제 해결 필요;;
def longest_increasing_subsequence_n_logn(sequence):
    # sequence : 주어진 수열. 1차원 리스트의 형태이다. 최소 1개 이상임을 보장.
    D = [1 for _ in range(0, len(sequence))]
    D_contents = [str(s) for s in sequence]
    X = [0] # 편의를 위해서 길이 length - 1 의 가장 큰 값의 Index 값을 가지게 변경.

    for i in range(1, len(sequence)):
        if sequence[X[-1]] < sequence[i]:
            D_contents[i] = D_contents[X[-1]] + str(sequence[i])
            D[i] = len(X) + 1
            X.append(i)
            continue
        for j in range(0, len(X)):
            if sequence[X[j]] > sequence[i]:
                if j != 0:
                    D_contents[i] = D_contents[X[j - 1]] + str(sequence[i])
                X[j] = i
                D[i] = j + 1
                break
    
    return len(X), D_contents[D.index(len(X))]

max_len, max_contents = longest_increasing_subsequence_n_logn([2, 3, 4, 5, 6, 1, 2, 3, 4, 5])
print(max_contents)
print(max_len)
max_len, max_contents = longest_increasing_subsequence_n_logn([5, 2, 1, 3, 4, 5, 1, 6])
print(max_contents)
print(max_len)