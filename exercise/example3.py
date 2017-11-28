import exercise
"""
print(exercise.add_nums(5, 8))
print(exercise.log_def)
NumberReverse = exercise.NumberReverse()
print(NumberReverse.ReverseNumber(1234))
NumberReverse = exercise.NumberReverse()
print(NumberReverse.ReverseNumberDyn(5678))
"""
NumberReverse = exercise.NumberReverse()
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
