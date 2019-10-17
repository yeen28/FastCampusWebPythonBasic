from random import sample

num_list = [1, 5, 4, 3, 2] # list
num_dict = {"a":6, "e":10, "d":9, "b":7, "c":8} # dictionary

# 오름 차순 정렬
q = num_list.sort() # 값을 정렬만 하고, 반환 값이 없습니다.
print(q) # None
print(num_list) # [1, 2, 3, 4, 5]
num_list = sorted(num_list) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_list) # [1, 2, 3, 4, 5]
# 단, 아래와 같이 정렬하면, 기존의 딕셔너리 자료형의 특징인 "키:값" 형태가 아닌, 단순히 값만을 나타내는 리스트 컬렉션이 된다는 점에 유의해야합니다.
num_dict = sorted(num_dict.values()) # 값을 정렬하고, 정렬된 결과를 반환합니다. # num_dict가 dictionary에서 list가 됨
print(num_dict) # [6, 7, 8, 9, 10]

# 내림 차순 정렬
# num_list.reverse() # -> 같은 의미
# print(num_list) # [5, 4, 3, 2, 1]
num_list.sort(reverse = True) # 값을 정렬만 하고, 반환 값이 없습니다. (같은 표현, num_list.reverse())
num_list = sorted(num_list, reverse = True) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_list) # [5, 4, 3, 2, 1]

# 단, 아래와 같이 정렬하면, 기존의 딕셔너리 자료형의 특징인 "키:값" 형태가 아닌, 단순히 값만을 나타내는 리스트 컬렉션이 된다는 점에 유의해야합니다.
num_dict = {"a":6, "e":10, "d":9, "b":7, "c":8}
num_dict = sorted(num_dict.values(), reverse = True) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_dict) # [10, 9, 8, 7, 6]

# lambda, map, filter

# lambda를 이용한 딕셔너리 내림차순 정렬
num_dict = {"a":6, "e":10, "d":9, "b":7, "c":8}
num_dict = sorted(num_dict.items(), key = lambda x:[x], reverse = True) # dictionary에서 list가 됨
print(num_dict) # [('e', 10), ('d', 9), ('c', 8), ('b', 7), ('a', 6)]

for k, v in num_dict: # num_dict는 list형태임
    print(k, v, end = ' ') # e 10 d 9 c 8 b 7 a 6 

rand = sample(range(1, 11), 5) # 1부터 10까지 랜덤한 수 5개 반환 -> list
print(rand) # [9, 8, 6, 2, 1]
up = list(filter(lambda x:x > 2, rand)) # rand에 있는 값들 중 2보다 큰 수만 up에 반환
print(up) # [9, 8, 6]

division = list(map(lambda x:x / 2, rand)) # rand에 있는 값들을 2로 나눈 후 division에 반환
print(division) # [4.5, 4.0, 3.0, 1.0, 0.5
