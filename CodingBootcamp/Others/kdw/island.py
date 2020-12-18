# 2-1. 섬의 갯수
# 입력예시
# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 1
row = 4
col = 5

island = [] #지도를 저장하기 위한 리스트
position = [[0 for c in range(col)] for r in range(row)]    #지나왔는지를 판단하는 리스트

for i in range(row):
    island.append(list(map(int, input().split())))

count = 0   #섬의 갯수

def pangaea(posx, posy):    #섬 갯수 판별 함수
    if posx >= row or posy >= col:  #리스트 범위를 초과한 경우
        return 0
    elif position[posx][posy] == 1: #이미 지나친 경우
        return 0
    elif island[posx][posy] == 0:   #바다에 닿은 경우
        return 0
    
    if island[posx][posy] == 1 and position[posx][posy] == 0:   #우측과 아래로 진행하여 섬의 규모 파악
        pangaea(posx, posy + 1)   
        pangaea(posx + 1, posy)             
    
    position[posx][posy] = 1    #지나친 장소임을 표시
    return 1
  
for i in range(row):
    for j in range(col):
        value = pangaea(i, j)
        if value == 1:  #1이 반환된 경우에만 섬 하나를 탐색하고 왔음을 의미함
            count += 1
        
print(count)
