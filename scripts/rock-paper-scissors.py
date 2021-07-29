from tkinter import *
import random

# Creating main window
root = Tk()
root.title("Rock, paper, scissors")
root.configure(bg="#fff")
root.resizable(False, False)

frame_choice = Frame(root, bg="#00ff08", padx=20, pady=10)
frame_choice.grid(row=1, column=0, columnspan=4)
count = 0


def display_choice():
	global count
	global show_choices
	global all_choices


	count += 1

	show_choices.grid_forget()

	show_choices["text"] = all_choices[:count]
	show_choices.grid(row=0, column=0, ipadx=30)

	show_choices.after(100, display_choice)

def choice(choice_name):
	global computer_choice
	global count
	global all_choices
	global show_choices
	global scissors
	global rock
	global paper

	rock.grid_forget()
	scissors.grid_forget()
	paper.grid_forget()

	paper = Label(root, text="Paper", fg="#fff", bg="#ff36da", padx=32, pady=17, font=("Impact", 25))
	paper.grid(row=0, column=1)
    
	rock = Label(root, text="Rock", fg="#fff", bg="#0099ff", padx=32, pady=17, font=("Impact", 25))
	rock.grid(row=0, column=0)

	scissors = Label(root, text="Scissors", fg="#fff", bg="orange", padx=32, pady=17, font=("Impact", 25))
	scissors.grid(row=0, column=2)

	choices = ["Rock", "Paper", "Scissors"]
	computer_choice = random.choice(choices)
	full_choice = "My choice: " + computer_choice
	player_choice = "Your choice: " + choice_name
	all_choices = player_choice + "\n" + full_choice

	choice_name = choice_name.lower()
	computer_choice = computer_choice.lower()

	victory = "Haha! I win, you lose!"

	tie = "A tie. I'll easily win next time though."
	
	loss = "You just won from luck..."

	if choice_name == "rock":
		if computer_choice == "rock":
			all_choices += "\n" + tie

		if computer_choice == "paper":
			all_choices += "\n" + victory

		if computer_choice == "scissors":
			all_choices += "\n" + loss

	if choice_name == "paper":
		if computer_choice == "rock":
			all_choices += "\n" + loss

		if computer_choice == "paper":
			all_choices += "\n" + tie

		if computer_choice == "scissors":
			all_choices += "\n" + victory

	if choice_name == "scissors":
		if computer_choice == "rock":
			all_choices += "\n" + victory

		if computer_choice == "paper":
			all_choices += "\n" + loss

		if computer_choice == "scissors":
			all_choices += "\n" + tie

	show_choices = Label(frame_choice, text="", bg="#00ff08", fg="#fff", font=("Calibri", 18), width=29, padx=9)
	show_choices.grid(row=0, column=0, ipadx=23)

	display_choice()

# Rock button to press
rock = Button(root, text="Rock", fg="#fff", bg="#0099ff", bd=0, activeforeground="#0099ff", activebackground="#fff",
              highlightthickness="1", font=("Impact", 25), padx=25, pady=10, command=lambda: choice("Rock"))
rock.config(highlightcolor="#0099ff", highlightbackground="#0099ff")
rock.grid(row=0, column=0)

# Paper button to press
paper = Button(root, text="Paper", fg="#fff", bg="#ff36da", bd=0, activeforeground="#ff36da", activebackground="#fff", highlightthickness="1", font=("Impact", 25), padx=25, pady=10, command=lambda: choice("Paper"))
paper.config(highlightcolor="#ff36da", highlightbackground="#ff36da")
paper.grid(row=0, column=1)

# Scissor button to press
scissors = Button(root, text="Scissors", fg="#fff", bg="orange", bd=0, activeforeground="orange", activebackground="#fff", highlightthickness="1", font=("Impact", 25), padx=25, pady=10, command=lambda: choice("Scissors"))
scissors.config(highlightcolor="orange", highlightbackground="orange")
scissors.grid(row=0, column=2)

mainloop()