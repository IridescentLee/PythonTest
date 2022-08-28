

def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    words = sentence.split()
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i + 1
    return -1


"i am tired"
"you"

s1 = "i love eating burger"
s2 = "burg"

a = isPrefixOfWord(1, sentence=s1, searchWord=s2)
print(a)


# sentence = "i love eating burger"
#
# searchWord = "burg"
#
# print(sentence.split())
# words = sentence.split()
# searchWord = 'burg'
# for i in range(len(words) + 1):
#     if words[i].startswith(searchWord):
#         num = i + 1
#         print(num)
#         break