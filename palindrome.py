def isPalindrome(strng):
    if len(strng) == 0:
        return 'Palindrome'
    if strng[0] != strng[len(strng)-1]:
        return 'Not Palindrome'
    return isPalindrome(strng[1:-1])
s='malayalam'
print(isPalindrome(s))