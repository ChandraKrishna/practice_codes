def reverse_number(num):
    rev_num = 0
    while num > 0:
        dig = num % 10
        rev_num = rev_num * 10 + dig
        num //=10
    return rev_num
    
user_input = int(input("Enter any number : "))
result = reverse_number(user_input)
print(f"Reversed number is : {result}")

"""
b = "krishna"
print(b[::-1])

c = 123
print(str(c)[::-1])
"""


