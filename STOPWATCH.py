# template for "Stopwatch: The Game"
import simplegui
integer=0
count_stop=0
count_win=0


# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    d=t%10
    c=(t/10)%10
    a=t//600
    b=(t-(a*600))//100
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Reset():
    global integer, count_stop,count_win
    integer=0
    count_win=0 
    count_stop=0
    if timer.is_running():
        timer.stop()
    
def Stop():
    global running, count_stop, count_win,integer
    
    if timer.is_running():
        count_stop+=1
    if (integer%10)==0:
        count_win+=1
    timer.is_running() ==False      
    timer.stop()  
          
    
def Start():
   
    timer.is_running() ==True  
    timer.start()   

# define event handler for timer with 0.1 sec interval

def timer_interval():
    global integer
    integer+=1      

# define draw handler

def draw_canvas(canvas):
    global integer,count_stop,count_win
    int=format(integer)
    cou=str(count_stop)
    cou_win=str(count_win)
    canvas.draw_text(int, (100, 100), 50, 'Red')
    canvas.draw_text(cou_win+"/" +cou, (265, 18), 18, 'Red')
    
# create frame
frame=simplegui.create_frame("StopWatch, the game", 300, 200)
frame.set_draw_handler(draw_canvas)
frame.set_canvas_background('White')
button1=frame.add_button("Reset the watch", Reset)
button2=frame.add_button("Stop the watch", Stop)
button3=frame.add_button("Start the watch", Start)
timer = simplegui.create_timer(100, timer_interval)
# register event handlers


# start frame
frame.start()



# Please remember to review the grading rubric
