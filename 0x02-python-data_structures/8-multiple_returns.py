#!/usr/bin/python3
def multiple_returns(sentence):
    ret1_len = len(sentence)
    ret2_char = sentence[0] if sentence else None
    return (ret1_len, ret2_char)
