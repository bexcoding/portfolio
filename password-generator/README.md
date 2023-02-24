# Password Generator Specification

My goal is to create a password generator written in python. This password generator will have the following specifications:
1. Will be written in python.
2. Will accept an integer from the user to determine the length of the password.
   - The integer will be between 4 and 15 (inclusive, i.e. the password can be 4 characters OR 15 characters OR any whole number between).
   - If any integer is used outside of these limits or if the input is of the incorrect type, the default password length of 8 characters will be used.
3. The program will include at least one of each of the following types:
   - Number
   - Uppercase letter
   - Lowercase letter
   - Symbol
4. The final output of the program will be a single string.
5. No password generated with the program will be saved, remembered, or stored in part or whole after the program is ended.
6. The password that is generated will follow no discernible pattern appart from meeting length and character type inclusion requirements.