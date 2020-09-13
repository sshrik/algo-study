# 배열이 주어지면 0을 맨 뒤로 정렬하고 다른 수는 순서를 유지해야 한다.
# 배열 튜플등 복사본을 만들지 않고 수행하십시오.
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = []
    zeroNum = 0
    inputFlag = True
    # 0 이면 입력 안하고, 0이 아니면 insertion sort로 진행.
    for _ in range(0, n):
        a = int(sys.stdin.readline().rstrip())
        if a == 0:
            zeroNum += 1
        else:
            for i in range(0, len(arr)):
                if arr[i] > a:
                    arr.insert(i, a)
                    inputFlag = False
                    break
            if inputFlag:
                arr.append(a)
            else:
                inputFlag = True
    
    for i in range(0, n - zeroNum):
        print(arr[i])
    for i in range(0, zeroNum):
        print("0")