def checkPrime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
    return True

def twinPrime(max_num):
    """
    Generates the list of twin primes
    """
    for first_num in range(2, max_num):
        second_num = first_num + 2
        if (checkPrime(first_num) and checkPrime(second_num)):
            print(" {0} and {1}".format(first_num, second_num))

print("Twin Prime: ")
twinPrime(1000)
