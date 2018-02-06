# RPLS
import simplegui 
import random



# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    function to convert the name the user inputs to the number
    """
    
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
         return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        return "Not a valid input"
 
 
#print(name_to_number("rock"))
#print(name_to_number("Spock"))
#print(name_to_number("paper"))
#print(name_to_number("lizard"))
#print(name_to_number("scissors"))
#print(name_to_number("test"))

def get_input(name):
    
    return (rpsls(name))


def number_to_name(number):
    """
    function to convert the number that the comput generates to the name for
    output purposes
    """
    
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"        
    elif number==4:
        return "scissors"
    else:
        return "Not a valid input"
    
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)


def rpsls(player_choice): 
    """ 
    Function to return meesages to the player anc omputer about there choices
    and to calculate the winner
    """
    
    # present the player choice to the player
    print "Player chooses " + player_choice 
    player_number=name_to_number(player_choice)
    #computer random choice
    computer_number=random.randrange(0,5) 
    print "Computer chooses " + number_to_name(computer_number) 
    # modulus difference between computer and player
    difference=(computer_number-player_number)%5
    
    if difference ==0:
        print "Player and computer tie!"
    elif difference==1 or difference==2:
        print "Computer wins!"
    elif difference==3 or difference==4:
        print "Player wins!"

 
    print("")


    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")


frame=simplegui.create_frame('RPSL',100,100)
inp=frame.add_input('Label', get_input, 100)
frame.start()


# always remember to check your completed program against the grading rubric


