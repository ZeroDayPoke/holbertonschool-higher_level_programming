#!/usr/bin/python3
"""
Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module
"""
def multiple_returns(sentence):
    ret1_len = len(sentence)
    ret2_char = sentence[0] if sentence else None
    return (ret1_len, ret2_char)
