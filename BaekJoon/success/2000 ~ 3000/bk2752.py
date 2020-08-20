import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    arr = [int(i) for i in inp]
    arr.sort()
    
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
        