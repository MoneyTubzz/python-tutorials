firstnumber = float(input("Enter first number: "))
secondnumber = float(input("Enter second number: "))
sum = firstnumber + secondnumber
subtraction = firstnumber - secondnumber
multiplication = firstnumber * secondnumber
if secondnumber != 0:
    division = firstnumber / secondnumber
else:
    division = "undefined (cannot divide by zero)"
print("The sum is: ", sum)
print("The subtraction is: ", subtraction)
print("The multiplication is: ", multiplication)
print("The division is: ", division)