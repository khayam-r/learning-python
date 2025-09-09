# condtional expressions

num = 5
a = 6
b = 7
age = 13
temp = 20
user_role = "guest"


# print("positive" if num > 0 else "negative" )
# result = "even" if num % 2 == 0 else "odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "adult" if age >= 18 else "child"
# weather = "hot" if temp > 20 else "cold"
access_level = "full access" if user_role == "admin" else "limited access"

print(access_level)