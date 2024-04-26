#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of
    operations needed to result in exactly n 'H'
    characters in this file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             If n is impossible to achieve, returns 0.
    '''
    pasted_chars = 1  # Tracks how many chars are currently in the file.
    clipboard = 0     # Tracks how many 'H's are copied to the clipboard.
    counter = 0       # Counts the number of operations performed.

    while pasted_chars < n:
        if clipboard == 0:
            # If clipboard is empty, copy all characters.
            clipboard = pasted_chars
            counter += 1  # Increment operations counter.

        if pasted_chars == 1:
            # If no characters are pasted yet, paste.
            pasted_chars += clipboard
            counter += 1  # Increment operations counter.
            continue  # Continue to the next iteration.

        remaining = n - pasted_chars  # Calculate remaining characters to paste.

        if remaining < clipboard or remaining % pasted_chars != 0:
            # Check if it's impossible to achieve n characters.
            # If remaining characters are less than clipboard size,
            # or if remaining cannot be divided evenly by pasted_chars,
            # it's impossible to achieve n characters.
            return 0

        # If remaining can be divided evenly by pasted_chars,
        # paste the clipboard; otherwise, copy all and then paste.
        pasted_chars += clipboard
        counter += 1 if remaining % pasted_chars else 2  # Increment operations counter.

    return counter if pasted_chars == n else 0  # Return the operations counter if n is achieved; otherwise, return 0.
