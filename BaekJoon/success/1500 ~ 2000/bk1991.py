# https://www.acmicpc.net/problem/1991
import sys
from collections import deque
fastio = sys.stdin.readline

def append_child(tree, root, left_child, right_child):
    root_index = tree.index(root)
    left_child_index = (root_index + 1) * 2 - 1
    right_child_index = (root_index + 1) * 2

    if right_child_index >= len(tree):
        temp = len(tree)
        for _ in range(temp, right_child_index + 1):
            tree.append(False)

    if left_child != ".":
        tree[left_child_index] = left_child
    if right_child != ".":
        tree[right_child_index] = right_child

def get_root_index(i):
    if i % 2 == 0:
        return (i // 2) - 1
    else:
        return (( i + 1 ) // 2) - 1

def get_right_child(i):
    return (i + 1) * 2

def get_left_child(i):
    return (i + 1) * 2 - 1

def front_order(tree, now):
    if tree[now] != False:
        print(tree[now], end="")
        front_order(tree, get_left_child(now))
        front_order(tree, get_right_child(now))


def middle_order(tree, now):
    if tree[now] != False:
        middle_order(tree, get_left_child(now))
        print(tree[now], end="")
        middle_order(tree, get_right_child(now))

def back_order(tree, now):
    if tree[now] != False:
        back_order(tree, get_left_child(now))
        back_order(tree, get_right_child(now))
        print(tree[now], end="")

if __name__ == "__main__":
    N = int(fastio().rstrip())
    tree = ["A"]

    for _ in range(N):
        inp = fastio().rstrip().split(" ")
        root = inp[0]
        lc = inp[1]
        rc = inp[2]

        append_child(tree, root, lc, rc)

    # print(tree)
    front_order(tree, 0)
    print("")
    middle_order(tree, 0)
    print("")
    back_order(tree, 0)
    print("")
