# https://www.acmicpc.net/problem/1922
import sys
NOT_LINK = sys.maxsize

def search_root(link_data, n):
    # Search n`th node`s root index.
    next = n

    while link_data[next] != next:
        next = link_data[next]
    
    return next

def set_root(link_data, n, root):
    next = n
    before = n

    while link_data[next] != next:
        before = next
        next = link_data[next]
        link_data[before] = root
    
    link_data[next] = root

if __name__ == "__main__":
    fastIO = sys.stdin.readline
    N = int(fastIO())
    M = int(fastIO())

    length_map = [[NOT_LINK for _ in range(N)] for _ in range(N)]
    length_list = []

    for _ in range(M):
        inp = fastIO().split(" ")
        x = int(inp[0]) - 1
        y = int(inp[1]) - 1
        length = int(inp[2])
        if length_map[x][y] > length:
            length_map[x][y] = length
            length_map[y][x] = length
    
    for x in range(N):
        for y in range(N):
            if x < y:
                if length_map[x][y] != NOT_LINK:
                    length_list.append((length_map[x][y], x + 1, y + 1)) 

    length_list.sort()
    link_data = [i for i in range(N + 1)]
    selected_link = []

    while len(selected_link) < N:
        if len(length_list) == 0:
            break

        now = length_list[0]
        del length_list[0]

        length = now[0]
        x = now[1]
        y = now[2]
        root_x = search_root(link_data, x)
        root_y = search_root(link_data, y)

        if root_x == root_y:
            # Make Cycle.
            set_root(link_data, x, root_x)
            set_root(link_data, y, root_y)
            continue

        # print("Link ", x, " and ", y)
        set_root(link_data, x, root_x)
        set_root(link_data, y, root_x)
        # print(link_data)
        selected_link.append(length)

    add_all = 0

    for sl in selected_link:
        add_all += sl

    print(add_all)



'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''