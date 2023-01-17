def count_primes(num):

    # Check for 0 or 1 input
    if num < 2:
        return 0

    # 2 or greater
    # Store our prime numbers 

    primes = [2]
    x = 3

    while x <= num:
        for y in range(3, x, 2):
            pass # unfinished 