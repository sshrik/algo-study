import sys
# 문자열 중에서 한 글자를 삭제 할 수 있을 때 회문으로 만들 수 있는지 판단하시오.

# 문자 한개를 뺀 모든 문자열을 만들어서, Backtracking 하면서 is_mirror() 수행해도 좋을 것 같음.
# O(N * N/2) = O(N^2)
# 문자를 입력 받으면서 각 알파뱃의 갯수가 짝수개인지, 혹은 한개 빼서 짝수개가 가능한지, 만약 짝수개라먄 회문이 가능한지 체크.
# 만약 홀수개 중에서도 1개짜리가 있다면 그냥 빼고 하면 되겠지만, 홀수개가 3, 5 개가 된다면 하나씩 빼면서 Backtracking 해야 성공.

# string.ascii_lowercase 는 lowercase 알파벳을 의미.

import string


def is_pallindrome(pall_str, n):
    if n == 1:
        return True
    
    stack = pall_str[0:n//2]
    if n % 2 == 0:
        check = pall_str[n//2:]
    else:
        check = pall_str[n//2+1:]
    
    for index in range(0, n//2):
        if stack[index] != check[n//2 - index - 1]:
            return False
    return True

def check_odd(str_number):
    odd_num = 0
    ret_value = 0

    for index in range(0, len(str_number)):    
        if str_number[index] % 2 == 1:
            odd_num += 1
            ret_value = index
    
    return odd_num, ret_value

def check_index(pall_string, n, odd_str):
    ret_value = []

    for index in range(0, n):
        if pall_string[index] == odd_str:
            ret_value.append(index)
    
    return ret_value

if __name__ == "__main__" :
    # n for string size, pall_str for checked str.
    n = int(sys.stdin.readline().rstrip())
    pall_string = sys.stdin.readline().rstrip()
    str_candidate = []
    str_number = []

    for p in pall_string:
        if p not in str_candidate:
            str_candidate.append(p)
            str_number.append(1)
        else:
            str_number[str_candidate.index(p)] += 1
        
    odd_number, odd_str_index = check_odd(str_number)
    if odd_number > 1:
        print("Can Not Pallindrome!")
    elif odd_number == 0:
        print("Pallindrome!" if is_pallindrome(pall_string, n) else "Not Pallindrome!")
    else:
        # Backtracking
        odd_index = check_index(pall_string, n, str_candidate[odd_str_index])
        avialalbe = False
        for oi in odd_index:
            if is_pallindrome(pall_string[0:oi] + pall_string[oi+1:], n - 1):
                avialalbe = True
        print("Pallindrome!" if avialalbe else "Not Pallindrome!")
        