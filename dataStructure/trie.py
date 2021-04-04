import string
# Use \n for end of word.
EOW = '\n'
string_bank = string.ascii_letters + "0123456789-_;:!@#$%^&*=" + EOW

TREE_END = -1

def make_child():
    return [TREE_END for _ in range(len(string_bank))]

def add_word(trie_root, word):
    now = trie_root
    add_word = word + EOW
    for w in add_word:
        next_index = string_bank.index(w)
        if now[next_index] == TREE_END:
            now[next_index] = make_child()
        now = now[next_index]

def get_not_terminated(trie_leaf):
    result = []
    
    if trie_leaf == TREE_END:
        return result
    
    for tl in range(0, len(trie_leaf)):
        if trie_leaf[tl] != TREE_END:
            result.append(tl)
    return result

def get_now_root(trie_root, trie_stack):
    now = trie_root
    for ts in trie_stack:
        now = now[ts[1][ts[0]]]
    return now

def get_word(trie_stack):
    result = ""
    for ts in trie_stack:
        if ts[0] != -1:
            result += string_bank[ts[1][ts[0]]]
    return result

def show_all_word(trie_root):
    next_root = trie_root
    trie_stack = [(-1, get_not_terminated(next_root))] #(next_index, next_available_list)
    word_list = []

    while trie_stack:
        now = trie_stack[-1]
        del trie_stack[-1]
        now_index = now[0]
        now_candidate = now[1]

        # 자식 모두 검색했으면 종료.
        if now_index == len(now_candidate) - 1:
            if now_index == -1:
                word_list.append(get_word(trie_stack)[:-1])
            continue
        now_index += 1
        trie_stack.append((now_index, now_candidate))

        next_root = get_now_root(trie_root, trie_stack)
        next_candidate = get_not_terminated(next_root)
        trie_stack.append((-1, next_candidate))
    
    return word_list

def search_word(trie_root, word):
    sword = word + EOW
    now = trie_root
    for w in range(0, len(sword)):
        next_index = string_bank.index(sword[w])
        if now[next_index] != TREE_END:
            now = now[next_index]
        else:
            return False

    return len(get_not_terminated(now)) == 0

import random
import string
import time

WORD_MAX_SIZE = 150
DICTIONARY_SIZE = 1000

def make_random_string(string_length):
    result = ""
    for _ in range(string_length):
        result += random.choice(string_bank)
    return result

def get_pi_arr(word):
    # pi_arr[k] 는 길이 k + 1 ( K index ) 까지의 substring의 pi ( failure ) 값.
    pi_arr = [0 for _ in range(len(word))]
    # word[0:j] 의 prefix는 suffix와 동일함.
    j = 0

    for i in range(1, len(word)):
        while j != 0 and word[i] != word[j]:
            j = pi_arr[j - 1]

        if word[i] == word[j]:
            j += 1
            pi_arr[i] = j

    return pi_arr

def KMP_search(search_dest, word):
    pi_arr = get_pi_arr(word)
    j = 0

    for i in range(0, len(search_dest)):
        while j != 0 and search_dest[i] != word[j]:
            j = pi_arr[j - 1]
        
        if search_dest[i] == word[j]:
            j += 1
        
        if j == len(word):
            return i - j + 1
    return -1

def KMP_dictionary_search(word_list, word):
    for wordl in word_list:
        if len(wordl) == len(word):
            if KMP_search(wordl, word) >= 0:
                return True
    return False

if __name__ == "__main__":
    trie_root = make_child()

    word_list = [make_random_string(WORD_MAX_SIZE) for _ in range(DICTIONARY_SIZE)]
    search_dest = random.randint(0, DICTIONARY_SIZE - 1)

    start_time = time.time()
    for i in range(DICTIONARY_SIZE):
        add_word(trie_root, word_list[i])
    for i in range(DICTIONARY_SIZE):
        result = search_word(trie_root, word_list[i])
    end_time = time.time()
    print("TRIE :", end_time - start_time)
    print("RESULT :", result)

    start_time = time.time()
    for i in range(DICTIONARY_SIZE):
        result = KMP_dictionary_search(word_list, word_list[i])
    end_time = time.time()
    print("KMP :", end_time - start_time)
    print("RESULT :", result)