# https://www.acmicpc.net/problem/9019
import sys

FOUND = 1
NOT_FOUND = -1

def list_to_num(li):
    return li[0] * 1000 + li[1] * 100 + li[2] * 10 + li[3]

def num_to_list(num):
    return_list = []

    return_list.insert(0, num % 10)
    num = int(num / 10)

    return_list.insert(0, num % 10)
    num = int(num / 10)

    return_list.insert(0, num % 10)
    num = int(num / 10)

    return_list.insert(0, num % 10)
    num = int(num / 10)

    return return_list

def D(li):
    num = list_to_num(li)
    num = (num * 2) % 10000
    return num_to_list(num)

def S(li):
    num = list_to_num(li)
    num = num - 1 if num != 0 else 9999
    return num_to_list(num)

def L(li):
    temp_li = [i for i in li]
    li0 = temp_li[0]
    del temp_li[0]
    temp_li.append(li0)
    return temp_li

def R(li):
    temp_li = [i for i in li]
    li3 = temp_li[3]
    del temp_li[3]
    temp_li.insert(0, li3)
    return temp_li

def find_DSLR_seq(source, dest):
    li_source = num_to_list(source)
    now_queue = [("", li_source)]

    while now_queue:
        now_value = now_queue[0]
        del now_queue[0]

        next_list = check_next(now_value, dest)
        if next_list == FOUND:
            break
        else:
            now_queue += next_list
        # print(now_queue)

def check_next(source, dest):
    # source format : ("", digit_list), dest format : number
    next_list = []
    next_list.append((source[0] + "D", D(source[1])))
    next_list.append((source[0] + "S", S(source[1])))
    next_list.append((source[0] + "L", L(source[1])))
    next_list.append((source[0] + "R", R(source[1])))
    for nl in next_list:
        if list_to_num(nl[1]) == dest:
            print(nl[0])
            return FOUND
    return next_list

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for t in range(T):
        inp = sys.stdin.readline().rstrip().split(" ")
        find_DSLR_seq(int(inp[0]), int(inp[1]))
