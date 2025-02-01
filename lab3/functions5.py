def generate_permutations(word, current=""):
    if len(word) == 0:
        print(current)
        return
    
    for i in range(len(word)):
        char = word[i]
        remaining_word = word[:i] + word[i+1:]
        generate_permutations(remaining_word, current + char)

word = input()
generate_permutations(word)