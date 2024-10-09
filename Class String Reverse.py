class class_reverse:
    
    def __init__(self, word_s):
        self.s = word_s
        
    def reverse_word(self):
        return self.s[::-1]
    
    def capitalize(self):
        return self.s.upper()
    
    
word = input("Enter a Word to be Reversed: ")
rev_ob = class_reverse(word)
result = rev_ob.reverse_word() and rev_ob.capitalize()
print(f"Reversed String: {result}")