#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """Print the status codes and total file size."""
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] > 0:
            print("{}: {}".format(key, dict_sc[key]))

total_file_size = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        
        # Expect at least 2 elements: file size and status code
        if len(parsed_line) < 2:
            continue

        try:
            file_size = int(parsed_line[0])  # First element is file size
            status_code = parsed_line[1]      # Second element is status code
        except ValueError:
            continue  # Skip lines where conversion fails

        total_file_size += file_size
        if status_code in dict_sc:
            dict_sc[status_code] += 1

finally:
    print_msg(dict_sc, total_file_size)
