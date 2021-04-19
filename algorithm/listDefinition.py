#https://poorman.tistory.com/411
import time

n = 10000
if __name__ == "__main__":
    strat_time = time.time()
    a = [([0] * n) for _ in range(n)]
    end_time = time.time()

    print("list * operation :", end_time - strat_time)
    
    strat_time = time.time()
    a = [[0 for _ in range(n)] for _ in range(n)]
    end_time = time.time()

    print("list for operation :", end_time - strat_time)
    