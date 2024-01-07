#!/usr/bin/python3

def multiple_returns(sentence):
     if not sentence:
         return (0, None)
     if sentence:
         num_char = len(sentence)
     
     return (num_char, sentence[0])     
