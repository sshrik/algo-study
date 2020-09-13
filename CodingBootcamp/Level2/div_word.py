# 띄어쓰기가 없는 단어의 기준을 정해주고 띄어쓰기를 만들어 주시오.
# "applepenapple", ["apple", "pen"] -> true
# 입력 문자열이 입력 단어들로만 구성 되는가?

import sys

def get_start_word(non_space_str, word_list, now_word_index):
    available_word = [] # Available word index list.
    now_using_index = 0 # Now using index at available word list.

    for index in range(0, n):
        if non_space_str.startswith(word_list[index], now_word_index):
            available_word.append(index)
    
    return available_word, now_using_index

if __name__ == "__main__":
    non_space_str = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    
    word_list = []
    for _ in range(0, n):
        word_list.append(sys.stdin.readline().rstrip())
    
    available_stack = []
    now_word_index = 0
    backtracing = False

    available_word, now_using_index = get_start_word(non_space_str, word_list, now_word_index)
    
    # 시작 가능한 단어가 있을 때, 단어 리스트 중에서 먼저 입력된 단어들 부터 시작.
    if len(available_word) != 0:
        available_stack.append((available_word, now_using_index))   # 시작 가능 단어와 현재 사용하고 있는 단어의 index 저장.
        now_word_index += len(word_list[available_word[now_using_index]])      # 그 단어의 길이만큼 시작 위치 증가.
    
    # Using back-tracking, check all word can be devided with given words.
    while len(available_stack) != 0:
        if backtracing:
            (available_word, now_using_index) = available_stack.pop()
            if now_using_index == len(available_word) - 1:
                # 만약 모든 단어를 다 썼다면, 한번 더 pop 해서 위로 올라감.
                now_word_index -= len(word_list[available_word[now_using_index]])      # 그 단어의 길이만큼 시작 위치 감소.
                continue
            else:
                now_word_index -= len(word_list[available_word[now_using_index]])      # 그 단어의 길이만큼 시작 위치 감소.
                now_using_index += 1
        else:
            available_word, now_using_index = get_start_word(non_space_str, word_list, now_word_index)

        # 시작 가능한 단어가 있을 때, 단어 리스트 중에서 먼저 입력된 단어들 부터 시작.
        if len(available_word) != 0:
            available_stack.append((available_word, now_using_index))   # 시작 가능 단어와 현재 사용하고 있는 단어의 index 저장.
            now_word_index += len(word_list[available_word[now_using_index]])      # 그 단어의 길이만큼 시작 위치 증가.
            backtracing = False
        else:
            backtracing = True
        # 만약 단어들로 non_space_str이 끝난다면 끝.
        if now_word_index == len(non_space_str):
            break
    
    if len(available_stack) != 0:
        print("success!")
        for avail in available_stack:
            print(word_list[avail[0][0]], end=" ")
    else:
        print("fail!")