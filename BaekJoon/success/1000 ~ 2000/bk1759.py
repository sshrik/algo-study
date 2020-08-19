import sys

def print_list(arr):
    print("____________________________________________")
    for i in range(0, len(arr)):
        print(arr[i])

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    L = int(inp[0]) # 암호 길이
    C = int(inp[1]) # 문자 갯수
    consonant = []  # 자음
    vowel = []  # 모음
    
    alphabet = sys.stdin.readline().rstrip().split(" ")
    alphabet.sort()

    for alp in alphabet:
        if alp in ['a', 'e', 'i', 'o', 'u']:
            vowel.append(alp)
        else:
            consonant.append(alp)
    
    # passwords[n] = n + 1 길이의 passwords 들.
    # passwords[n][m] = alphabet[m] 으로 끝나는 n + 1 길이의 passwords
    string_length = 1
    passwords = [[[alp] for alp in alphabet]]

    # Password 모음 숫자만 세어두면 자음 숫자는 size에서 빼서 구할 수 있다.
    vowel_number = [[]]

    for p in passwords[0]:
        if p[0] in vowel:
            vowel_number[0].append([1])
        else:
            vowel_number[0].append([0])

    while string_length < L:
        passwords.append([[] for _ in range(0, C)])
        vowel_number.append([[] for _ in range(0, C)])
        
        # 이전에 있던 암호의 뒤에다가 암호를 이어 붙인다. 
        # 다만 이전의 글자보다 큰 글자만 붙일 수 있고 중복해서 붙일 수 없음..
        
        for i in range(0, C):
            for j in range(0, i):
                passwords[string_length][i] += [p + alphabet[i] for p in passwords[string_length - 1][j]]
                if alphabet[i] in vowel:
                    vowel_number[string_length][i] += [1 + v for v in vowel_number[string_length - 1][j]]
                else:
                    vowel_number[string_length][i] += [v for v in vowel_number[string_length - 1][j]]
        string_length += 1

    string_length -= 1
    # print_list(vowel_number)
    # print_list(passwords)
    
    password_candidates = []
    for i in range(0, C):
        for j in range(0, len(passwords[string_length][i])):
            # 만약 자음이 2개 미만이거나, 모음이 0개면 안됨.
            if string_length + 1 - vowel_number[string_length][i][j] > 1 and vowel_number[string_length][i][j] != 0:
                password_candidates.append(passwords[string_length][i][j])

    password_candidates.sort()
    for pc in password_candidates:
        print(pc)

'''
4 5
a e i o u

=> no

3 6
a b c d e f

'''