#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys  # Import the sys module for system-specific parameters and functions.

# Initialize a dictionary to store counts of HTTP status codes.
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize variables to track total file size and line count.
total_size = 0
counter = 0

try:
    # Iterate over each line in the standard input.
    for line in sys.stdin:
        # Split the line into a list of words.
        line_list = line.split(" ")

        # Check if the line has more than 4 elements.
        if len(line_list) > 4:
            # Extract HTTP status code and file size.
            code = line_list[-2]
            size = int(line_list[-1])

            # Update cache with count of HTTP status codes.
            if code in cache.keys():
                cache[code] += 1

            # Update total file size and line count.
            total_size += size
            counter += 1

        # Check if 10 lines have been processed.
        if counter == 10:
            # Reset line counter and print file size and HTTP status code counts.
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass  # Ignore any exceptions that occur during execution.

finally:
    # Print file size and HTTP status code counts at the end.
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
