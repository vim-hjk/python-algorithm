def sieve_of_eratosthenes(num):
    for i in range(num + 1):
        arr[i] = i

    for i in range(2, num + 1):
        if arr[i] is not 0:
            prime_number.append(i)
        for j in range(2, (num // i) + 1):
            arr[i * j] = 0


num = int(input('N = '))
arr = [None] * (num + 1)
prime_number = []

sieve_of_eratosthenes(num)
print(prime_number)
print(len(prime_number))
