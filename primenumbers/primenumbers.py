__author__ = 'greg'


# prompt the user for the number we are going to use 
def main():
    #primenumbers is a Prime -tara
    primenumbers = Prime()
    #getting the user imput... -tar
    number = int(input("Enter a number: "))
    #list all prime numbers less than or equal to the user input -tara
    primenumbers.get_primes(number)
    

class Prime:
    ## this class finds all of the prime numbers up to and including the number entered by the uer
    
    def __init__(self):
        print("")
    
    
    # loops through all numbers up to an including the one the user entered and passes each one as a parameter for is_prime(num)
    # and print only the ones that are found to be prime
    def get_primes(self, n):
        for num in range(2, n + 1):
            if self.is_prime(num):
                print(num)
    
    
    # determines if the number passed as a parameter is prime or not; returns true if the given number is prime, false otherwise
    def is_prime(self, num):
        prime = True
        for x in range(2, num):
            if num % x == 0:
                prime = False
        return prime


main()
