# https://www.acmicpc.net/problem/1764
import string
EOW = "\n"
word_bank = string.ascii_lowercase + EOW

import sys
fastio = sys.stdin.readline

def trie_node():
    return [-1] * len(word_bank)

def trie_add(root, word):
    now = root

    for w in word:
        if now[word_bank.index(w)] == -1:
            now[word_bank.index(w)] = trie_node()
        now = now[word_bank.index(w)]
    
def trie_search(root, word):
    now = root

    for w in word:
        if now[word_bank.index(w)] == -1:
            return False
        now = now[word_bank.index(w)]
    
    return now == trie_node()

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    root = trie_node()
    for _ in range(N):
        word = fastio().rstrip()
        trie_add(root, word+EOW)
    
    res_list = []
    for _ in range(M):
        word = fastio().rstrip()
        if trie_search(root, word + EOW):
            res_list.append(word)
    res_list.sort()
    print(len(res_list))
    for rl in res_list:
        print(rl)

'''
4 5
a
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
a
'''