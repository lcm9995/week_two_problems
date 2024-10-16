def reverseWords(s):
    words_list = s.strip().split()
    words_list.reverse()
    for word in words_list:
        word.strip()
    res = " ".join(words_list)
    return res