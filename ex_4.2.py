def is_palindrome(word):
   
   """
   Funkcja odwaraca kolejność liter w słowie poprzez slicing 
   a nastepnie porównuje nowo powstałe słowo z początkowym

   """
   rword = word[::-1]
   
   if rword == word:
      return True
   else:
      return False
    
        
print(is_palindrome("kajak"))
help(is_palindrome)