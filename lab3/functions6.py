def reverse():
    sentence = input()
    words = sentence.split()
    reversed = words[::-1]
    return ' '.join(reversed)
reversed_sent = reverse()
print(reversed_sent)