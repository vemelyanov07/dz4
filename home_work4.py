from functools import reduce


n = int(input("Введите целое число "))
x = 0
def summ(num):
    while num >= 0:
        num = num % 10
        x = x+num
        num = num//10
    return x
print(summ(n))

n = int(input("Введите целое число "))
y = 1
def summ(num):
    while num >= 0:
        num = num % 10
        y = y+num
        num = num//10
        return y
print(summ(y))

start = 1
end = 10
itog = sum(range(1, 10))
def sum_range(start,end):
    return(end*(end+1)/2) - (start - 1) * start/2
print(itog)
print (sum_range(start, end))


          


