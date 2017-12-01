import flaskExamples
"""
print(flaskExamples.add_nums(5, 8))
print(flaskExamples.log_def)
NumberReverse = flaskExamples.NumberReverse()
print(NumberReverse.ReverseNumber(1234))
NumberReverse = flaskExamples.NumberReverse()
print(NumberReverse.ReverseNumberDyn(5678))
"""
NumberReverse = flaskExamples.NumberReverse()
# print(NumberReverse.DivisibleBy7(1603))
summ = 0
for num in range(10**8, 10 ** 11):
    summ = summ + NumberReverse.DivisibleBy7(num)
print(summ)
# 136364420695
# 1350000019615390
"""
print(NumberReverse.DivisibleBy7(1603))
"""
