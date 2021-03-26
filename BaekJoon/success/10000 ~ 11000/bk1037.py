N = int(input())
inp = input().split(" ")
n_list = [int(inp[i]) for i in range(0, N)]
n_list.sort()

print(n_list[0] * n_list[N-1])