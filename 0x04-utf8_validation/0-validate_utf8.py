#!/usr/bin/python3
""" This module defines the function: validUTF8."""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for byte in data:
        # Consider only the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & 0xE0) == 0xC0:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check continuation byte (10xxxxxx)
            if (byte & 0xC0) != 0x80:
                return False
            num_bytes -= 1

    # If num_bytes is not 0, there are incomplete characters
    return num_bytes == 0
