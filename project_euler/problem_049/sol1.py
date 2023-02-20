"""
Prime permutations

Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of
the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Solution:

First, we need to generate all 4 digits prime numbers. Then greedy
all of them and use permutation to form new numbers. Use binary search
to check if the permutated numbers is in our prime list and include
them in a candidate list.

After that, bruteforce all passed candidates sequences using
3 nested loops since we know the answer will be 12 digits.
The bruteforce of this solution will be about 1 sec.
"""

import math
from itertools import permutations



def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).

    A number is prime if it has exactly two factors: 1 and itself.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(87)
    False
    >>> is_prime(563)
    True
    >>> is_prime(2999)
    True
    >>> is_prime(67483)
    False
    """

    if 1 < number < 4:
        # 2 and 3 are primes
      
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(math.sqrt(number) + 1), 6):
      
        if number % i == 0 or number % (i + 2) == 0:
            
            return False
    return True


def search(target: int, prime_list: list) -> bool:
    """
    function to search a number in a list using Binary Search.
    >>> search(3, [1, 2, 3])
    True
    >>> search(4, [1, 2, 3])
    False
    >>> search(101, list(range(-100, 100)))
    False
    """

    left, right = 0, len(prime_list) - 1
    while left <= right:
        
        middle = (left + right) // 2
        if prime_list[middle] == target:
           
            return True
        elif prime_list[middle] < target:
            left = middle + 1
            
        else:
            right = middle - 1
            

    return False


def solution():
    """
    Return the solution of the problem.
    >>> solution()
    296962999629
    """
    prime_list = [n for n in range(1001, 10000, 2) if is_prime(n) ]
    candidates = []

    for number in prime_list:
        # branch 0
        brachsett(0)

        tmp_numbers = []

        for prime_member in permutations(list(str(number))):
            prime = int("".join(prime_member))
            # branch 1
            brachsett(1)
            if prime % 2 == 0:
                # branch 2
                brachsett(2)
                continue

            if search(prime, prime_list):
                # branch 3
                brachsett(3)
                tmp_numbers.append(prime)

        tmp_numbers.sort()
        if len(tmp_numbers) >= 3:
            # branch 4
            brachsett(4)
            candidates.append(tmp_numbers)

    passed = []
    for candidate in candidates:
        length = len(candidate)
        found = False
        #branch 5
        brachsett(5)
        for i in range(length):
            # branch 6
            brachsett(6)
            for j in range(i + 1, length):
                # branch 7
                brachsett(7)
                for k in range(j + 1, length):
                    # branch 8
                    brachsett(8)
                    if (
                        abs(candidate[i] - candidate[j])
                        == abs(candidate[j] - candidate[k])
                        and len({candidate[i], candidate[j], candidate[k]}) == 3
                    ):
                    # branch 9
                        brachsett(9)
                        passed.append(
                            sorted([candidate[i], candidate[j], candidate[k]])
                        )
                        found = True

                    if found:
                        #branch 10
                        brachsett(10)
                        break
                if found:
                    # branch 11
                    brachsett(11)
                    break
            if found:
                # branch 12
                brachsett(12)
                break

    answer = set()
    for seq in passed:
        answer.add("".join([str(i) for i in seq]))

    return max(int(x) for x in answer)



check =[0]*21
def brachsett(i):
    check[i] = 1 

if __name__ == "__main__":
    print(solution())
    

    counter = 0
    for i in range(13):
        if check[i]==1:
            counter += 1
    print(counter/13*100)
