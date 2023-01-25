#!/usr/bin/python3
"""rock that doc"""


def text_indentation(text):
    """placeholder"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.lstrip(' ')
    text = text.rstrip(' ')
    text = text.replace(".", ".\n"
                        "\n").replace("?", "?\n\n").replace(":", ":\n\n")
    tokens = text.split("\n")
    tokens = [token.strip() for token in tokens]
    text = "\n".join(tokens)
    print(text, end="")
