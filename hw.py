class Reverse:
    def __init__(self, s=""):
        self.s = s
    def __str__(self):
        words = self.s.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words
user_input = input("Enter a string: ")
rev_obj = Reverse(user_input)
print("Reversed string:", rev_obj)