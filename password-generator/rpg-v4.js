/* 
Title: Random Password Generator, v4
Description: Creates random password; written in javascript
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
*/


const uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
const lowers = "abcdefghijklmnopqrstuvwxyz"
const symbols = "!@#$%^&*()[]{}/=?+-_|'`~"
const numbers = "0123456789"

// maps the different types of characters to different numbers
const types = new Map([
    [0, uppers],
    [1, lowers],
    [2, symbols],
    [3, numbers]
])
// the total length of the password can be changed here
const passLength = 8

/**
list -> list
given a list of values, returns a randomized list with the same values
shuffle via fisher-yates algorithm
*/
const shuffle = (pass) => {
    for (let i = pass.length - 1; i > 0; i--) {
	const j = Math.floor(Math.random() * (i + 1))
	const temp = pass[i]
	pass[i] = pass[j]
	pass[j] = temp
    }
    return pass
}

/**
list, string -> string
given a list of values and an empty string (acc), returns a string of all the
combined values in the list
*/
const listToString = (list, acc) => {
    for (let i = 0; i < list.length; i++) {
	acc += list[i]
    }
    return acc
}

/**
number -> list
given the length of the desired password, returns a list of random values.
any password of 4 or more characters is guaranteed to have at least one or
more of each character type
*/
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
}

const main = () => {
    return listToString(shuffle(generatePassword(passLength)), "")
}

console.log(main())
