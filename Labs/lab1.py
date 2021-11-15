import random


def add_binary(bin_num1, bin_num2):
    """
    :param bin_num1: str
    :param bin_num2: str
    :return: str
    """
    longer = bin_num1 if len(bin_num1) > len(bin_num2) else bin_num2
    shorter = bin_num1 if len(bin_num1) < len(bin_num2) else bin_num2
    result = ''
    carry = 0
    for i in range(1, len(longer)+1):
        neg = i * -1
        if i <= len(shorter):
            if shorter[neg] == '1' and longer[neg] == '1' and carry:
                result = '0' + result
            elif shorter[neg] == '1' and longer[neg] == '1' and not carry:
                result = '0' + result
                carry = 1
            elif (shorter[neg] == '1' or longer[neg] == '1') and carry:
                result = '0' + result
            elif shorter[neg] == '1' or longer[neg] == '1':
                result = '1' + result
            elif carry:
                result = "1" + result
                carry = 0
            else:
                result = '0' + result
        else:
            if carry and longer[neg] == '1':
                result = '0' + result
            elif longer[neg] == '1':
                result = '1' + result
            elif longer[neg] == '0' and carry:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result
    if carry:
        result = '1' + result
    return result


def can_construct(word, letters):
    """
    :param word: str
    :param letters: str
    :return: bool
    """
    word = list(word)
    letters = list(letters)
    print(word, letters)
    if len(letters) < len(word):
        return False
    for i in word:
        try:
            if i in letters:
                letters.remove(i)
        except ValueError:
            return False
    return True


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):
        return Complex((self.a - other.a), (self.b - other.b))

    def __mul__(self, other):
        new_a = (self.a * other.a) - (self.b * other.b)
        new_b = (self.a * other.b) + (self.b * other.a)
        return Complex(new_a, new_b)

    def __repr__(self, other=None):
        return str(self.a) + ' + ' + str(self.b) + 'i'


def create_permutation(n):
    """
    :param n: int
    :return: lst
    """
    result = []
    for i in range(n):
        rand = random.randint(0, n-1)
        while rand in result:
            rand = random.randint(0, n-1)
        result.append(rand)
    return result


def scramble_word(word):
    result = [''] * len(word)
    indexes = create_permutation(len(word))
    for i in range(len(word)):
        result[indexes[i]] = word[i]
    return ''.join(result)


def guess(word):
    scrambled = ' '.join(scramble_word(word).split())
    print('Unscramble the word:  ' + scrambled)
    i = 1
    guessed = False
    while i <= 3 and not guessed:
        user_guess = input('Try #' + str(i) + ':  ')
        if user_guess == word:
            guessed = True
            print('Yay, you got it!')
        else:
            print('Wrong!')
            i += 1
    if not guessed:
        print('You fail')
        retry = input('Try Again? (y/n):  ')
        if retry == 'y':
            guess(word)


def main():
    print(add_binary('10011', '10111'))
    print(add_binary('101', '100100'))
    print(can_construct("apples", "aples"))
    print(can_construct("apples", "aplespl"))
    # constructor, output
    cplx1 = Complex(5, 2)
    print(cplx1)  # 5 + 2i
    cplx2 = Complex(3, 3)
    print(cplx2)  # 3 + 3i
    # addition
    print(cplx1 + cplx2)  # 8 + 5i
    # subtraction
    print(cplx1 - cplx2)  # 2 - 1i
    # multiplication
    print(cplx1 * cplx2)
    print(create_permutation(6))
    print(scramble_word("pokemon"))
    # guess('pokemon')
