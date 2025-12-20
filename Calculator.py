try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What operation would you like to perform?.\nPress + for addtion\nPress - for subtraction\nPress * for multiplication\nPress / for division")


    o = input("Enter Operation: ") 
    match o:
        case "+":
            print(f"The result is: {a + b}")
   
        case "-":
            print(f"The result is: {a - b}")
   
        case "*":
            print(f"The result is: {a * b}")
   
        case "/":
            print(f"The result is: {a / b}")

        case default:
            print(f"There was an error")

except Exception as e:
    print("Enter a valid value of a and b")



'''
Output:
Enter the first number: 67
Enter the second number: 3
What operation would you like to perform?.
Press + for addtion
Press - for subtraction
Press * for multiplication
Press / for division
Enter Operation: *
The result is: 201

Enter the first number: 77
Enter the second number: 79
What operation would you like to perform?.
Press + for addtion
Press - for subtraction
Press * for multiplication
Press / for division
Enter Operation: *
The result is: -2


Enter the first number: 77
Enter the second number: 13
What operation would you like to perform?.
Press + for addtion
Press - for subtraction
Press * for multiplication
Press / for division
Enter Operation: +
The result is: 90

'''