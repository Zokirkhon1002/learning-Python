def is_palindrome(s):
    listfor = []
    for i in s:
        listfor.append(i)
    listfor.reverse()
    result = "".join(listfor)
    return s.lower() == result.lower();


print(is_palindrome("kiyik"))
print(is_palindrome("kiyiknoma"))