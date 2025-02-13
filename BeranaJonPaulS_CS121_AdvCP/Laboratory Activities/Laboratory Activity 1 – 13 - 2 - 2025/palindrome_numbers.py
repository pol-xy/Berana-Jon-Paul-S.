num = int(input("Enter a number: "))

palindrome_num = str(num)
if palindrome_num == palindrome_num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
