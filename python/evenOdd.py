def evenOdd(num):
    if num % 2 == 0:
        if num == 0:
            return "Whole Number"
        return "Even"
    else:
        return "Odd"
    
user_input = int(input("Enter any number : "))
result = evenOdd(user_input)
print(f"Input Number is {result}")