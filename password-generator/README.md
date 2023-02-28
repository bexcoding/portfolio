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
| Version 3 (rpg-v3.rkt) | Different implementation using racket. Approach is significantly different from v1 or v2. The racket code does not render correctly in GitHub but it can be downloaded by clicking on the Raw tab. |
| Version 4 (rpg-v4.js) | A version written in JavaScript. Has similar implementation to the racket version but also has unique style. |

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

# V1 and V2 Compared to V3

Both version 1 and version 2 are written in python while version 3 is written in racket. While I have written many programs in python, I have relatively little experience at this point with racket. This meant, despite many attempts to make the implementation of version 3 similar to the first two versions, I did not have the experience to do so.

1. The first issue I ran into was getting user input. In python, it is relatively simple to get input and assign it to a variable with something like `pass_length = input("Type password length: ")`. This variable could then be passed around the program. In racket, the `(read-line)` function works similarly but I could not get it to appear at the correct segment of the code. The prompt for input would happen at an unexpected portion of the code. Then, when I tried to pair it with a `print` statement to explain what sort of input the user should provide, the `print` statement would happen afterwards. I'm sure there is a simple fix to this problem, but I do not currently have this solution. While I was not able to ask the user how long they wanted their password, it did simplify the code because I did not have to account for user input or the errors that can come along with that.
2. Given the issues I had at the start with getting the code to match its python counterpart, I decided to remain simple in implementation. I wanted to remove the need for a password generator followed by a password checker like in the first two versions. These original versions could actually produce passwords that were longer than intended. For example, if you wanted a four character password but it only had numbers and symbols, the password checker would add a lowercase and uppercase letter. This would actually make the password six characters long instead of four characters. In my racket version, I removed the password checker and simply added one random character from each list. This assured that the password had an element from each list without the need to be rechecked. Then, I repeated the process again and added the results into a single list of eight characters. I shuffled this and turned the list into a string. This implementation dramatically reduced complexity and the necessary lines of code while ensuring an equally valid random password.
3. The .rkt filetype does not render appropriately in GitHub. If you click on rpg-v3.rkt, you can look above the file, click on Raw, and this will download a copy that you could view in DrRacket. Otherwise, below you can see the code copied into a text format:

``` racket

(define uppers (string->list "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
(define lowers (string->list "abcdefghijklmnopqrstuvwxyz"))
(define symbols (string->list "!@#$%^&*()[]{}/=?+-_|'`~"))
(define numbers (string->list "0123456789"))

; list -> list
; given an empty list, returns a list of random characters from the four character types
(define (base pass-list)
  (define (list-helper xs ys rand)
    (append xs (list (list-ref ys rand))))
  (begin
    (set! pass-list (list-helper pass-list uppers (random 0 26)))
    (set! pass-list (list-helper pass-list lowers (random 0 26)))
    (set! pass-list (list-helper pass-list numbers (random 0 10)))
    (set! pass-list (list-helper pass-list symbols (random 0 24)))
    pass-list))

; function -> string
; given a function that works with lists, returns a shuffled list that is changed to a string
(define (final f)
  (list->string (shuffle (append (f null) (f null)))))

(final base)

```

# Version 4

Version 4 is written in JavaScript and has a similar style to version 3. I could not get user input to work so I had to set the password to a fixed length of 8 characters. Like v3, this allowed me to skip creating a function to accept user input. When I was researching built-in functions, I couldn't find a functions that did what I wanted for two components: truly randomizing a list and changing a list to a string. Because of this, I had to create my own way of converting a list to a string, which took up more space. For the shuffle algorithm, I used the Fisher-Yates algorithm which is supposed to be a way of truly randomizing a list. This algorithm was written long ago, so I borrowed the common implementation and stored it under the function name `shuffle`.
One component that sets this version apart from the rest was the use of the `map` concept, which is similar to a Python dictionary.

``` javascript

const types = new Map([
    [0, uppers],
    [1, lowers],
    [2, symbols],
    [3, numbers]
])

```

By creating this link, I was able to refer to the different character strings by the number 0, 1, 2, or 3. After generating a random character, the reference to the character strings was incremented and a random number would be applied to each character string in turn. This allowed me to be certain that any password of four or more characters has at least on of each character type without the need to check after the fact.

``` javascript

const generatePassword = (len) => {
    let n = 0 // n allows function to loop through types map
    let tempStr = ""
    let tempChar = ""
    let passList = []
    while (len > 0) {
	if (n > 3) {
	    n = 0
	}
	tempStr = types.get(n)
	tempChar = tempStr[Math.floor(Math.random() * tempStr.length)]
	passList.push(tempChar)
	n++
	len--
    }
    return passList

```

The only extra requirement was to shuffle the list of characters after they had been generated to make sure that they did not form a pattern. The downside of this approach is that if a hacker knew the length n of the password, they could tell that n/4 elements were of each type of character. However, given that you couldn't determine the location of the elements because of shuffling, it should not present a security threat. 