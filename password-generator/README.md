# Random Password Generator (RPG) Specification

My goal is to create a random password generator (RPG) written in python. This password generator will have the following specifications:
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

# Versions

| Version | Comments |
| --- | --- |
| Version 1 (rpg-v1.py) | Written in python; two of the included functions - create_password() and pass_checker() are written recursively. |
| Version 2 (rpg-v2.py) | Identical to version 1 but is written with create_password() and pass_checker() as iterative solutions instead of recursive. |

# Version 1 vs Version 2

Version 1 and 2 are nearly identical random password generators. The only difference is in the implementation of two of the functions in the code. The two functions are `create_password()` and `pass_checker()`. I originally wrote them in v1 as recursive solutions because it has taken me a long time to fully understand recursion. When I recently took the [Programming Languages, Part A](https://www.coursera.org/learn/programming-languages) class on Coursera, I finally began to understand recursion because it was required in nearly every solution. However, that class was in SML/NJ (Standard ML - New Jersey) which is a static, functional language. I learned programming first in python which is a dynamic, imperative language. Therefore, I decided that I wanted to practice recursion in python. While recursion felt very natural to me in SML/NJ because of the math-like feel of the language, it did not feel so natural in python. When I compare the iterative and recursive solutions side by side, I believe that the iterative solution appears more intuitive and easier to read.
For Example, here are the two functions presented in both versions:

### Created Password Function

Recursive:

``` python

def create_password(n, password):
    if n <= 0:
        return password
    else:
        return create_password(n - 1, random_item() + password)

```

Iterative:

``` python

def create_password(n, password):
    while n > 0:
        password += random_item()
        n -= 1
    return password

```

### Pass Checker Function

Recursive:

``` python

def pass_checker(password, up, low, num, sym):
    if password == "":
        return [up, low, num, sym]
    else:
        if password[0] in uppers:
            return pass_checker(password[1:], up + 1, low, num, sym)
        elif password[0] in lowers:
            return pass_checker(password[1:], up, low + 1, num, sym)
        elif password[0] in nums:
            return pass_checker(password[1:], up, low, num + 1, sym)
        elif password[0] in symbs:
            return pass_checker(password[1:], up, low, num, sym + 1)

```

Iterative:

``` python

def pass_checker(password, up, low, num, sym):
    for item in password:
        if item in uppers:
            up += 1
        elif item in lowers:
            low += 1
        elif item in nums:
            num += 1
        elif item in symbs:
            sym += 1
    return [up, low, num, sym]

```

### Analysis

While the recursive `create_password()` function is only slightly more bulky, the recursive `pass_checker()` solution is significantly more bulky and less visually appealing. Part of the issue is the need for the repetitive `return` calls, which clogs the code with what would normally be unnecessary repetition. The other issue has to do with the design of this particular function which requires four separate accumulators. In a recursive solution, you have to continue to pass in each argument that is necessary for the function. In this case, it is required to insert each of the 4 accumulators 4 different times for the different branches. While I do enjoy creating a recursive solution to a problem just to see if I can make it work, I would prefer the iterative solutions to both of these functions. The iterative solutions are easy to read and understand and are less visually distracting. I think that python is written in such a way that `for` and `while` loops are very intuitive and elegant to implement and review.