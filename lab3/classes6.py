def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    
numbers = [10, 20, 17, 19, 15, 3, 7, 35]
primes = list(filter(lambda x: prime(x), numbers))

print(primes)