'''
Title: Random Password Generator, v.1
Description: Creates a random password from 4 to 15 characters long.
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding

\\......//\\......//\\......//\\......//\\......//\\......//\\......//\\......//
 \\....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....// 
\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /
 \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// / 
> | || | <> | || | <> |                                     > | || | <> | || | <  
> | || | <> | || | <> | ||                          ||   // > | || | <> | || | <
 /  /\  \  /  /\  \  /  ||                          ||  //   /  /\  \  /  /\  \ 
/  /  \  \/  /  \  \/   ||____       ___      ___   || //   /  /  \  \/  /  \  \
  | <> | || | <> | ||   ||    \\   //   \\  //   \\ ||||    | | <> | || | <> | |
  | <> | || | <> | ||   ||     || ||____|| ||       || \\   | | <> | || | <> | |
   \  /  ||  \  /  ||   ||     || ||       ||       ||  \\  |  \  /  ||  \  /  | 
\\  \/  //\\  \/  //\\  ||____//   \\___//  \\___// ||   \\ \\  \/  //\\  \/  //
.\\    //..\\    //..\\                                      \\    //..\\    //.
..\\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //..
...\\//......\\//......\\//......\\//......\\//......\\//......\\//......\\//...


'''

import string
import random

uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
nums = string.digits
symbs = string.punctuation

def check_input(user_input):
    '''
string -> int
given the desired password length, return an int version of the input
or if the input is invalid, return the int 8 
    '''
    try:
        user_input = int(user_input) 
    except:
        return 8
    else:
        if 4 <= user_input <= 15:
            return user_input
        else:
            return 8

def random_item():
    '''
() -> string
selects a random character type and returns a random element from it
    '''
    choice_type = random.choice([uppers, lowers, nums, symbs])
    return random.choice(choice_type)

def create_password(n, password):
    '''
int, string -> string
given the desired length of the password (n) and an empty string,
returns a password with the chosen length
    '''
    if n <= 0:
        return password
    else:
        return create_password(n - 1, random_item() + password)

def pass_checker(password, up, low, num, sym):
    '''
string, int, int, int, int -> list of ints
given the preliminary password and an accumulator for each group of character
type, returns a list that shows how much each category was used
    '''
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

def modify(mod, check_list):
    '''
string, list of ints -> string
given the preliminary password and a list that shows how many times each
category is used, returns the original password if all categories are present
or adds any desired character that is missing
    '''
    if check_list[0] == 0:
        mod += random.choice(uppers)

    if check_list[1] == 0:
        mod += random.choice(lowers)

    if check_list[2] == 0:
        mod += random.choice(nums)

    if check_list[3] == 0: 
        mod += random.choice(symbs) 
    return mod

def main():
    set_length = check_input(input('''
Enter the desired password length or press enter for an 8 digit password: '''))
    prelim = create_password(set_length, "")
    check = pass_checker(prelim, 0, 0, 0, 0)
    if 0 in check:
        return modify(prelim, check)
    else:
        return prelim

if __name__ == "__main__":
    print(main())
