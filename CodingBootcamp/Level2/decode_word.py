# 입력하는 문자열이 주어지고, 그를 통해 디코딩 된 문자열을 반환
# 3 [a] 2 [bc] == aaabcbc
# 3[a2 [c]] == accaccacc
# abc 3[cd] xyz == abccdcdcdxyz

import sys

def number_decode(number, string_stack):
    return string_stack * number

def is_number(letter):
    return letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def is_alpha(letter):
    return letter in [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
    encode_str = sys.stdin.readline().rstrip()
    decoded_str = ""

    total_stack = []

    number_flag = False
    saved_number = 2

    for letter in encode_str:
        if letter == " ":
            continue
        if is_number(letter):
            # 숫자가 들어오면 Flag를 세워서 얼마나 반복할지 저장.
            number_flag = True
            saved_number = int(letter)
        elif is_alpha(letter):
            # 알파벳이면 숫자가 있는지 없는지 판단해서 stack에 저장.
            if number_flag:
                total_stack.append((saved_number, letter))
            else:
                total_stack.append((1, letter))
            number_flag = False
        elif letter == "[":
            # [ 가 나왔으면 일단 None 으로 저장.
            # 추후 ] 가 나왔을 때 반복 가능하게 숫자만 미리 저장.
            if number_flag:
                total_stack.append((saved_number, None))
            else:
                total_stack.append((1, None))
            number_flag = False
        elif letter == "]":
            # ] 가 나왔으면 저장했던 String 들을 쭉 훑으면서 String을 만들어 stack 에 저장.
            temp_decoded = ""
            while True:
                # 하나씩 pop 하면서 계산
                elements = total_stack.pop()
                # None 이 있는 것이 [ 가 시작한 부분.
                if elements[1] == None:
                    # (num, None) is returned. append (num, nowStrings) and break
                    total_stack.append((elements[0], temp_decoded))
                    break
                else:
                    # Stack 형식으로 뒤에서 부터 훑기 때문에, 이미 읽은 값이 뒤로 ( temp decoded ) 가야 한다.
                    temp_decoded = number_decode(elements[0], elements[1]) + temp_decoded
    
    for elements in total_stack:
        # Queue 형식으로 앞에서부터 훑기 떄문에 위와 더하는 방식이 다름.
        decoded_str = decoded_str + number_decode(elements[0], elements[1])

    print(decoded_str)