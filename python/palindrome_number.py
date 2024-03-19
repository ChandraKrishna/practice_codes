def reverse_number(number):
    reversed_number = 0
    original_number = number
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    if reversed_number == original_number:
        return "Palindrome"
    else:
        return "Not Palindromes"

user_input = int(input("Enter a number: "))
result = reverse_number(user_input)
print(f"The reverse of {user_input} is {result}.")