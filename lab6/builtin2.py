def cnt_chars(s):
    uppers = sum(1 for char in s if char.isupper())
    lowers = sum(1 for char in s if char.islower())
    return uppers, lowers
s = input()
upper, lower = cnt_chars(s)
print("number of uppercase letters:", upper)
print("number of lowercase letters:", lower)