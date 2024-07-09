sum_n = 0
number = 0
while number != -999:
    number = int(input("Enter a number (-999 to terminate): "))
    if number != -999:
        sum_n += number

print(f"Sum of the numbers : {sum_n}")

