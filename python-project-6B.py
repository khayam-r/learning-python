# temperature conversion calculator

unit = input("is this temperature in celsius or fahrenheit (c/f): ")
temp = float(input("enter the temperature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f" the temperature in fahrenheit is : {temp}ºF")
elif unit == "f":
    temp = round((temp - 32) * 5  / 9)
    print(f" the temperature in celsius is : {temp}ºC")
else:
    print(F"{unit} is and invalid unit of measurement")


















































































