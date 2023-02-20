#helps run_scene choose whether to run next scenario, give win, or give loss
def win_lose(scn, option):
    if type(option) == list:
        run_scene(option)
    elif type(option) == tuple:
        print(option[0])
        if option[1] == "lose":
            game_over_screen()
        else:
            game_win_screen()

#given a list with scenario options, will exit, take the user to the next scenario, or display an error
def run_scene(scenario):
    print(scenario[0])
    user_input = input(scenario[1])
    user_input = (user_input.strip()).lower()
    if user_input == "x":
        exit()
    elif user_input in scenario[2]:
        win_lose(scenario, scenario[2][user_input])
    else:
        print("\nThere was an error. Please try again and check your spelling.")
        run_scene(scenario)

#displays the initial messages of the game to determine if the user wants to play the game or not
def starting_screen():
    print("You lift your head off your keyboard and realize you're still at work. Welcome to a day in the life of a nurse.")
    init_input = input("Do you dare continue? If you would like to play, type 'yes'. Type 'no' to end the game: ")
    if init_input.lower() == "yes":
        pass
    elif init_input.lower() == "no":
        print("Game Over")
        exit()
    else:
        print("\nThere was an error. Please try again and check your spelling.")
        starting_screen()

            
#displays a losing game message and asks if they want to play again
def game_over_screen():
    print("""\n
    {{{{{}  {{{{{}  {}  {}  {{{{{}    {{{{{}  {}  {}  {{{{{}  {{{{{}
    {}      {}  {}  {}{}{}  {}        {}  {}  {}  {}  {}      {}  {}
    {} {{}  {{{{{}  {}  {}  {{{{{}    {}  {}  {}  {}  {{{{{}  {{{{}
    {}  {}  {}  {}  {}  {}  {}        {}  {}   {}{}   {}      {}  {}
    {{{{{}  {}  {}  {}  {}  {{{{{}    {{{{{}    {}    {{{{{}  {}  {}
   \n """)
    user_input = input("Would you like to play again? If so, type 'yes'. If not, type 'no'. If you have already lost several times and you would like know the correct series of answers, type 'answers': ")
    if user_input.lower() == "yes":
        main()
    elif user_input.lower() == "no":
        print("Thanks for playing!")
    elif user_input.lower() == "answers":
        print("\nThe answers in order are: 'wait', 'stay', 'run', 'away', 'ball'. If you type these answers in this order, you should win the game.\n")
        main()
    else:
        print("\nThere was an error. Please try again and check your spelling.")
        game_over_screen()

#displays the winning message
def game_win_screen():
    print("\nCongratulations. You won! You successfully completed the day as a nurse.")
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
        main()
    else:
        print("Game Over")
        exit()
        
#this is the list of scenarios. there are seven in total. they contain a prompt for the scenario, a message that asks what the user wants to do, and a
#dictionary with the keywords and the results of using those keywords. they are listed in reverse order because
#they refer to the next scene and the next scene has to exist before being referred to
scene7 = ["\nAs you run away, the man's last dose of meth kicks in and he is now much faster than you. What do you do?",
          "Type 'judo' to judo kick. Type 'ball' to curl into a ball on the floor: ",
          {"judo": ("\nYou successfully land the judo kick and bust the man's jaw. Later in the day you get busted by the feds. You lost your license and are a convicted felon.", "lose"), "ball": ("\nYou curl into a ball on the floor and sustain minimal damage. The naked man is brought to jail. Now that there is extra space on the unit, prepare yourself to get your next patient. At least there's no way the new patient will be as crazy as that last guy, right? ..........", "win")}]

scene6 = ["\nYou call security. Within minutes, ten people are holding the man down in the hallway. What do you do?",
          "Type 'medicine' to go grab the medicine to sedate the man. Type 'hold' to help hold the man down with the others: ",
          {"medicine": ("\nYou grab the medicine and give it to the man. In the rush, you had accidentally grabbed a paralytic, causing the man to stop breathing. You are sued for negligence.", "lose"), "hold": ("\nYou hold the man down with the other people while another nurse grabs the medicine. The naked man moves at the last second and the needle goes into your hand on accident. All of the medicine is given. You pass out and need close monitoring in the emergency room for several hours.", "lose")}]

scene5 = ["\nYou run over toward the scene and yell at the naked man to get his attention. Now that you have his attention, what do you do?",
          "Type 'away' to run away from the man. Type 'dive' to dive into a nearby medical closet that you see: ",
          {"away": scene7, "dive": ("\nYou dive into a medical closet but a rack of oxygen tanks falls on you and crushes you.", "lose")}]

scene4 = ["\nYou stay where you are to see what happens. You see another nurse go toward the yelling and suddenly, a naked, bloody man jumps out and grabs her. What do you do?",
          "Type 'run' to run over to the other nurse and help her. Type 'call' to call security from the nearest phone: ",
          {"run": scene5, "call": scene6}]

scene3 = ["\nYou run toward the direction of the yelling. A naked, bloody man jumps out of nowhere and grabs you. What do you do?",
          "Type 'get away' to try to get away. Type 'push' to push the man away: ",
          {"get away":("\nYou try to get away. This sends the man into a rage. He attacks you and you need one week in intensive care.",
                       "lose"), "push":("\nYou push the man away and he stumbles through a glass door. The manager and security arrive just in time to see this. You're going to jail.", "lose")}]

scene2 = ["\nA naked man runs out of the room where you heard the screaming. There is blood running down his neck and a wild look in his eyes. What do you do?",
          "Type 'help' if you want to go help the naked man. Type 'stay' if you want to stay where you are to see what happens next: ",
          {"help":("\nWhen you try to stop his neck from bleeding, the man thinks you are trying to choke him and he returns the favor. The other nurses weren't able to help you in time.", "lose") , "stay": scene4}]

scene1 = ["\nWhen you lift your head off the keyboard, you hear a scream down the hallway. What do you do?",
              "Type 'wait' if you want to wait to see what happens. Type 'investigate' to go investigate the noise: ",
              {"wait": scene2, "investigate": scene3}]

#main game loop
def main():
    starting_screen()
    run_scene(scene1)
           
if __name__ == "__main__":
    main()
