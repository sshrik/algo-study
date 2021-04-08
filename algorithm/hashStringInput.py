import random
import string
import time

WORD_MAX_SIZE = 10
DICTIONARY_SIZE = 100000
INPUT_SIZE = DICTIONARY_SIZE * 1

# string_bank = string.ascii_letters + "0123456789-_;:!@#$%^&*="
EOW = "\n"
string_bank = string.ascii_uppercase
search_bank = string_bank + EOW

def make_random_string(string_length):
    result = ""
    for _ in range(string_length):
        result += random.choice(string_bank)
    return result

def is_prime(number):
    half_number = int(number ** 0.5)

    for i in range(2, half_number):
        if number % i == 0:
            return False
    return True

def find_over_prime(number):
    next_number = number + 1

    while not is_prime(next_number):
        next_number += 1
    return next_number

def naive_search(input_list):
    return_list = []
    return_cnt = []

    for il in input_list:
        if il in return_list:
            return_cnt[return_list.index(il)] += 1
        else:
            return_list.append(il)
            return_cnt.append(1)
    return return_list, return_cnt

STR_LEN = len(search_bank)
MAX_HASH_VALUE = find_over_prime(STR_LEN ** WORD_MAX_SIZE)

def calc_hash_value(word):
    hash_value = 0

    for w in word:
        hash_value *= STR_LEN
        hash_value += (string_bank.index(w) + 1)
        hash_value %= MAX_HASH_VALUE

    return hash_value

def hash_saerch(input_search):
    hash_table = [0 for _ in range(MAX_HASH_VALUE)]
    word_list = []
    word_cnt = 0
    
    for word in input_search:
        hash_value = calc_hash_value(word)
        if hash_table[hash_value] == 0:
            word_list.append(word)
            word_cnt += 1
        hash_table[hash_value] += 1
    
    return hash_table, word_list
TRIE_END = None

def make_trie_child():
    return_list = [TRIE_END for _ in range(len(search_bank) - 1)]
    return_list.append(-1)
    return return_list

def trie_add(trie_root, word, word_cnt):
    now_root = trie_root
    for w in range(0, len(word)):
        if now_root[search_bank.index(word[w])] == None:
            now_root[search_bank.index(word[w])] = make_trie_child()
        if w != len(word) - 1:
            now_root = now_root[search_bank.index(word[w])]
    now_root[-1] = word_cnt

def trie_index(trie_root, word):
    now_root = trie_root
    for w in word:
        if now_root[search_bank.index(w)] == None or now_root[search_bank.index(w)] == -1:
            return -1
        now_root = now_root[search_bank.index(w)]
    if now_root == -1:
        return -1
    return now_root

def trie_search(word_list):
    trie_root = make_trie_child()
    word_cnt = 0
    result_list = []
    result_count = []

    for word in word_list:
        ind = trie_index(trie_root, word + EOW)
        if ind < 0:
            trie_add(trie_root, word + EOW, word_cnt)
            result_list.append(word)
            result_count.append(1)
            word_cnt += 1
        else:
            result_count[ind] += 1
    return trie_root, result_list, result_count

if __name__ == "__main__":
    word_dest = random.randint(0, DICTIONARY_SIZE)
    word_dest = DICTIONARY_SIZE
    word_list = [make_random_string(WORD_MAX_SIZE) for _ in range(word_dest)]
    input_dest = random.randint(DICTIONARY_SIZE, INPUT_SIZE)
    input_dest = INPUT_SIZE
    input_list = [word_list[random.randint(0, word_dest - 1)] for _ in range(input_dest)]
    
    print("Word List Length :", word_dest, "Input Length :", input_dest)

    now = time.time()
    #naive_list, naive_cnt = naive_search(input_list)
    end = time.time()
    print("Naive Search :", end - now, "ms")

    now = time.time()
    trie_root, trie_list, trie_count = trie_search(input_list)
    end = time.time()
    print("Trie Search :", end - now, "ms")
    
    now = time.time()
    hash_table, hash_list = hash_saerch(input_list)
    end = time.time()
    print("Hash Search :", end - now, "ms")

    print(len([]), len(trie_list), len(hash_list))