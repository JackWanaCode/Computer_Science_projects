import tkinter
import random

colors = ['Red','Blue','Green','Pink','Black',
          'Yellow','Orange','White','Purple','Brown']

score = 0

timeleft = 30

def startGame(event):

    if timeleft == 30:
        countdown()

    nextColor()

def nextColor():
    global score
    global timeleft
    # if a game is currently play
    if timeleft > 0:
        #make the text entry box active
        e.focus_set()
        #if the clour typed is equal to the color of the text
        if e.get().lower() == colors[1].lower():
            score += 1
        #clear the text entry box
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        #change the color to type, by changing the text and
        #the color to a random color value
        label.config(fg=str(colors[1]), text=str(colors[0]))
        #update the score
        scoreLabel.config(text="Score: " + str(score))

#Countdown time function
def countdown():
    global  timeleft
    #if a gamve is in play
    if timeleft > 0:
        timeleft -= 1
        #update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("374x200")
#add an instruction label
instructions = tkinter.Label(root, text="Type in the color "
                                        "of the words, and not "
                                        "the word text!",
                                        font = ('Helvetica', 12))
instructions.pack()
#add score label
scoreLabel = tkinter.Label(root, text="Press enter to start", font = ('Helvetica', 12))
scoreLabel.pack()
#add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()
#add a label for displaying the colors
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
#add a text entry box for typing in colors
e = tkinter.Entry(root)
#runt the startGame function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
