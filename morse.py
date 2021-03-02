#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Benjamin Feder'

from morse_dict import MORSE_2_ASCII

# from itertools import groupby


def decode_bits(bits):
    bits = bits.strip("0")  # remove whitespace from ends of bits

    counts = []  # set empty list to later get min num of spaces in a row
    count = 0  # set count to default zero

    last_bit = "1"

    # for i, char in enumerate(bits):
    #     if char == "0" and bits[i-1] != "1":
    #         count += 1
    #     elif char == "1" and bits[i-1] == "0":
    #         counts.append(count)
    #         count = 1
    #     elif char == "0" and bits[i-1] == "1":
    #         counts.append(count)
    #         count = 1
    #     elif char == "1" and bits[i-1] != "0":
    #         count += 1

    for char in bits:
        if char != last_bit:
            counts.append(count)
            count = 0
            last_bit = char
        count += 1

    counts.append(count)

    time_multiplier = min(counts)
    """get min num of spaces in a row set as time
    unit multiplier"""

    # ones_count = 0
    # zeros_count = 0
    morse_chars = ""  # set empty string for morse message to be added to

    # for i, num_char in enumerate(bits):
    #     if num_char == "1" and i != len(bits) - 1:
    #         if zeros_count // time_multiplier == 3:
    #             morse_chars += " "
    #         elif zeros_count // time_multiplier == 7:
    #             morse_chars += "   "
    #         zeros_count = 0
    #         ones_count += 1
    #     elif num_char == "1" and i == len(bits) - 1:
    #         if zeros_count // time_multiplier == 3:
    #             morse_chars += " "
    #         elif zeros_count // time_multiplier == 7:
    #             morse_chars += "   "
    #         zeros_count = 0
    #         ones_count += 1
    #         if ones_count // time_multiplier == 1:
    #             morse_chars += "."
    #         elif ones_count // time_multiplier == 3:
    #             morse_chars += "-"
    #     elif num_char == "0":
    #         if ones_count // time_multiplier == 1:
    #             morse_chars += "."
    #         elif ones_count // time_multiplier == 3:
    #             morse_chars += "-"
    #         ones_count = 0
    #         zeros_count += 1

    for i, count in enumerate(counts):
        if i % 2 == 0:
            if count // time_multiplier == 1:
                morse_chars += "."
            elif count // time_multiplier == 3:
                morse_chars += "-"
        else:
            if count // time_multiplier == 3:
                morse_chars += " "
            elif count // time_multiplier == 7:
                morse_chars += "   "

    return morse_chars


def decode_morse(morse):
    morse = morse.strip()
    """remove potential white spaces from either
    end of message"""
    # break up message by words (3 spaces in morse)
    morse_words_list = morse.split("   ")

    actual_words = ""  # set empty string for words that will be added

    for words in morse_words_list:  # loop through all encoded words
        # break up words by character (1 space between each character in morse)
        chars_list = words.split(" ")
        actual_chars = ""
        """set empty string for characters that will be
        added to the word"""
        for dots_dashes in chars_list:  # loop through each encoded character
            actual_chars += MORSE_2_ASCII[dots_dashes]
        actual_words += actual_chars + " "
    return actual_words.strip()  # remove final white space from end of words


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
