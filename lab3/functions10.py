def unique(lst):
    answer = []
    for num in lst:
        if num not in answer:
            answer.append(num)
    return answer
lst = input()
lst = list(map(int, lst.split()))
print(unique(lst))
