from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Create the main window
window = Tk()
window.title("Rock Paper Scissors")
window.geometry("700x300")
window.configure(background="#1e1e1e")

# Load images
image_rock = ImageTk.PhotoImage(Image.open("Rock.png"))
image_paper = ImageTk.PhotoImage(Image.open("Paper.png"))
image_scissor = ImageTk.PhotoImage(Image.open("Scissor.png"))

# Labels for player and computer
label_player = Label(window, image=image_scissor, bg="#1e1e1e")
label_computer = Label(window, image=image_scissor, bg="#1e1e1e")

label_computer.grid(row=1, column=4, pady=20)
label_player.grid(row=1, column=2, pady=20)

# Score Labels
player_score = Label(window, text="0", font=('arial', 40, "bold"), fg="#00FF00", bg="#1e1e1e")
computer_score = Label(window, text="0", font=('arial', 40, "bold"), fg="#FF4500", bg="#1e1e1e")

player_score.grid(row=1, column=1)
computer_score.grid(row=1, column=5)

# Player and Computer indicators
player_indicator = Label(window, font=("Helvetica", 20, "bold"), text="PLAYER", fg="#00FF00", bg="#1e1e1e")
computer_indicator = Label(window, font=("Helvetica", 20, "bold"), text="COMPUTER", fg="#FF4500", bg="#1e1e1e")

player_indicator.grid(row=0, column=1)
computer_indicator.grid(row=0, column=5)

# Message Label
final_message = Label(window, font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e1e", text="")
final_message.grid(row=1, column=3)


# Function to update the message
def update_message(msg):
    final_message.config(text=msg)


# Update the score
def update_score(winner):
    if winner == "player":
        score = int(player_score["text"]) + 1
        player_score.config(text=str(score))
    elif winner == "computer":
        score = int(computer_score["text"]) + 1
        computer_score.config(text=str(score))


# Check for winner
def check_winner(player, computer):
    if player == computer:
        update_message("It's a Tie!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        update_message("Player Wins!")
        update_score("player")
    else:
        update_message("Computer Wins!")
        update_score("computer")


# Function to update choices
def update_choices(player_choice):
    options = ["rock", "paper", "scissor"]
    computer_choice = options[randint(0, 2)]

    # Update images
    label_player.config(image=image_rock if player_choice == "rock" else
                               image_paper if player_choice == "paper" else
                               image_scissor)
    
    label_computer.config(image=image_rock if computer_choice == "rock" else
                                  image_paper if computer_choice == "paper" else
                                  image_scissor)

    # Check winner
    check_winner(player_choice, computer_choice)


# Buttons with modern styling
button_style = {
    "width": 12,
    "height": 2,
    "font": ("Arial", 15, "bold"),
    "fg": "black",
    "relief": "flat"
}

button_rock = Button(window, text="ROCK", bg="#FF5733", command=lambda: update_choices("rock"), **button_style)
button_paper = Button(window, text="PAPER", bg="#33FF57", command=lambda: update_choices("paper"), **button_style)
button_scissor = Button(window, text="SCISSOR", bg="#3380FF", command=lambda: update_choices("scissor"), **button_style)

button_rock.grid(row=2, column=2, padx=10, pady=20)
button_paper.grid(row=2, column=3, padx=10, pady=20)
button_scissor.grid(row=2, column=4, padx=10, pady=20)

# Run the game loop
window.mainloop()
