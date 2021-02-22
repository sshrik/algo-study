#KMP Algorithm

def get_suffix(word, n):
    return word[n:]

def get_prefix(word, n):
    return word[:n]

def get_pi_length(word):
		# Suffix와 Prefix 가 동일한 n 을 return 한다. 없으면 0, 있다면 index + 1 값을 return ( 길이를 return 해야 하기 때문 )
    wl = len(word)
    for i in range(0, int(wl / 2)):
        if get_prefix(word, i) == get_suffix(word, i):
            return i + 1
    return 0

def get_intersect(word, text, start_n):
		# text[start_n] 부터 시작해서 word와 겹치는 단어를 return. 
    interesct_word = ""
    for i in range(0, len(word)):
        if text[start_n + i] == word[i]:
            interesct_word += word[i]
        else:
            break
    return interesct_word

def kmp_search(word, text):
    tl = 0

    while tl < len(text):
        interesct_word = get_intersect(word, text, tl)
        if interesct_word == word:
            return tl
        else:
            # word가 나오지 않았다면 겹쳤던 단어의 pi_length를 구해서 해당 길이 전까지는 검색하지 않고 넘어감.
            pi_length = get_pi_length(interesct_word)
            tl += len(interesct_word) - pi_length

    return -1

if __name__ == "__main__":
    word = "acdecac"
    text = "acacdecacdeacdecacdecacaccac"

    print(kmp_search(word, text))