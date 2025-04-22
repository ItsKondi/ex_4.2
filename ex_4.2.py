def is_palindrome(word):

    word_reversed = str(reversed(word))
    if word == word_reversed:
        return True
    else: 
        return False
        
is_palindrome("kajak")
print(str(reversed("kajak")))