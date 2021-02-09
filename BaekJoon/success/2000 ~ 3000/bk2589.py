# https://www.acmicpc.net/problem/2589
import sys

def get_node_num_to_coord(n, width):
    w = n % width
    h = int(n / width)
    return (h, w)

def get_node_num(w, h, width,):
    return h * width + w

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    height = int(inp[0])
    width = int(inp[1])
    
    lw_map = [["" for _ in range(width)] for _ in range(height)]
    for h in range(height):
        inp = sys.stdin.readline().rstrip()
        for w in range(width):
            lw_map[h][w] = inp[w]

    link_map = [[False for _ in range(node_number)] for _ in range(node_number)]
    node_number = width * height
    dist_map = [[0 for _ in range(node_number)] for _ in range(node_number)]
    
    for h in range(height):
        for w in range(width):
            

    for n1 in range(node_number):
        for n2 in range(node_number):
            (h1, w1) = get_node_num_to_coord(n1, width)
            (h2, w2) = get_node_num_to_coord(n2, width)
            link_map[n1][n2]

    for n1 in range(node_number):
        for n2 in range(node_number):
            if link_map[n1][n2]:
                dist_map[n1][n2] = 1
                dist_map[n2][n1] = 1

    changed = False
    while not changed:
        changed = False
        for h in range(height):
            for w in range(width):
                if


