from tkinter import *
import random
import pywhatkit

width, height = 500, 250

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

def OPEN_WHATSAPP():
    a = pywhatkit.sendwhatmsg_instantly('+91 9312422987', 'Hey! Thanks for making this game but I would like to give some suggestions so that this game can be improved well \n 1. <Suggestion 1> \n 2. <Suggestion 2> \n 3. <Suggesstion 3>', 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    print(a)


def START_GAME():

    options = ['Rock', 'Paper', 'Scissors']
    a = random.choice(options)


    width = 500
    height = 250

    def PRINT_COMPUTER_CHOICE():
        COMPUTER_CHOICE_LABEL = Label(Sparsh_Root, text = f"Computer chose {a}", font = ('Poppins 15 underline'))
        COMPUTER_CHOICE_LABEL.pack()

    def SHOW_RESULT_IF_USER_CHOOSES_ROCK():
        if a.lower() == 'rock':
            TIED = Label(Sparsh_Root, text = f"Computer chose {a} and you also chose rock. \n Hence it is a tie!", font = ('Bahnschrift', 15))
            TIED.pack(side = BOTTOM)
        elif a.lower() == 'paper':
            YOU_LOSE = Label(Sparsh_Root, text = f"Computer chose {a} and you chose rock. \n Hence you lose!", font = ('Bahnschrift', 15))
            YOU_LOSE.pack(side = BOTTOM)
        elif a.lower() == 'scissors':
            YOU_WIN = Label(Sparsh_Root, text = f"Computer chose {a} and you chose rock. \n Hence you win!", font = ('Bahnschrift', 15))
            YOU_WIN.pack(side = BOTTOM)

    def SHOW_RESULT_IF_USER_CHOOSES_PAPER():
        if a.lower() == 'rock':
            YOU_WIN_2 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose paper. \n Hence you win!", font = ('Bahnschrift', 15))
            YOU_WIN_2.pack(side = BOTTOM)
        elif a.lower() == 'paper':
            TIED_2 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose paper. \n Hence it is a tie!", font = ('Bahnschrift', 15))
            TIED_2.pack(side = BOTTOM)
        elif a.lower() == 'scissors':
            YOU_LOSE_2 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose paper. \n Hence you lose!", font = ('Bahnschrift', 15))
            YOU_LOSE_2.pack(side = BOTTOM)
    def SHOW_RESULT_IF_USER_CHOOSES_SCISSORS():
        if a.lower() == 'rock':
            YOU_LOSE_3 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose scissors. \n Hence you lose!", font = ('Bahnschrift', 15))
            YOU_LOSE_3.pack(side = BOTTOM)
        elif a.lower() == 'paper':
            YOU_WIN_3 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose scissors. \n Hence you win!", font = ('Bahnschrift', 15))
            YOU_WIN_3.pack(side = BOTTOM)
        elif a.lower() == 'scissors':
            TIED_3 = Label(Sparsh_Root, text = f"Computer chose {a} and you chose scissors. \n Hence it is a tie!", font = ('Bahnschrift', 15))
            TIED_3.pack(side = BOTTOM)


    Sparsh_Root = Tk()
    Sparsh_Root.title("Main")
    Sparsh_Root.geometry("1280x720")

    TITLE_LABEL = Label(Sparsh_Root, text = "Rock, Paper and Scissors By Sparsh", font = ('Algerian 19 bold italic underline'))
    TITLE_LABEL.pack()

    SELECT_YOUR_CHOICE_LABEL = Label(Sparsh_Root, text = "Select your choice : ", font = ('Bahnschrift', 15))
    SELECT_YOUR_CHOICE_LABEL.pack()

    SELECT_ROCK_BUTTON = Button(Sparsh_Root, text = "ROCK", bg = 'red', fg = 'black', activebackground = "blue", font = ('Bahnschrift'), command = SHOW_RESULT_IF_USER_CHOOSES_ROCK)
    SELECT_ROCK_BUTTON.pack()

    SELECT_SCISSORS_BUTTON = Button(Sparsh_Root, text = "SCISSORS", bg = 'red', fg = 'black', activebackground = "blue", font = ('Bahnschrift'), command = SHOW_RESULT_IF_USER_CHOOSES_SCISSORS)
    SELECT_SCISSORS_BUTTON.pack()

    SELECT_PAPER_BUTTON = Button(Sparsh_Root, text = "PAPER", bg = 'red', fg = 'black', activebackground = "blue", font = ('Bahnschrift'), command = SHOW_RESULT_IF_USER_CHOOSES_PAPER)
    SELECT_PAPER_BUTTON.pack()

    KINDLY_NOTE_LABEL = Label(Sparsh_Root, text = "KINDLY NOTE THE FOLLOWING THINGS!", font = ('Bahnschrift 17 bold'))
    KINDLY_NOTE_LABEL.pack()

    NOTE_ON_CLICKING_THE_BUTTON_LABEL = Label(Sparsh_Root, text = "When you click on one the above options then whatever you and computer \n have chosen will be displayed along with the result.", font = ('Bahnschrift', 15))
    NOTE_ON_CLICKING_THE_BUTTON_LABEL.pack()

    TO_PLAY_AGAIN_LABEL = Label(Sparsh_Root, text = "Also, if you want to play again then exit the game and \n click on the play game button again.", font = ('Bahnschrift 15 italic'))
    TO_PLAY_AGAIN_LABEL.pack()

    EXIT_THE_GAME_BUTTON = Button(Sparsh_Root, text = "EXIT GAME!", bg = 'red', fg = 'black', activebackground = 'blue', font = ('Bahnschrift', 20), command = Sparsh_Root.destroy)
    EXIT_THE_GAME_BUTTON.pack(side = BOTTOM)

    Sparsh_Root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------


root = Tk()
root.title("Main")
root.geometry("640x360")

PLAY_GAME_BUTTON = Button(root, text = "PLAY GAME!", bg = "red", fg = 'black', activebackground = 'blue', font = ('Bahnschrift',20), command = START_GAME)
PLAY_GAME_BUTTON.pack()

CLICK_ON_THE_ABOVE_BUTTON_TO_PLAY_LABEL = Label(root, text = "Click on the above button to play the game!", font = ('Bahnschrift',15))
CLICK_ON_THE_ABOVE_BUTTON_TO_PLAY_LABEL.pack()

EXIT_GAME_BUTTON = Button(root, text = "EXIT GAME!", bg = 'red', fg = 'black', activebackground = 'blue', font = ('Bahnschrift', 20), command = root.destroy)
EXIT_GAME_BUTTON.pack()

CLICK_ON_THE_ABOVE_BUTTON_TO_EXIT_LABEL = Label(root, text = "Click on the above button to exit the game!", font = ('Bahnschrift',15))
CLICK_ON_THE_ABOVE_BUTTON_TO_EXIT_LABEL.pack()

IMPROVEMENTS_LABEL = Label(root, text = "Any improvements? Click on the above button to go to the whatsapp!", font = ('Bahnschrift', 15))
IMPROVEMENTS_LABEL.pack(side = BOTTOM)

OPEN_WHATSAPP_BUTTON = Button(root, text= "OPEN WHATSAPP", bg = 'red', fg = 'black', activebackground = 'blue', font = ('Bahnschrift', 20), command = OPEN_WHATSAPP)
OPEN_WHATSAPP_BUTTON.pack(side = BOTTOM)

CREATED_BY_SPARSH_LABEL = Label(root, text = "Created By Sparsh", font = ('Arial Black', 25))
CREATED_BY_SPARSH_LABEL.pack(side = BOTTOM)

root.mainloop()

