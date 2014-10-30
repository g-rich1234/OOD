__author__ = 'greg'

def get_input():
    number = int(input("Enter a number: "))
    return number


def get_primes(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)


def is_prime(num):
    prime = True
    for x in range(2, num):
        if num % x == 0:
            prime = False
    return prime


get_primes(get_input())