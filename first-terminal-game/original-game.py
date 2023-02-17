#the game options will always start here
def starting_screen():
    init_input = input("Do you dare continue? If you would like to play, type 'yes'. Type 'no' to end the game: ")
    if init_input.lower() == "yes":
        scenario_1()
    elif init_input.lower() == "no":
        print("Game Over")
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        starting_screen()

#this is the screen that the player goes to when they lose the game
def game_over_screen():
    print(" ")
    print("""
    {{{{{}  {{{{{}  {}  {}  {{{{{}    {{{{{}  {}  {}  {{{{{}  {{{{{}
    {}      {}  {}  {}{}{}  {}        {}  {}  {}  {}  {}      {}  {}
    {} {{}  {{{{{}  {}  {}  {{{{{}    {}  {}  {}  {}  {{{{{}  {{{{}
    {}  {}  {}  {}  {}  {}  {}        {}  {}   {}{}   {}      {}  {}
    {{{{{}  {}  {}  {}  {}  {{{{{}    {{{{{}    {}    {{{{{}  {}  {}
    """)
    print(" ")
    user_input = input("Would you like to play again? If so, type 'yes'. If not, type 'no'. If you have already lost several times and you would like a cheat code, type 'cheat'. If you want to know the correct series of answers, type 'answers': ")
    if user_input.lower() == "yes":
        scenario_1()
    elif user_input.lower() == "no":
        print("Thanks for playing!")
    elif user_input.lower() == "cheat":
        print(" ")
        print("To use the cheat code, type 'run away' in the first scene when you hear a yell down the hallway.")
        scenario_1()
    elif user_input.lower() == "answers":
        print(" ")
        print("The answers in order are: 'wait', 'stay', 'run', 'away', 'ball'. If you type these answers in this order, you should win the game.")
        scenario_1()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        game_over_screen()

#this is the screen that the player goes to when they win the game
def game_win_screen():
    print(" ")
    print("Congratulations. You won! You successfully completed the day as a nurse.")
    print("""
                 {{{{}   {{{{}  {}  {}
                 {}  {}  {{     {}  {}
                 {{{{}   {{{}    {}{}
                 {}  {}  {{     {}  {}
                 {{{{}   {{{{}  {}  {} Rx

                                   [[[
                 [[[[[[[[[[[[[[[[[[[[[     [[
    <============[[[[[[[[[[[[[[[[[[[[[[[[[[[[
                 [[[[[[[[[[[[[[[[[[[[[     [[
                                   [[[    
 
  """)
    user_input = input("Would you like to play again? If so, type 'yes'. If not, type 'no': ")
    if user_input.lower() == "yes":
        scenario_1()
    else:
        print("Game Over")

#scenario 1 leads to scenario 2 with "wait" option, to scenario 3 with "investigate" option, or to a secret win by typing "run away"
def scenario_1():
    print(" ")
    print("When you lift your head off the keyboard, you hear a scream down the hallway. What do you do?")
    user_input = input("Type 'wait' if you want to wait to see what happens. Type 'investigate' to go investigate the noise: ")
    if user_input.lower() == "wait":
        scenario_2()
    elif user_input.lower() == "investigate":
        scenario_3()
    #this next line is a cheat code to automatically win the game.
    elif user_input.lower() == "run away":
        game_win_screen()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_1()

#scenario 2 leads to a loss for "help" option or to scenario 4 with "stay" option
def scenario_2():
    print(" ")
    print("A naked man runs out of the room where you heard the screaming. There is blood running down his neck and a wild look in his eyes. What do you do?")
    user_input = input("Type 'help' if you want to go help the naked man. Type 'stay' if you want to stay where you are to see what happens next: ")
    if user_input.lower() == "help":
        print(" ")
        print("When you try to stop his neck from bleeding, the man thinks you are trying to choke him and he returns the favor. The other nurses weren't able to help you in time.")
        game_over_screen()
    elif user_input.lower() == "stay":
        scenario_4()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_2()

#each option in scenario 3 leads to a loss
def scenario_3():
    print(" ")
    print("You run toward the direction of the yelling. A naked, bloody man jumps out of nowhere and grabs you. What do you do?")
    user_input = input("Type 'get away' to try to get away. Type 'push' to push the man away: ")
    if user_input.lower() == "get away":
        print(" ")
        print("You try to get away. This sends the man into a rage. He attacks you and you need one week in intensive care.")
        game_over_screen()
    elif user_input.lower() == "push":
        print(" ")
        print("You push the man away and he stumbles through a glass door. The manager and security arrive just in time to see this. You're going to jail.")
        game_over_screen()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_3()
        
#scenario 4 leads to scenario 5 with "run" option or to scenario 6 with "call" option
def scenario_4():
    print(" ")
    print("You stay where you are to see what happens. You see another nurse go toward the yelling and suddenly, a naked, bloody man jumps out and grabs her. What do you do?")
    user_input = input("Type 'run' to run over to the other nurse and help her. Type 'call' to call security from the nearest phone: ")
    if user_input.lower() == "run":
        scenario_5()
    elif user_input.lower() == "call":
        scenario_6()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_4()

# scenario 5 leads to scenario 7 with "away" option or to game over with "dive" option
def scenario_5():
    print(" ")
    print("You run over toward the scene and yell at the naked man to get his attention. Now that you have his attention, what do you do?")
    user_input = input("Type 'away' to run away from the man. Type 'dive' to dive into a nearby medical closet that you see: ")
    if user_input.lower() == "away":
        scenario_7()
    elif user_input.lower() == "dive":
        print(" ")
        print("You dive into a medical closet but a rack of oxygen tanks falls on you and crushes you.")
        game_over_screen()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_5()

# each option in scenario 6 leads to a loss
def scenario_6():
    print(" ")
    print("You call security. Within minutes, ten people are holding the man down in the hallway. What do you do?")
    user_input = input("Type 'medicine' to go grab the medicine to sedate the man. Type 'hold' to help hold the man down with the others: ")
    if user_input.lower() == "medicine":
        print(" ")
        print("You grab the medicine and give it to the man. In the rush, you had accidentally grabbed a paralytic, causing the man to stop breathing. You are sued for negligence.")
        game_over_screen()
    elif user_input.lower() == "hold":
        print(" ")
        print("You hold the man down with the other people while another nurse grabs the medicine. The naked man moves at the last second and the needle goes into your hand on accident. All of the medicine is given. You pass out and need close monitoring in the emergency room for several hours.")
        game_over_screen()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_6()
    
# scenario 7 leads to a loss with the "judo" option or scenario 10 with the "ball" option
def scenario_7():
    print(" ")
    print("As you run away, the man's last dose of meth kicks in and he is now much faster than you. What do you do?")
    user_input = input("Type 'judo' to judo kick. Type 'ball' to curl into a ball on the floor: ")
    if user_input.lower() == "judo":
        print(" ")
        print("You successfully land the judo kick and bust the man's jaw. Later in the day you get busted by the feds. You lost your license and are a convicted felon.")
        game_over_screen()
    elif user_input.lower() == "ball":
        print(" ")
        print("You curl into a ball on the floor and sustain minimal damage. The naked man is brought to jail. Now that there is extra space on the unit, prepare yourself to get your next patient. At least there's no way the new patient will be as crazy as that last guy, right? ..........")
        game_win_screen()
    else:
        print(" ")
        print("There was an error. Please try again and check your spelling.")
        scenario_7()
    
print("You lift your head off your keyboard and realize you're still at work. Welcome to a day in the life of a nurse.")
starting_screen()