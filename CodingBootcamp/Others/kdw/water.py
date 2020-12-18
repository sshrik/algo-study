# 3-1. 빗물 잡기
# 입력 예시 : 0 1 0 2 1 0 1 3 2 1 2 1
land = list(map(int, input().split()))

top = max(land) #최대 높이를 구함
length = len(land)  #전체 길이를 구함

water = 0   #물의 양을 저장하기 위함
flag = 0    #벽을 만났는지 기록하기 위함

for i in range(top):
    flag = 0
    temp = 0
    for cur in range(length):
        if land[cur] == 0 and flag == 0:    #벽이 아니고 이전에 벽을 만나지 않은 경우
            continue
        elif land[cur] != 0 and flag == 0:  #벽이고 이전에 벽을 만나지 않은 경우
            land[cur] -= 1                  #다음 반복을 위해 벽의 높이를 낮춤
            flag = 1                        #벽을 만났음을 표시한다
        elif land[cur] == 0 and flag == 1:  #벽이 아니고 이전에 벽을 만난 경우
            temp += 1                       #물이 고여있음을 뜻하므로 임시로 저장
        elif land[cur] != 0 and flag == 1:  #벽이고 이전에 벽을 만난 경우
            land[cur] -= 1                  #다음 반복을 위해 벽의 높이를 낮춤
            water += temp                   #물이 고여있는 상황이므로 temp를 저장하여줌
            temp = 0  

print(water)