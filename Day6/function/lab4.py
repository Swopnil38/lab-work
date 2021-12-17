'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
'''
def multiple(limit):
    sum2 =0
    for i in range(limit+1):
        if i%3 == 0 or i%5 == 0:
            sum2 += i
    return sum2

num1 = int(input("Enter any Number:"))
sum_1 = multiple(num1)
print(f"The sum of multipes of 3 and 5 is: {sum_1}")