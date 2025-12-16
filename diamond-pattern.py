n = int(input("Enter number: "))

space = n - 1
stars = 1

for i in range(n):
    print("  " * space + "* " * stars)
    space -= 1
    stars += 2

space = 1
stars = stars - 4

for i in range(n-1):
    print("  " * space + "* " * stars)
    space += 1
    stars -= 2
