import Utils


def temp_calc(celsius):
    # for number in celsius:
    multiplied = Utils.multiply(celsius, 1.8)
    conversion = (Utils.add(multiplied, 32))
    print("result = {0} fahrenheit".format(conversion))


value_str = input("enter numbers: ")
value_str_list = value_str.split(",")

for value_str in value_str_list:
    temp_calc(float(value_str))
