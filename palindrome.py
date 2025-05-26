# Q2. Write a Python program to Check Palindrome?

# Input 1 - 
# input_string = "A man, a plan, a canal, Panama"

# input 2 - 
# input_number = 12321


def palindrome_string(input_string):
    #converting to lowercase + removing spaces and special characters
    str = ''.join(char.lower() for char in input_string if char.isalnum())
    return str == str[::-1]

def palindrome_number(input_number):
    # converting the number to string
    str_number = str(input_number)
    return str_number == str_number[::-1]


if __name__ == "__main__":

    # Test with a string input
    input_string = "A man, a plan, a canal, Panama"
    print("Is Palindrome (String):", palindrome_string(input_string))
    # Test with a number input
    input_number = 12321
    print("Is Palindrome (Number):", palindrome_number(input_number))
    