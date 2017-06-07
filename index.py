import math

def divisors(number):
    """ Returns list of all divisors of number """
    alld = []
    for i in range(1, number // 2 +1): #round(math.sqrt(number))+2
        if number % i == 0:
            alld.append(i)

    #print(number, alld)
    return alld

def binary_1(number):
    """ Returns number of 1s in binary expansion of the number """
    count = 0
    while number > 0:
        if number % 2 == 1:
            count = count + 1
        number = number // 2
    return count

def seq(sequence, method, val, err):
    """ Asserts/tests sequence of numbers using method """
    for element in sequence:
        assert(method(element)) is val, "Number: "+str(element)+" <- "+err

'''
HAPPY

Definition: One can take the sum of the squares of the digits of a number.
Those numbers are happy for which iterating this operation eventually
leads to 1.
First ten: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44
There are 1441 happy numbers below 10,000.
'''

def happy(number):
    """ Returns True if number is happy """
    #print("start", number)
    while True:
        num = 0
        while number > 0:
            num = num + (number % 10) ** 2
            number = number // 10

        #print("num", num)
        if num == 1:
            return True
        elif num < 10:
            return False
        else:
            number = num



def test_happy():
    """ Tests happy method """
    seq([1, 7, 10, 13, 19, 23, 28, 31, 32, 44], happy, True,
        "happy number from test sequence is not happy")
    seq([2, 8, 11, 14, 20, 22, 29, 33, 34, 45], happy, False,
        "not happy number is happy")


'''
LUCKY

Definition: To build the lucky number sequence, start with natural numbers. 
Delete every second number, leaving 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ... . 
The second number remaining is 3, so delete every third number, leaving 1, 3, 7, 9, 13, 15, 19, 21, ... . 
The next number remaining is 7, so delete every 7th number, leaving 1, 3, 7, 9, 13, 15, 21, ... . 
The next number remaining is 9, so delete every ninth number, etc.
Those numbers were lucky they weren't crossed out.
First ten: 1, 3, 7, 9, 13, 15, 21, 25, 31, 33
There are 1118 lucky numbers below 10,000.

Another definition: https://en.wikipedia.org/wiki/Lucky_number
'''


def lucky(number):
    """ Returns True if number is lucky """

    #odd numbers are unlucky
    if number % 2 == 0:
        return False

    sequence = [1]*(number+1)
    for i in range(len(sequence)):
        #zero out all even numbers
        if i % 2 == 0:
            sequence[i] = 0

    #print(sequence)

    position = 2
    unlucky = 0
    while unlucky < number and position < number:
        count = 0
        #find unlucky number
        for i in range(len(sequence)):
            if sequence[i] == 1:
                count = count +1
            if count == position:
                unlucky = i
                break
        #print("unlucky", unlucky)

        #prune sequence of unlucky-divisible positions
        count = 0
        for i in range(len(sequence)):
            if sequence[i] == 1:
                count = count + 1
            if count == unlucky:
                sequence[i] = 0
                count = 0

        #print(sequence)
        position = position + 1
        #print("position", position)

        #if number was eliminated already then it is unlucky
        if sequence[number] == 0:
            return False


    '''
    for i in range(len(sequence)):
        if sequence[i] == 1:
            print("lucky", i) 
    exit()
    '''

    return sequence[number] == 1


def test_lucky():
    """ Tests lucky method """
    seq([1, 3, 7, 9, 13, 15, 21, 25, 31, 33], lucky, True,
        "lucky number from test sequence is not lucky")
    seq([2, 4, 8, 10, 14, 16, 23, 27, 34, 36], lucky, False,
        "not lucky number is lucky")


'''
PERFECT

Definition: The number n is perfect if the sum of all its positive divisors except itself is equal to n.
Less than perfect numbers are called deficient, too perfect -- abundant.
First ten: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 
2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216
There are 4 perfect numbers below 10,000.
'''

def perfect(number):
    """ Returns True if number is perfect """
    return sum(divisors(number)) == number

def test_perfect():
    """ Tests perfect method """
    seq([6, 28, 496, 8128], perfect, True,
        "perfect number from test sequence is not perfect")
    '''
    seq([6, 28, 496, 8128, 33550336, 8589869056, 137438691328,
         2305843008139952128, 2658455991569831744654692615953842176,
         191561942608236107294793378084303638130997321548169216], perfect, True,
        "perfect number from test sequence is not perfect")
    '''
    seq([2, 4, 8, 10, 14, 16, 23, 27, 34, 36], perfect, False,
        "not perfect number is perfect")

'''
DEFICIENT

Definition: The number n is deficient if the sum of all its positive divisors except itself is less than n.
Compare with perfect and abundant numbers.
First ten: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11
There are 7508 deficient numbers below 10,000.
'''

def deficient(number):
    """ Returns True if number is perfect """
    return sum(divisors(number)) < number

def test_deficient():
    """ Tests deficient method """
    seq([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], deficient, True,
        "deficient number from test sequence is not deficient")
    seq([6, 12, 18, 20, 24, 30, 36, 40, 42, 48, 54], deficient, False,
        "not deficient number is deficient")

'''
ABUNDANT

Definition: The number n is abundant if the sum of all its positive divisors except itself is more than n.
They are abundant above perfection, not to mention deficiency. See perfect and deficient numbers.
First ten: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54
There are 2487 abundant numbers below 10,000.
'''

def abundant(number):
    """ Returns True if number is abundant """
    return sum(divisors(number)) > number

def test_abundant():
    """ Tests abundant method """
    seq([12, 18, 20, 24, 30, 36, 40, 42, 48, 54], abundant, True,
        "abundant number from test sequence is not abundant")
    seq([6, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11], abundant, False,
        "not abundant number is abundant")


'''
FIBONACCI

Definition: Fibonacci numbers are numbers that form the Fibonacci sequence. The Fibonacci sequence is defined as starting with 1, 1 and then each next term is the sum of the two preceding ones.
Fibonacci numbers are very common in nature. For example, a pineapple has 8 spirals if you count one way, and 13 if you count the other way.
First ten: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
There are 19 different Fibonacci numbers below 10,000.
'''

def fibonacci(number):
    """ Returns True if number is fibonacci """
    
    if number == 1:
        return True

    f1 = 1
    f2 = 2
    while f2 < number:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    return f2 == number

def test_fibonacci():
    """ Tests fibonacci method """
    seq([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], fibonacci, True,
        "fibonacci number from test sequence is not fibonacci")
    seq([6, 7, 9, 10, 11], fibonacci, False,
        "not fibonacci number is fibonacci")


'''
PRIME

Definition: A prime is a positive integer greater than 1 that is divisible by no positive integers other than 1 and itself.
Prime numbers are opposite to composite numbers.
First ten: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
There are 1229 primes below 10,000.
'''

def prime(number):
    """ Returns True if number is prime """
    if number == 1:
        return False
    if number == 2:
        return True
    
    #print(list(range(2, round(math.sqrt(number))+1)))
    for i in range(2, round(math.sqrt(number))+1):
        if number % i == 0:
            #print(number, i)
            return False

    return True

def test_prime():
    """ Tests fibonacci method """
    seq([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], prime, True,
        "prime number from test sequence is not prime")
    seq([4, 6, 8, 9, 12, 14, 15, 16, 18, 20], prime, False,
        "not prime number is prime")



'''
TRIANGULAR

Definition: If you start with n points on a line, then draw n-1 points above and between, then n-2 above and between them, and so on, you will get a triangle of points. The number of points in this triangle is a triangle number.
Compare to square, pentagonal and tetrahedral numbers.
First ten: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
There are 140 triangular numbers below 10,000.

Test method: http://mathforum.org/library/drmath/view/57162.html
'''

def triangular(number):
    """ Returns True if number is triangular """
    if number == 1:
        return True
    root = round(math.sqrt(number*2))

    print(number, root)

    return root * (root+1) == 2 * number or root * (root-1) == 2 * number

def test_triangular():
    """ Tests triangular method """
    seq([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], triangular, True,
        "triangular number from test sequence is not triangular")
    seq([4, 8, 9, 12, 14, 16, 18, 20], triangular, False,
        "not triangular number is triangular")



'''
SQUARE

Definition: The number n is a square if it is the square of an integer.
First ten: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
There are 99 squares below 10,000.
'''

def square(number):
    """ Returns True if number is square """
    if number == 1:
        return True
    root = round(math.sqrt(number))

    return root**2 == number

def test_square():
    """ Tests square method """
    seq([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], square, True,
        "square number from test sequence is not square")
    seq([8, 12, 14, 18, 20], square, False,
        "not square number is square")


'''
CUBE

Definition: The number n is a cube if it is the cube of an integer.
First ten: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000
There are 21 cube numbers below 10,000.
'''

def cube(number):
    """ Returns True if number is cube """
    if number == 1:
        return True
    root = round(number ** (1. / 3))

    return root**3 == number

def test_cube():
    """ Tests cube method """
    seq([1, 8, 27, 64, 125, 216, 343, 512, 729, 1000], cube, True,
        "cube number from test sequence is not cube")
    seq([4, 9, 16, 25, 36, 49, 81, 100], cube, False,
        "not cube number is cube")



'''
ODD

Definition: A number is odd if it is not divisible by 2.
Numbers that are not odd are even. Compare with another pair -- evil and odious numbers.
First ten: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
There are 5000 odd numbers below 10,000.
'''

def odd(number):
    """ Returns True if number is odd """

    return number % 2 == 1

def test_odd():
    """ Tests odd method """
    seq([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], odd, True,
        "odd number from test sequence is not odd")
    seq([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], odd, False,
        "not odd number is odd")



'''
EVEN

Definition: A number is even if it is divisible by 2.
Numbers that are not even are odd. Compare with another pair -- evil and odious numbers.
First ten: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
There are 4999 even numbers below 10,000.
'''

def even(number):
    """ Returns True if number is even """

    return number % 2 == 0

def test_even():
    """ Tests even method """
    seq([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], even, True,
        "even number from test sequence is not even")
    seq([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], even, False,
        "not even number is even")

'''
REPUNIT

Definition: A repunit is an integer in which every digit is one.
The term repunit comes from combining "repeated" and "unit".
First ten: 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111
There are 4 repunits below 10,000.
'''

def repunit(number):
    """ Returns True if number is repunit """
    while number > 9:
        if number % 10 != 1:
            return False
        else:
            number = number // 10
    return number == 1

def test_repunit():
    """ Tests repunit method """
    seq([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111], repunit, True,
        "repunit number from test sequence is not repunit")
    seq([3, 5, 7, 9, 13, 15, 17, 19], repunit, False,
        "not repunit number is repunit")

'''
LAZY CATERER

Definition: The n-th lazy caterer number is the maximum number of pieces a (circular) pizza can be cut into with n (straight-line) cuts.
Unlike the situation with cake, everybody gets the toppings.
First ten: 2, 4, 7, 11, 16, 22, 29, 37, 46, 56
There are 140 lazy caterer numbers below 10,000.

Formula: https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence
'''

def lazy_caterer(number):
    """ Returns True if number is lazy_caterer """
    # n-th lazy caterer number is (n**2 + n + 2) / 2

    n = 1
    while True:
        p = (n**2 + n + 2) / 2
        if p == number:
            return True
        elif p > number:
            return False
        n = n + 1

def test_lazy_caterer():
    """ Tests lazy_caterer method """
    seq([2, 4, 7, 11, 16, 22, 29, 37, 46, 56], lazy_caterer, True,
        "lazy_caterer number from test sequence is not lazy_caterer")
    seq([3, 5, 9, 13, 15, 17, 19], lazy_caterer, False,
        "not lazy_caterer number is lazy_caterer")


'''
ODIOUS

Definition: The number n is odious if it has an odd number of 1's in its binary expansion.
Guess what evil numbers are.
First ten: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19
There are 5000 odious numbers below 10,000.
'''

def odious(number):
    """ Returns True if number is odious """
    return odd(binary_1(number))

def test_odious():
    """ Tests odious method """
    seq([1, 2, 4, 7, 8, 11, 13, 14, 16, 19], odious, True,
        "odious number from test sequence is not odious")
    seq([3, 5, 6, 9, 10, 12, 15, 17, 18, 20], odious, False,
        "not odious number is odious")


'''
EVIL

Definition: The number n is evil if it has an even number of 1's in its binary expansion.
Guess what odious numbers are.
First ten: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20
There are 4999 evil numbers below 10,000.
'''

def evil(number):
    """ Returns True if number is evil """
    return even(binary_1(number))

def test_evil():
    """ Tests evil method """
    seq([3, 5, 6, 9, 10, 12, 15, 17, 18, 20], evil, True,
        "evil number from test sequence is not evil")
    seq([1, 2, 4, 7, 8, 11, 13, 14, 16, 19], evil, False,
        "not evil number is evil")



'''
UNDULATING

Definition: Undulating numbers are numbers of the form abababab... in base 10.
This property is significant starting from 3-digit numbers, so we will not consider numbers below 100.
First ten: 101, 111, 121, 131, 141, 151, 161, 171, 181, 191
There are 180 undulating numbers below 10,000.
'''

def undulating(number):
    """ Returns True if number is undulating """
    if number < 100:
        return False
    number = str(number)
    for idx in range(len(number)-2):
        if number[idx] != number[idx+2]:
            return False

    return True

def test_undulating():
    """ Tests undulating method """
    seq([101, 111, 121, 131, 141, 151, 161, 171, 181, 191], undulating, True,
        "undulating number from test sequence is not undulating")
    seq([1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 345, 1234], undulating, False,
        "not undulating number is undulating")

'''
TWIN

Definition: A prime number is called a twin prime if there exists another prime number differing from it by 2.
First ten: 3, 5, 7, 11, 13, 17, 19, 29, 31, 41
There are 409 twin primes below 10,000.
'''

def twin(number):
    """ Returns True if number is twin """
    if number < 3:
        return False

    if not prime(number):
        return False

    return prime(number - 2) or prime(number + 2)

def test_twin():
    """ Tests twin method """
    seq([3, 5, 7, 11, 13, 17, 19, 29, 31, 41], twin, True,
        "twin number from test sequence is not twin")
    seq([1, 2, 4, 8, 14, 16, 15, 21], twin, False,
        "not twin number is twin")



'''
TETRAHEDRAL (PYRAMIDAL)

Definition: A tetrahedral number is the number of balls you can put in a triangular pyramid.
This is the space generalization of triangular and square numbers.
First ten: 1, 4, 10, 20, 35, 56, 84, 120, 165, 220
There are 38 tetrahedral numbers below 10,000.

Formula: https://en.wikipedia.org/wiki/Tetrahedral_number
'''

def tetrahedral(number):
    """ Returns True if number is tetrahedral """
    # n-th tetrahedral number is n * (n + 1) * (n + 2) / 6

    n = 1
    while True:
        p = n * (n + 1) * (n + 2) / 6
        if p == number:
            return True
        elif p > number:
            return False
        n = n + 1

def test_tetrahedral():
    """ Tests tetrahedral method """
    seq([1, 4, 10, 20, 35, 56, 84, 120, 165, 220], tetrahedral, True,
        "tetrahedral number from test sequence is not tetrahedral")
    seq([3, 5, 9, 13, 15, 17, 19], tetrahedral, False,
        "not tetrahedral number is tetrahedral")


'''
PRONIC (HETEROMECIC)

Definition: The number is called pronic if it is the product of two consecutive numbers.
They are twice triangular numbers.
First ten: 2, 6, 12, 20, 30, 42, 56, 72, 90, 110
There are 99 pronic numbers below 10,000.
'''

def pronic(number):
    """ Returns True if number is pronic """

    root = round(math.sqrt(number))

    return root * (root + 1) == number or root * (root - 1) == number

def test_pronic():
    """ Tests pronic method """
    seq([2, 6, 12, 20, 30, 42, 56, 72, 90, 110], pronic, True,
        "pronic number from test sequence is not pronic")
    seq([3, 5, 9, 13, 15, 17, 19], pronic, False,
        "not pronic number is pronic")


'''
PRIMORIAL

Definition: The p-primorial is the product of all primes less than or equal to p. It is sometimes denoted by p#.
Compare to compositorials and factorials.
First ten: 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230
There are 5 primorials below 10,000.
'''

def primorial(number):
    """ Returns True if number is primorial """
    product = 1
    n = 1
    while True:
        if prime(n):
            product = product * n

        if product == number:
            return True
        elif product > number:
            return False
        n = n + 1


def test_primorial():
    """ Tests primorial method """
    seq([2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230], primorial, True,
        "primorial number from test sequence is not primorial")
    seq([3, 5, 9, 13, 15, 17, 19], primorial, False,
        "not primorial number is primorial")


'''
PALINDROME

Definition: A palindrome is a number that reads the same forward or backward.
First ten: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
There are 198 palindromic numbers below 10,000.
'''

def palindrome(number):
    """ Returns True if number is palindrome """
    number = str(number)
    for idx in range(len(number)//2):
        if number[idx] != number[len(number)-idx-1]:
            return False

    return True

def test_palindrome():
    """ Tests palindrome method """
    seq([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], palindrome, True,
        "palindrome number from test sequence is not palindrome")
    seq([15, 17, 19], palindrome, False,
        "not palindrome number is palindrome")



'''
PALINDROMIC PRIME

Definition: A palindromic prime is a prime which is a palindrome.
In base 2 Mersenne primes are palindromic primes.
First ten: 2, 3, 5, 7, 11, 101, 131, 151, 181, 191
There are 20 palindromic primes below 10,000.
'''

def palindromic_prime(number):
    """ Returns True if number is palindromic_prime """
    return prime(number) and palindrome(number)

def test_palindromic_prime():
    """ Tests palindromic_prime method """
    seq([2, 3, 5, 7, 11, 101, 131, 151, 181, 191], palindromic_prime, True,
        "palindromic_prime number from test sequence is not palindromic_prime")
    seq([15, 17, 19], palindromic_prime, False,
        "not palindromic_prime number is palindromic_prime")


'''
PENTAGONAL

Definition: Pentagonal numbers are of the form n(3n - 1)/2.
Pentagonal numbers are to pentagons what triangular numbers are to triangles and square numbers are to squares.
First ten: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145
There are 81 pentagonal numbers below 10,000.
'''

def pentagonal(number):
    """ Returns True if number is pentagonal """
    n = 1
    while True:
        p = n * (3 * n - 1) / 2
        if p == number:
            return True
        elif p > number:
            return False
        n = n + 1

def test_pentagonal():
    """ Tests pentagonal method """
    seq([1, 5, 12, 22, 35, 51, 70, 92, 117, 145], pentagonal, True,
        "pentagonal number from test sequence is not pentagonal")
    seq([3, 9, 13, 15, 17, 19], pentagonal, False,
        "not pentagonal number is pentagonal")
