import collections

N = int(input())
dq = collections.deque(range(N, 0, -1))

while len(dq) != 1:
    dq.pop()
    a = dq.pop()        # pop() 은 뒤에서 제거, popleft() 는 앞에서 제거
    dq.appendleft(a)    # append(a) 는 뒤에서 추가, appendleft(a) 는 앞에서 추가
    # rotate(n) 은 요소들을 값만큼 회전. ex ) dq.rotate(3) -> 3만큼 뒤에서 앞으로 옴. 음수는 반대로
print(dq[0])