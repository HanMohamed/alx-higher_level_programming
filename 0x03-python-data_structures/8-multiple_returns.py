#!/usr/bin/python3

# Write a function that returns a tuple with
# the length of a string and its first character.
def multiple_returns(sentence):
    if (sentence):
        return (len(sentence), sentence[0])

    return (0, None)
