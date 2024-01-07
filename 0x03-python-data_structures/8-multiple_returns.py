#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence = None

    if sentence:
        char_len = len(sentence)

    else:
        char_len = 0

    return (char_len, sentence if not sentence else sentence[:1])    
