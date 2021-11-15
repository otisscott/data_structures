from lab1 import add_binary


class Polynomial:
    def __init__(self, data=None):
        if data is None:
            data = [0]
        self.data = data

    def __add__(self, other):
        shorter = self.data if len(self.data) < len(other.data) else other.data
        longer = self.data if len(self.data) > len(other.data) else other.data
        new_data = []
        for i in range(len(longer)):
            if i < len(shorter):
                new_data.append(shorter[i] + longer[i])
            else:
                new_data.append(longer[i])
        return Polynomial(new_data)
    
    def __call__(self, num):
        result = 0
        for i in range(len(self.data)):
            result += self.data[i]*(num**(i+1))
        return result


class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str

    def __add__(self, other):
        return UnsignedBinaryInteger(add_binary(self.data, other.data))

    def decimal(self):
        result = 0
        reverse = self.data[::-1]
        for i in range(len(self.data)):
            result += int(reverse[i])*(2**i)
        return result

    def __lt__(self, other):
        return True if self.decimal() < other.decimal() else False

    def __gt__(self, other):
        return True if self.decimal() > other.decimal() else False

    def __eq__(self, other):
        return True if self.decimal() == other.decimal() else False

    def is_twos_power(self):
        num = self.decimal()
        while num > 0:
            num = num / 2
            if num % 2 != 0:
                return False
            if num == 2:
                return True

    def largest_twos_power(self):
        return 2**(len(self.data) - 1)

    def __or__(self, other):
        if len(self.data) != len(other.data):
            longer = self.data if len(self.data) > len(other.data) else other.data
            shorter = self.data if len(self.data) < len(other.data) else other.data
            difference = len(longer) - len(shorter)
            shorter = difference * '0' + shorter
        else:
            shorter = other.data
            longer = self.data
        result = ''
        for i in range(len(longer)):
            if shorter[i] == '1' or longer[i] == '1':
                result += '1'
            else:
                result += '0'
        return UnsignedBinaryInteger(result)

    def __and__(self, other):
        if len(self.data) != len(other.data):
            longer = self.data if len(self.data) > len(other.data) else other.data
            shorter = self.data if len(self.data) < len(other.data) else other.data
            difference = len(longer) - len(shorter)
            shorter = difference * '0' + shorter
        else:
            shorter = other.data
            longer = self.data
        result = ''
        for i in range(len(longer)):
            if shorter[i] == '1' and longer[i] == '1':
                result += '1'
            else:
                result += '0'
        return UnsignedBinaryInteger(result)

    def __repr__(self):
        return '0b' + self.data


def main():
    poly1 = Polynomial([3, 7, 0, -9, 2])
    poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
    poly3 = poly1 + poly2
    print(poly3.data)
    val1 = poly1(1)
    print(val1)
    val2 = poly2(1)
    print(val2)
    val3 = poly3(1)
    print(val3)

    b1 = UnsignedBinaryInteger('10011')
    b2 = UnsignedBinaryInteger('100')
    print("b1 is: ", b1)
    print("b2 is: ", b2)
    b3 = b1 + b2
    print("b3 is: ", b3)

    print("\nChecking decimal values:\n")
    print(b1.decimal())  # 19
    print(b2.decimal())  # 4
    print(b3.decimal())  # 23
    print("\nChecking comparisons:\n")
    print(b1 < b2)  # False
    print(b2 < b1)  # True
    print(b1 > b2)  # True
    print(b2 > b1)  # False
    print(b1 + b2 == b3)  # False
    print("\nChecking is_twos_power:\n")
    print(b1.is_twos_power())  # False
    print(b2.is_twos_power())  # True
    print(b3.is_twos_power())  # False
    print("\nChecking largest_twos_power:\n")
    print(b1.largest_twos_power())  # 16
    print(b2.largest_twos_power())  # 4
    print(b3.largest_twos_power())  # 16
    print("\nTesting b1: ", b1, "b2: ", b2)
    b4 = b1 | b2
    b5 = b1 & b2
    print(b1, "|", b2, "=", b4)  # 0b100
    print(b1, "&", b2, "=", b5)
    b6 = UnsignedBinaryInteger('1010')
    b7 = UnsignedBinaryInteger('1001')
    print("\nTesting b6: ", b6, "b7: ", b7)
    b8 = b6 | b7
    b9 = b6 & b7
    print(b6, '|', b7, '=', b8)
    print(b6, '&', b7, '=', b9)
