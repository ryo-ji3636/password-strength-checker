# password-strength-checker
A beginner-friendly Python tool that checks password strength, built as my first step toward learning cybersecurity


# Usage
'''bash
git https://github.com/ryo-ji3636/password-strength-checker.git
cd password-strength-checker
python passord_checker.py
'''


# What I learned 
First, I made very easy checker using only if and for functions. Then, I added define function for evaluating if password is strong or not. Also, I used getpass module because the length of password can be elements that others guess my password. I also added a check against a list of common passwords, loaded from a txt file. I noticed that a password like `Password1!` satisfies all the rules (length, uppercase, lowercase, digit, symbol) but is still a predictable pattern, so rule-based checks alone are not enough. While building this, I found a bug: an empty line in the password list caused every password to be marked as weak, because an empty string is always "contained in" any string in Python.This taught me to think about edge cases when reading external files.
I changed 'is_strong' top return both a boolean and a list of reasons, so the function focuses only on judging the password, while printing is handled separately in `__main__`. This taught me the idea of separating logic from display. I also wrote tests with pytest. While testing, I accidentally created two functions with the same name, and Python silently used the second one without any error — that was a good reminder to always check the full test output, not just assume things are working.



# Future improvements
-  I will use more larger, real-world common password list
- handle edge cases like passwords containing only whitespace
