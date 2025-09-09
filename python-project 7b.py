#  logical operators 
# and 

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is HOT outside")
    print("it is sunny") 
elif temp <= 0 and is_sunny:
    print("it is COLD outside")
    print("it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("it is HOT outside")
    print("it is cloudy") 
elif temp <= 0 and not is_sunny:
    print("it is COLD outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")