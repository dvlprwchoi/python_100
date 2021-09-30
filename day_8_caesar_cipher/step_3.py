alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(text_input, shift_amount, function_type):
    text_output = ""
    # #This if statement should not be in the for loop
    if function_type == "decode":
        shift_amount *= -1
    for letter in text_input:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        text_output += alphabet[new_position]
    print(f"The {function_type} text is {text_output}")


# def caesar(text_input, shift_amount, function_type):
#     text_output = ""
#     for letter in text_input:
#         position = alphabet.index(letter)
#         if (function_type == "encode"):
#             new_position = position + shift_amount
#         elif (function_type == "decode"):
#             new_position = position - shift_amount
#         else:
#             print("You have to choose between 'encode' and 'decode'.")
#             return
#         text_output += alphabet[new_position]
#     print(f"The {function_type} text is {text_output}")


# def caesar(text_input, shift_amount, function_type):
#     text_output = ""
#     if (function_type == "encode"):
#         for letter in text_input:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             text_output += alphabet[new_position]
#         print(f"The {function_type} text is {text_output}")
#     elif (function_type == "decode"):
#         for letter in text_input:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             text_output += alphabet[new_position]
#         print(f"The {function_type} text is {text_output}")
#     else:
#         print("Try it again!")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text_input=text, shift_amount=shift, function_type=direction)
