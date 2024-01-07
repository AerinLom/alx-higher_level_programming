#!/usr/bin/python3

def multiple_returns(sentence):
     if not sentence:
         sentence = None

     if sentence:
         num_char = len(sentence)

     else:
         num_char = 0
     
     return (num_char, sentence if not sentence else sentence[:1])     
