__author__ = 'greg'
# prompt the user for the number we are going to use and return that number
def get_input():
    number = int(input("Enter a number: "))
    return number

# loops through all numbers up to an including the one the user entered and passes each one as a parameter for is_prime(num)
# and print only the ones that are found to be prime
def get_primes(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)

# determines if the number passed as a parameter is prime or not; returns true if the given number is prime, false otherwise
def is_prime(num):
    prime = True
    for x in range(2, num):
        if num % x == 0:
            prime = False
    return prime


get_primes(get_input())
