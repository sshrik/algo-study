'''
EOW = "\n"
EMPTY = -1
word_bank = string.ascii_lowercase + EOW

def make_word_child():
    return [EMPTY for _ in range(len(word_bank))]

def insert_word(word_dict, word, index):
    now = word_dict
    dest = word
    for w in dest:
        now_indx = word_bank.index(w)
        if now[now_indx] == -1:
            now[now_indx] = make_word_child()
        now = now[now_indx]
    now[-1] = index

def search_word(word_dict, word):
    now = word_dict
    dest = word + '\n'
    for w in dest:
        now_indx = word_bank.index(w)
        if now[now_indx] == -1:
            return -1
        now = now[now_indx]
    return now
    
if __name__ == "__main__":
    word_dict = make_word_child()
    word_index = []
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    for n in range(N):
        word = fastio().rstrip()
        insert_word(word_dict, word.lower(), n + 1)
        word_index.append(word)

    for m in range(M):
        inp = fastio().rstrip()
        if inp[0] in string.ascii_uppercase:
            print(search_word(word_dict, inp.lower()))
        else:
            print(word_index[int(inp) - 1])
'''
'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''
# https://www.acmicpc.net/problem/1620
import sys
import string
import bisect
fastio = sys.stdin.readline

if __name__ == "__main__":
    word_index = []
    word_dict = []
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    for n in range(N):
        word = fastio().rstrip()
        word_index.append(word)
        word_dict.append((word, n + 1))
    word_dict.sort()

    for m in range(M):
        inp = fastio().rstrip()
        if inp[0] in string.ascii_uppercase:
            indx = bisect.bisect(word_dict, (inp, N + 1)) - 1
            print(word_dict[indx][1])
        else:
            print(word_index[int(inp) - 1])

