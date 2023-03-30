# Napisz funkcję sprawdzającą czy podane liczby są  liczbami pierwszymi w szybszy sposób niż wprzykładzie. Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi. (10%)
import math


def prime(*args):
    for number in args:
        is_prime = True
        for i in range(2, math.floor(number ** 0.5)+1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")


if __name__ == '__main__':
    prime(0, 1, 2, 3, 4, 5)