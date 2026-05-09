# ✏️ Write a function called count_vowels that takes a string and returns how many vowels are in it.
# count_vowels("hello")        → 2
# count_vowels("python")       → 1
# count_vowels("aeiou")        → 5

# def count_vowels(vowels):
#     vow = "a,e,i,o,u"
#     for i in vowels:
#         if vowels == vow:
#             return vow
#     return vow
# print(count_vowels("hello"))


def count_vowels(word):
    vow = "aeiou"
    count = 0
    for i in word:
        if i in vow:  
            count = count + 1  
    return count
print(count_vowels("hellow"))