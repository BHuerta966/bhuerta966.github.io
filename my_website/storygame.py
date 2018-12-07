import time
# Brenda is a quiet, isolated student who attends The Palmdale Aerospace Academy in 2018 Palmdale, California. 
#Her life changes forever when she discovers the school's secret-- a majestic, sophisticated skeleton from the "other world" 
#that lives in a broom closet.  
def Bone():
    print ('You are Brenda Marrow, a TPAA Scholar.')
    time.sleep(1)
    print ('You have just exited from your second class with Ms. Breight.')
    time.sleep(1)
    print ('You have every class with Ms. Breight as your teacher except for 6th period with Brophy, Breights rival.')
    time.sleep(1)
    print ('You have no idea how this happened.')
    time.sleep(1)
    print ('But Breight made it possible after you reluctantly agreed to join Girl Code before the idea sort of died.')
    time.sleep(3)
    print ('    _____ _                               __  ______                   ___  ___ ')                            
    print ('   /  ___| |                             / _| | ___ \                  |  \/  |  ')                           
    print ('   \ `--.| |__   __ _ _ __   ___    ___ | |_  | |_/ / ___  _ __   ___  | .  . | __ _ _ __ _ __ _____      __ ')
    print ("    `--. \ '_ \ / _` | '_ \ / _ \  / _ \|  _| | ___ \/ _ \| '_ \ / _ \ | |\/| |/ _` | '__| '__/ _ \ \ /\ / / ")
    print ('   /\__/ / | | | (_| | |_) |  __/ | (_) | |   | |_/ / (_) | | | |  __/ | |  | | (_| | |  | | | (_) \ V  V / ')
    print ('   \____/|_| |_|\__,_| .__/ \___|  \___/|_|   \____/ \___/|_| |_|\___| \_|  |_/\__,_|_|  |_|  \___/ \_/\_/  ')
    print ('                   | |                                                                                    ')
    print ('                   |_|                                                                                    ')
    time.sleep(2)
    print('Before leaving the second floor of the school, you hear a loud thump.')
    choice=raw_input('After surveying your surroundings, you hear an even louder thump. Do you ignore the sound and go to Bridge?(Y/N)')    
    while choice != 'Y' and choice != 'N':
        choice=raw_input('Stop messing around. The only choices are Y or N. Try Again (Y/N)')
    if choice == 'Y':
        print('Your forget about the weird sound and go to your Bridge Class.')
        time.sleep(1)
        print('You join the rest of Girl Code while they discuss ideas of how to revive Girl Code.')
        time.sleep(1)
        print('Bad End 1: Missed Opportunity')
        return
    else: #you chose'N'
        print('You decide that "Girl Code Meetings" are a waste of time and search for the source of the startling noise.')
        time.sleep(1)
        print('You check almost every class for the noise; after some time, you begin to lose hope.')
        choice=raw_input('BUT WAIT!!!The closet next to you makes the same unmistakeable sound. Do you open the closet door?(Y/N)')
        while choice != 'Y' and choice != 'N':
            choice=raw_input('Stop messing around. The only choices are Y or N. Try Again (Y/N)')
        if choice == 'N':
            print('Well, that was a waste of time.')
            time.sleep(1)
            print('You were too scared to open the door so you back up too much and fall of the second floor.')
            time.sleep(1)
            print('You are dead.')
            time.sleep(1)
            print('Bad End 2: Waste of Time')
            return
        else:
            print('You hesiantly open the door and witness a beautiful sight. A lovely skeleton, wrapped in a plastic sheet, turns to you and gasps.')    
            time.sleep(1)
            print('You panic and stumble back, but skeleton-senpai touches your forehead with its hand.You can see everything.')      
            time.sleep(1)
            print('All the pain and suffering that this poor yet beautiful skeleton has gone through.')
            time.sleep(1)
            print('You find out its name, which is Samuel btw, and how the students have been tormenting it with fortnite dances.')
            choice=raw_input('Do you help Samuel escape?(Y/N)')
            while choice != 'Y' and choice != 'N':
                choice=raw_input('Stop messing around. The only choices are Y or N. Try Again (Y/N)')
            if choice == 'N':
                print('YOU HEARTLESS PERSON! YOU ARE NOT GOING TO HELP THIS POOR SKELETON???!? DO YOU NOT REALIZE HOW INHUMAN YOU ARE RIGHT NOW! YOU ARE GOING TO LET THIS SKELETON BE TORTURED WITH FORTNITE DANCES?!?!?! FINE, Be that way! I quit!')
                time.sleep(1)
                print('Bad End 3: Narrator Quits')
                return
            else:
                print("You grab a blanket to place over the skeleton and place your 'friend' on the janitor's cart . You push it out of the closet, but  you feel a hand on your shoulder.")
                time.sleep(1)
                print('You turn around and the hand belongs to Zebersky, a fellow student and Russian Spy.(She is also dressed as Young Stalin btw.) She pulls you by the arm and takes you to a safer location.')
                time.sleep(1)
                print('She tells you that she was sent by Brophy to kill the skeleton so GIRL CODE could never be revived again.(The skeleton is somehow involved with Girl Code.) He wanted to replace it with Girffins in Real Life Coding.')
                time.sleep(1)
                print('But, Zebersky had a change of heart and decides to help you escape with the secret.BUT OUT OF NOWHERE, BREIGHT SHOWS UP WITH YOUR GIRL CODE TEAM MEMBERS.')
                time.sleep(1)
                print('She challenges you to a duel with a  Quadratic formula sword. She kicks another sword towards you. The spy pulls out colorful gears.')
                choice=raw_input('Are you going to fight?(Y/N)')
                while choice != 'Y' and choice != 'N':
                    choice=raw_input('Stop messing around.The only choices are Y or N. Try Again (Y/N)')
                if choice== 'Y':
                    print('Since this game follows pokemon battle mechanics, all of the members inculding BREIGHT attacks.')
                    time.sleep(2)
                    for GirlCode in ['GIRL1','GIRL2','Breight']:
                        print('The '+GirlCode+' attacks you...she misses.')
                        time.sleep(3)
                    print('Zebersky throws gears at Breight while you swing randomly at her until you finally are able to strike her blade. It breaks in half and Breight is left in shock.')
                    time.sleep(1)
                    print('You run out of the school with the skeleton in your arms, in bridal style duh, and Zebersky follows you. She notices that you are having a moment with your skeleton friend so she salutes at you and dissapears into the night. You look at Samuel and kiss its forhead. ')
                    time.sleep(1)
                    print('Good End:The Shape of Bone Marrow.')
                    return
                else:
                    print("You throw your Brophy plushie at Breight and run away with Samuel. Zebersky catches up with you and salutes at you as she disappears into the night. (you don't know why so much time passed while in the closet but it is now night time, okay?) You turn to your lovely skeleton friend and you realize that it isn't alive.  ")
                    time.sleep(1)
                    print('Normal End: Stolen Property?')
                    return
                    
        
        
        
        
        
        
        
        
        