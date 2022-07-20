def check_anagram(str1,str2):
    if len(str1) == len(str2):
        for ch in str1:
            if ch not in str2:
                return False
        return True
    else:
        return False

str1 = input("Enter word 1:")
str2 = input("Enter word 2:")

print("Words are anagram" if check_anagram(str1,str2) else "Words are not anagram")


