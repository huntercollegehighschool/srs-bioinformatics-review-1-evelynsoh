"""
Define a function isDNA that takes a single string as an input. The string is supposed to represent a DNA string that only has molecules A, C, G, and T. The function returns True(the Boolean value) if the string is a valid DNA string, and False if it's not.
"""

def isDNA(dna):
  correct = "ACGT"
  for letter in dna: 
    if letter not in correct: 
        return False
  return True