def sum(x, y, test = 1):
    return x + y + test

x = 1
y = 1
print(sum(x, y, 3)) # 5

def sum(x, *y):
    result = 0
    for i in y:
        result += i
    print(x + result)
    
sum(1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # 56

'''
def sum(x, *y):
    sum_list = []
    for i in y:
        sum_list.append(i)
    print(sum_list)
sum(1, 1, 2, 3, 4, 5)  # [1, 2, 3, 4, 5]
'''

def sum(one, two):
    return one + two

print(sum(one = 1, two = 1)) # 2
