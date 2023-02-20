# My First Python Terminal Game

This is a game written for the command line using python. The original game was written as my first undirected project.

### Premise and Background
---

I wrote this game at my lowest point in my nursing career while taking care of COVID patients in the ICU. The plot is that you have to make it through a day as a nurse while not getting in trouble with your boss or getting attacked by a drunk man. The scenarios played out the way that I felt at the time - that there was no way to make everyone happy or to predict what crazy things would happen in a single day. While things are much better for me now as I revise the code, it is funny to look back on the wacky scenarios that I invented for the game.

This is one of my first programs that I wrote after I learned python. It is written in the style of the earliest computer games: text-based adventure. While there are cooler video games that can be created with graphics, text-based games allow beginning coders to circumnavigate the difficult code that is involved in modern video games and focus on logic - i.e., if you do this thing, some other thing will happen.

I originally wrote the code for this game in May of 2022. This original code is labeled as 'original-game.py' and will remain unchanged from its original form. However, even weeks after writing the program, I learned of better ways of performing some of the tasks within the code. The most obvious example that catches my eye as I look at the original is that I didn't know about 'newline' characters yet. Every time I wanted a new line, I would add a 'print(" ")' statement which could be easily cleaned up by adding '\n' in the given string.

The newer version written in February of 2023 is just one of the ways that I figured that the code could be re-written. This new version is labeled as 'updated-game.py'. Feel free to look at both versions to see how this game changed over time.


### Changes
---

1. Replaced each instance of 'print(" ")' with "\n". This allows a newline without requiring a line of code because the newline character can be written right into the string.
2. Added the if __name__ == "__main__" component at the bottom of the code. This allows automatic starting of the code if it's being run directly.
3. Abstracted scenarios from the function running the scenarios. The original code constantly repeated several components including printing a message, asking for input, cleaning up the input, and checking which scenario to run afterwards. I removed the repitition and created a function to perform all of these tasks along with a helper function. All of the scenario information was put into 7 different lists.
4. The game over screen retained the option for getting all of the answers to win but the cheat code phrase was removed. I felt that two different cheats weren't necessary.