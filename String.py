# Given a sentence, reverse all words and remove all leading and preceding whitespace
def reverse_string(s):
    words = (' ').join(s.split()[::-1])
    return words
