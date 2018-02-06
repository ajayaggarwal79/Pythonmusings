# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
global secret_number
global guesses
global range
range=100
secret_number=0
guesses=0


# helper function to start and restart the game
def new_game():
    global secret_number
    global guesses
    secret_number=random.randrange(0,range)
    
    if range==100:
        guesses=7
    elif range==1000:
        guesses=10
    
    print "New game. Range is", "[0,", str(range) +")"
    print "Number of guesses is", str(guesses)
    print
    

# define event handlers for control panel
def range100():
    global range
    range=100
    new_game()
    

def range1000():
    global range
    range=1000
    new_game()
   
    
def input_guess(guess):
    # main game logic goes here
    win=False
    
    global guesses
    #print secret_number
    numerical_guess=int(guess)
    output=" "
    print "Guess was", guess
    guesses=guesses-1
    print "Number of remaining guesses is", str(guesses)
    
    if numerical_guess==secret_number:
        win=True
    elif numerical_guess<secret_number:
        output="Higher!"
    elif numerical_guess>secret_number:
        output="Lower!"
        
    if win is True:
        print("Congrats, you have guessed correctly")
        print
        new_game()
    elif guesses==0:
        print
        print'You ran out of guesses. The number was',str(secret_number)
        print
        new_game()
    else:
        print(output)
    
           
  
    
# create frame
frame=simplegui.create_frame("Guess the number",250,250)

inp=frame.add_input("Enter your guess",input_guess,100)
inp1=frame.add_button('Range is [0,100)', range100)
inp2=frame.add_button('Range is [0,1000)', range1000)

# register event handlers for control elements and start frame

frame.start()


# call new_game 
new_game()

