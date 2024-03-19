def reverse_str(str):
    rev = ''
    org = str
    count = len(str)

    for i in str:
        rev = rev + str[count-1]
        count = count -1
    
    if rev == org:
        return "Palindrome"
    else:
        return "Not Palindromes"

user_input = str(input("Enter any string : "))
result = reverse_str(user_input)
print(f"Reversed string is : {result}")