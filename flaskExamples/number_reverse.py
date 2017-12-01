
class NumberReverse:

    reverse = 0
    remainder = 0

    def __init__(self):
        pass

    def ReverseNumber(self, num):
        rev = 0
        while(num > 0):
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        return rev

    def ReverseNumberDyn(self, num):
        if (num > 0):
            self.remainder = num % 10
            self.reverse = self.reverse * 10 + self.remainder
            self.ReverseNumberDyn(num // 10)
        else:
            return self.reverse
        return self.reverse

    def DivisibleBy7(self, num):
        reversedNumber = 0
        self.remainder = 0
        self.reverse = 0
        magicNumber = (1, 3, 2, 6, 4, 5, 1, 3, 2, 6, 4, 5,
                       1, 3, 2, 6, 4, 5, 1, 3, 2, 6, 4, 5,)
        reversedNum = 0
        reversedNumber = self.ReverseNumberDyn(num)
        # print(reversedNumber)
        for num1 in range(len(str(reversedNumber))):
            reversedNum = reversedNum +\
                (int(str(reversedNumber)[num1]) * magicNumber[num1])
        """
        if (reversedNum > 7):
            self.DivisibleBy7(reversedNum)
        """
        if(reversedNum % 7 == 0):
            return (reversedNumber+num)
        else:
            return 0
