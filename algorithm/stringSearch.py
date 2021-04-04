import random
import string
import time

STRING_SIZE = 1000000
WORD_MAX_SIZE = 10000
string_bank = string.ascii_letters + "0123456789-_;:!@#$%^&*="
#string_bank = "ABC"

def make_random_string(string_length):
    result = ""
    for _ in range(string_length):
        result += random.choice(string_bank)
    return result

def fast_naive_search(search_dest, word):
    word_size = len(word)
    for i in range(0, len(search_dest)):
        if search_dest[i: i + word_size] == word:
            return i
    return -1

def naive_search(search_dest, word):
    for i in range(0, len(search_dest)):
        for j in range(0, len(word)):
            if search_dest[i + j] == word[j]:
                if j == len(word) - 1:
                    return i 
            else:
                break
    return -1

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

def search_test(search_function):
    while True:
        search_dest = make_random_string(STRING_SIZE)
        word_size = random.randint(1, WORD_MAX_SIZE)
        start_loc = random.randint(0, STRING_SIZE - word_size)
        search_word = search_dest[start_loc:start_loc + word_size]

        find_loc = search_function(search_dest, search_word)
        if search_dest[find_loc: find_loc + word_size] != search_dest[start_loc: start_loc + word_size]:
            print(search_dest)
            print(search_word)
            print("Search Dest Length :", len(search_dest), "Search Word Length :", len(search_word))
            print("Search at", start_loc)  
            print("Find at :", find_loc)
            input()

BIG_PRIME = 10007

def get_2_pow(N):
    # Get 2^0 ~ 2^N-1 list
    power_2 = [1]
    for _ in range(1, N):
        power_2.append((power_2[-1] * 2) % BIG_PRIME)
    return power_2

def get_hash_value(str_value, power_2):
    hash_value = 0
    for i in range(0, len(str_value)):
        hash_value += (get_str_value(str_value[i]) * power_2[len(str_value) - 1 - i]) % BIG_PRIME
    return hash_value % BIG_PRIME

def get_str_value(char_value):
    return string_bank.index(char_value)

def rabin_karp_search(search_dest, word):
    power_2 = get_2_pow(len(word))
    dest_hash_value = get_hash_value(search_dest[:len(word)], power_2)
    word_hash_value = get_hash_value(word, power_2)
    next_index = len(word)

    while True:
        if dest_hash_value == word_hash_value:
            if search_dest[next_index - len(word):next_index] == word:
                return next_index - len(word)
        if next_index == len(search_dest):
            return -1
        
        dest_hash_value = (dest_hash_value - get_str_value(search_dest[next_index - len(word)]) * power_2[-1] ) * 2 + get_str_value(search_dest[next_index])
        dest_hash_value %= BIG_PRIME
        next_index += 1

if __name__ == "__main__":
    search_dest = make_random_string(STRING_SIZE)
    word_size = random.randint(1, WORD_MAX_SIZE)
    start_loc = random.randint(0, STRING_SIZE - word_size)
    search_word = search_dest[start_loc:start_loc + word_size]

    print("Search Dest Length :", len(search_dest), "Search Word Length :", len(search_word))
    print("Searcg at ", start_loc)

    now_time = time.time()
    find_loc = naive_search(search_dest, search_word)
    end_time = time.time()
    print("Naive Search : ", end_time - now_time)
    print("Find at :", find_loc, "Success :", find_loc == start_loc)
    
    now_time = time.time()
    find_loc = fast_naive_search(search_dest, search_word)
    end_time = time.time()
    print("FAST Naive Search : ", end_time - now_time)
    print("Find at :", find_loc, "Success :", find_loc == start_loc)

    now_time = time.time()
    find_loc = KMP_search(search_dest, search_word)
    end_time = time.time()
    print("KMP Search : ", end_time - now_time)
    print("Find at :", find_loc, "Success :", find_loc == start_loc)

    now_time = time.time()
    find_loc = rabin_karp_search(search_dest, search_word)
    end_time = time.time()
    print("Rabin Karp Search : ", end_time - now_time)
    print("Find at :", find_loc, "Success :", find_loc == start_loc)


    # print(KMP_search("BBBBAAAAACCBACBBBAACCCCABABAABAACABABABCBAACBCAACAABBBCCABAAABBBCCABCABCACCBBCABCCBCCBBCCBBBCBCAABCA", "ABABAB"))
    # print(KMP_search("ACAAACABBBACACCBCABCBABCCCACBCCCCBACBCCCAAACAACACAACCBBAAACCBCCCACAACCABBAACCBAAACABABCCCABBACABCACC", "CCCCBAC"))
    # print(KMP_search("BCCCBBAABCCBABCACBBACABCBCCBBCCBBCACCACABBCABCCAACCBABBBCCCBABBBCCBCBABBCAABACACCBCCACACABACACCBBBAA", "ACABBCAB"))
    # print(KMP_search("CABAAAABACCABBBBABBCCCABBBAABBBBABACCBACCBABBACAACBBBCABBCCABCABAACCACCCABCACACCCCACCACAACCBCAAAABBA", "CCCABBBA"))
    # print(KMP_search("ACACABABACAABACBABCBBAACCBBCBBCBBBBAACCAABBACBACCABAACCCCBABBAAAAACACCBACBBCBACCCABCCBABCBBBBBACBCBC", "ACBBCBACCCA"))
    # print(KMP_search("BCBCAABCACACABCBAACABAACCCCBABBBBACCBABBCBABCCCCABCCABCACAABCABBAAAABACBCAAAAABCAACCBCBBBBBACAAABBBA", "AAA"))
    # print(KMP_search("CAABCBCCBABABBBAABACAACAAABCCCBCBCACCBBAABCBCBCBAACBBBABAAACCCCCBBAACCACAAABCCBACBBBACCABCCBBBABAACC", "ABCBCBCBAAC"))
    # print(KMP_search("CBCBCBBBCCAAAABCBBCCCBAAABCAAACBAAABACACABACABCBACBCCBCBBCBCCBABAABBCBAABBCBACBCCBBCAACCCACACABAABBC", "BCBBCCC"))
    


    