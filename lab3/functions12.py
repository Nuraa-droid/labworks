def histogram(lst):
    for num in lst:
        print("*" * num)
lst = input()
lst = list(map(int, lst.split()))
histogram(lst)