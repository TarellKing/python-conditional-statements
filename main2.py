num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
choice = input("Do you want to Add(+),Subtract(-),Multiply(*), or Divide(/)? ")

if choice.upper() == "ADD":
    answer = num1 + num2
    print(num1, "+", num2, "=", answer)


elif choice.upper() == "SUBTRACT":
    answer = num1 - num2
    print(num1, "-", num2, "=", answer)

elif choice.upper() == "MULTIPLY":
    answer = num1 * num2
    print(num1, "*", num2, "=", answer)

elif choice.upper() == "DIVIDE":
    answer = num1 / num2
    print(num1, "/", num2, "=", answer)

