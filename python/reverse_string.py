def reverse_str(str):
    rev = ''
    count = len(str)

    for i in str:
        rev = rev + str[count-1]
        count = count -1
    return rev

user_input = str(input("Enter any string : "))
result = reverse_str(user_input)
print(f"Reversed string is : {result}")

"""
b = "krishna"
print(b[::-1])

c = 123
print(str(c)[::-1])
"""