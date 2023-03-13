# Project Overview

The purpose of this 'cipher project' is to implement several different common ciphers that can encrypt or decrypt a given text. None of these ciphers are new. They all have been written many times before by many others. Instead of originality, I am setting out to write these ciphers in order to get practice with writing Python. Where possible, I will try to add my own flair. I hope to end up with several different ciphers that I can combine into either a module or package to get practice with making different files work together. I also hope to allow two different methods of interaction:
    1. inserting text manually by typing or copying and pasting into the terminal and recieving the results in the terminal.
    2. providing the name of the file that I want encrypted/decrypted and getting the output sent to another file.
I may also include the code necessary to break these codes. As a disclaimer, I am writing this project in the same order as the book that I am following to write this code - "Cracking Codes with Python" by Al Sweigart. He teaches Python in this book by showing his way of implementing certain ciphers. While I will consult his solutions, I will ultimately be writing my own and not simply copying his. I appreciate his desire to help others learn Python by providing many of his books for free online at inventwithpython.com. 

# Ciphers Included

| Cipher Name    | Description |
| --- | --- |
| Reverse Cipher | Does not change any element of the message. Simply reverses the elements in the message. For this reason, the same function can perform both encryption and decryption. |

# Reverse Cipher

The `reverse_cipher()` function is relatively simple and works by going from the end of the message and working towards the beginning. 

``` python
def reverse_cipher(message):
    new_message = ""
    i = len(message) - 1
    while i >= 0:
        new_message += message[i]
        i -= 1
    return new_message
```

##### Usage

Here is the message before being inserted into the reverse cipher:

> "Here is a good example of the reverse cipher at work. Notice that the inclusion of punctuation (like ! or . or ?) is a dead give-away that the message is simply backwards."

Here is the result:

> '.sdrawkcab ylpmis si egassem eht taht yawa-evig daed a si )? ro . ro ! ekil( noitautcnup fo noisulcni eht taht ecitoN .krow ta rehpic esrever eht fo elpmaxe doog a si ereH'

If you wanted to decrypt that same message, you get the same as the original:

> "Here is a good example of the reverse cipher at work. Notice that the inclusion of punctuation (like ! or . or ?) is a dead give-away that the message is simply backwards."

##### Second Version

While the reverse cipher can trick the eyes for a quick moment, I personally think that it is a dead give-away to have either punctuation or capital letters. I decided to create a second version of the reverse cipher called `reverse_without_punctuation()` that drops all punctuation and makes all letters lowercase. This is even harder for the eyes to detect what is going on. Only by going character by character can someone catch a pattern in a unique common word and realize that the message is just backwards. This solution requires `import string` in the file.

``` python
def reverse_without_punctuation(message):
    new_message = ""
    i = len(message) - 1
    while i >= 0:
        if message[i] in string.ascii_letters:
            new_message += (message[i]).lower()
        i -= 1
    return new_message
```

Here is the next message before being inserted:

> 'This reverse function removes punctuation and makes sure all characters are lowercase. In my opinion, this makes the cipher less obvious. The side effect is that decrypting the message results in a message without punctuation or spaces. This is harder to read than usual but still doable.'

As you can see, the result of the encryption does not immediately gives itself away and could possibly be interpreted as a series of random characters if not observed closely:

> 'elbaodllitstublausunahtdaerotredrahsisihtsecapsronoitautcnuptuohtiwegassemanistluseregassemehtgnitpyrcedtahtsitceffeedisehtsuoivbosselrehpicehtsekamsihtnoinipoymniesacrewolerasretcarahcllaerussekamdnanoitautcnupsevomernoitcnufesreversiht'

The only problem with this method is that on decryption the message still does not have punctuation. The words run together. While this is an unfortunate side effect, I believe that it is worth the extra chance that someone wouldn't be able to understand the encrypted message:

> 'thisreversefunctionremovespunctuationandmakessureallcharactersarelowercaseinmyopinionthismakesthecipherlessobviousthesideeffectisthatdecryptingthemessageresultsinamessagewithoutpunctuationorspacesthisishardertoreadthanusualbutstilldoable'
