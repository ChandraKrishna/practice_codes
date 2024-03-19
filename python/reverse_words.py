def reverse_words(input_str):
    words = input_str.split()  # Split the string into a list of words
    reversed_words = ' '.join(reversed(words))  # Reverse the list of words and join them back

    return reversed_words

# Example usage:
user_input_string = input("Enter a string: ")
result = reverse_words(user_input_string)
print(f"The reversed words of '{user_input_string}' are '{result}'.")
