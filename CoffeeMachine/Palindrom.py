from audioop import reverse

s = "AkkkkA"

if s == s[::-1]:
    print("palindrome")
else:
    print("NOt a palindrome")