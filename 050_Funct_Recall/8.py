# Retrieved 2026-05-09, License - CC BY-SA 3.0

# def reverse(text):
#     if len(text) <= 1:
#         return text

#     return reverse(text[1:]) + text[0]
# print(reverse("how"))


def reverse_string(text):
    result = ""
    for i in text:
        result = i + result  
    return result
print(reverse_string("how"))