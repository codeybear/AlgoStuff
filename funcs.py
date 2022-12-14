"""Useful methods derived from project euler problems, based on Amazon interview advice"""
import math


def calc_radius(x: int, y: int):
    """Calculate the radius by a point marked on the radius"""
    return math.sqrt(x**2 + y**2)


def find_divisors(num):
    """Quick method of finding all the divisors"""
    divs = [1, num]

    for test_num in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % test_num == 0:
            divs.append(test_num)
            divs.append(num // test_num)

    divs = list(set(divs))

    return divs


def binets_formula(num):
    """Binet's Formula. Calculate the nth term of fibonacci"""
    # pre-calculate sqrt(5) as we use it 3 times
    sqrt5 = math.sqrt(5)

    term = int((((1 + sqrt5)**num - (1 - sqrt5)**num) / (2**num * sqrt5)))

    return term


def is_prime(num):
    """Check to see if this number is a prime number"""
    for num2 in range(2, int(math.sqrt(num)) + 1):
        if num % num2 == 0:
            return False

    return True


def find_prime_factors(target):
    """Find the factors of a number that are prime. Not optimised."""
    for num in range(2, target):
        if target % num == 0:
            if is_prime(num):
                print(num)


def find_combos(target):
    """Find the number of possible coin combinations for a specified target"""
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    table = [0] * (target + 1)
    table[0] = 1
  
    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            table[j] += table[j - coins[i]]
  
    print(table)
    return table[target]

def create_palindrome(inp, b, isOdd):
    n = inp
    palin = inp
  
    # checks if number of digits to be produced is odd or even
    # if odd then neglect the last digit of input when reversing
    if (isOdd):
        n = n // b
  
    # Creates palindrome by just appending reverse
    # of number to itself
    while (n > 0):
        palin = palin * b + (n % b)
        n = n // b
    return palin
  
def generate_palindromes(n):
    """Function to print decimal palindromic numbers up to n."""

    # Run two times for odd and even length palindromes
    for j in range(2):
        i = 1
        pall = 0

        while True:
            pall = create_palindrome(i, 10, j % 2)
            if pall > n: break
            print(pall)
            i = i + 1
  