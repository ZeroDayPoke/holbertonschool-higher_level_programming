#!/usr/bin/python3
"""rock that doc"""


def text_indentation(text):
    """placeholder"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n"
                        "\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(text, end="")
