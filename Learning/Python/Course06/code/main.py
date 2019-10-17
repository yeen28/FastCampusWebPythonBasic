test1 = "Life is too short, %s"
result1 = test1 % "You need python."
print(result1) # Life is too short, You need python.
test1 = "Life is too short, %s %s %s"
result1 = test1 % ("You", "need", "python.")
print(result1) # Life is too short, You need python.
test2 = "Life is too short, %s"
result2 = test2 % "10"
print(result2) # Life is too short, 10
# 하지만 
# test2 = "Life is too short, %d"
# result2 = test2 % "10"  -> 에러!
test3 = "Life is too short, %.2f"
result3 = test3 % 100.1234
print(result3) # Life is too short, 100.12
test4 = "Life is too short, {} {} {}"
result4 = test4.format("You", "need", 10)
print(result4) # Life is too short, You need 10
# test4 = "Life is too short, %s %s %s"
# result4 = test4.format("You", "need", 10)
# print(result4) # Life is too short, %s %s %s
test5 = "\"Life is too short\",\n\'You need python.\'"
print(test5)
'''
"Life is too short",
'You need python.'
'''
