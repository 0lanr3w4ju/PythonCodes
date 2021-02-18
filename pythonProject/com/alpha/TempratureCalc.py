import Utils

try:
    celsius = int(input("enter number to be converted: "))
except ValueError:
    print("enter only number")
else:
    multiplied = Utils.multiply(celsius, 1.8)
    conversion = (Utils.add(multiplied, 32))

    print("result = {0} fahrenheit".format(conversion))
