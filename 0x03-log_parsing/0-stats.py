#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print status codes and total file size.
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
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
        
        # Expecting at least 3 elements (file size, status code)
        if len(parsed_line) < 3:
            continue

        try:
            file_size = int(parsed_line[0])  # file size
            status_code = parsed_line[1]  # status code
        except ValueError:
            continue  # Skip lines where conversion fails

        total_file_size += file_size
        if status_code in dict_sc:
            dict_sc[status_code] += 1

finally:
    print_msg(dict_sc, total_file_size)
