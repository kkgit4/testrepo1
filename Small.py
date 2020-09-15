largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n = float(num)
    except:
        print("Invalid input")

    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n

    if largest is None:
        largest = n
    elif largest < n :
        largest = n

print("Maximum", largest)
print("Minimum", smallest)
