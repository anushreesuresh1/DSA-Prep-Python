# Q1. Write a Python program to Reverse a String?
# input_string = "Hello, World!"

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

def reverse_string_loop(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string



def reverse_string_in_place(input_string):
    start, end = 0, len(input_string) - 1
    while start < end:
        input_string[start], input_string[end] = input_string[end], input_string[start]
        start += 1
        end -= 1
    return ''.join(input_string)



if __name__ == "__main__":
    input_string = "Hello, World!"
    print("Original String:", input_string)
    print("Reversed String:", reverse_string(input_string))
    print("Reversed String (using loop):", reverse_string_loop(input_string))
    print("Reversed String (in place):", reverse_string_in_place(list(input_string)))

