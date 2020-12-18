# 2-2. 간격 병합(일정 간격의 병합)
# 입력 예시: [[1, 3], [2, 6], [8, 10], [15, 18]]
import re
text = input()
text = re.split(r'[\[ \] , ]', text) #입력이 대괄호를 통해서 주어질 경우 구분하기 위함

array = []
temp = []
count = 0
for i in range(1, len(text) - 1):    
    if text[i].isdigit():
        temp.append(int(text[i]))
        count += 1
    if count == 2: #두개씩 묶어서 저장하기 위함
        array.append(list(temp))
        temp = []
        count = 0

array = sorted(array, key = lambda x: (x[0], x[1])) #첫 인자를 기준으로 정렬함

left = array[0][0]
right = array[0][1]
result = []

for dist in array:
    if dist[0] < right and dist[1] <= right: #두 값이 모두 기존값보다 작거나 같은 경우
        continue
    elif dist[0] <= right and dist[1] > right: #두 번째 인자가 기존 우측값보다 큰 경우
        right = dist[1]        
    elif dist[0] > right: #기존 범위를 벗어난 경우
        temp = [left, right]
        result.append(list(temp))
        left = dist[0]
        right = dist[1]        
    
temp = [left, right]
if temp not in result: #반복문이 종료되고 마지막 부분에서 기존 범위를 벗어난 경우 저장되지 못하므로 따로 저장하기 위함
    result.append(temp)

print(result)