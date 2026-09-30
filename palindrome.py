text = input("enter a string:")
cleaned_text = text.replace(" ", "").lower ()
if cleaned_text == cleaned_text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")