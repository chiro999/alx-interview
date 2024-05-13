#!/usr/bin/python3
"""
UTF-8 Validation
"""

# Define the function validUTF8 that takes a list of integers (data) as input
def validUTF8(data):
    """
    Data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    # Initialize byte_count to 0
    byte_count = 0

    # Iterate through each integer in the data list
    for i in data:
        # If byte_count is 0, indicating the start of a new UTF-8 character
        if byte_count == 0:
            # Check if the integer matches the pattern for a 2-byte character
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            # Check if the integer matches the pattern for a 3-byte character
            elif i >> 4 == 0b1110:
                byte_count = 2
            # Check if the integer matches the pattern for a 4-byte character
            elif i >> 3 == 0b11110:
                byte_count = 3
            # If none of the above patterns match, it's an invalid byte sequence
            elif i >> 7 == 0b1:
                return False
        else:
            # If byte_count is not 0, indicating a continuation byte
            # Check if the integer matches the pattern for a continuation byte
            if i >> 6 != 0b10:
                return False
            # Decrement byte_count to move to the next byte of the UTF-8 character
            byte_count -= 1

    # After iterating through all integers, if byte_count is 0, it's a valid UTF-8 sequence
    return byte_count == 0
