import time
from collections import deque

PUSH_POP_NUMBER = 100000

if __name__ == "__main__":
    start_time = time.time()
    arr = [i for i in range(20)]
    for i in range(PUSH_POP_NUMBER):
        arr.append(i)
    for i in range(PUSH_POP_NUMBER):
        arr.insert(0, i)
    for i in range(PUSH_POP_NUMBER):
        del arr[-1]
    for i in range(PUSH_POP_NUMBER):
        del arr[0]
    end_time = time.time()

    print("LIST take", (end_time - start_time) * 1000, "ms")

    start_time = time.time()
    dq = deque(range(20))
    for i in range(PUSH_POP_NUMBER):
        dq.append(i)
    for i in range(PUSH_POP_NUMBER):
        dq.appendleft(i)
    for i in range(PUSH_POP_NUMBER):
        dq.pop()
    for i in range(PUSH_POP_NUMBER):
        dq.popleft()
    end_time = time.time()

    print("deque take", (end_time - start_time) * 1000, "ms")

    '''
    start_time = time.time()
    head = [NOT_LINK, -1, NOT_LINK]
    for i in range(20):
        append(head, i)

    for i in range(INSERT_NUMBER):
        insert_loc = random.randint(0, 19 + i) 
        insert_at(head, insert_loc, i)
    end_time = time.time()

    print("LINKED LIST take", (end_time - start_time) * 1000, "ms")
    '''
