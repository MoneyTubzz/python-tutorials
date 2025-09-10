count = int(input("Enter the amount of Fibonacci numbers to generate: "))
a, b = 0, 1
for i in range(count):
    print(a)
    a, b = b, a + b