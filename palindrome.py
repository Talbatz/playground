def ispalindrome():
	inp = raw_input("your word? ")
	if inp == inp[::-1]:
		return "Palindrome :-)"
	else:
		return "Not palindrome... :-("
		
print ispalindrome()