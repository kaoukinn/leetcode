celsius = 36.50

anslist = []
Fahrenheit = round(celsius * 1.80 + 32.00, 5)
Kelvin = round(celsius + 273.15, 5)
anslist.append(Kelvin)
anslist.append(Fahrenheit)
print(anslist)
# Kelvin = ("{:.5f}".format(Kelvin))
# Fahrenheit = ("{:.5f}".format(Fahrenheit))

# anslist.append("{:.5f}".format(Kelvin))
# anslist.append("{:.5f}".format(Fahrenheit))
# new_list = [float(x) for x in anslist]
# print(new_list)
