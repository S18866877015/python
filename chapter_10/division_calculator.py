#print(5/0) 会引发ZeroDifisionError: division by zero

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
"""
