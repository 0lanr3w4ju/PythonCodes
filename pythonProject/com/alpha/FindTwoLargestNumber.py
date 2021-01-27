# finds the two largest numbers of ten numbers

firstLargestNumber = 0
secondLargestNumber = 0
counter = 0

while counter < 10:
    digit = int(input("enter number: "))

    if digit > firstLargestNumber:
        secondLargestNumber = firstLargestNumber
        firstLargestNumber = digit
    elif digit > secondLargestNumber:
        secondLargestNumber = digit
    counter += 1

print()
print(f"largest number = {firstLargestNumber}")
print(f"second largest number = {secondLargestNumber}")

