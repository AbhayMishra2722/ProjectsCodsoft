import tkinter as tk
import random
import winsound

# --- Game data ---
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

# --- Determine winner ---
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        result = "It's a tie!"
        beep("tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        result = "You win!"
        beep("win")
    else:
        computer_score += 1
        result = "Computer wins!"
        beep("lose")
    return result

# --- Play simple beep sound ---
def beep(result_type):
    if result_type == "win":
        winsound.Beep(1000, 200)
    elif result_type == "lose":
        winsound.Beep(500, 200)
    elif result_type == "tie":
        winsound.Beep(800, 200)

# --- On choice ---
def on_choice(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_canvas.delete("all")
    comp_canvas.delete("all")
    draw_choice(user_canvas, user_choice, "blue")
    draw_choice(comp_canvas, computer_choice, "red")

    result_text.set(f"Your choice: {user_choice.capitalize()}\n"
                    f"Computer: {computer_choice.capitalize()}\n"
                    f"{result}")

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    play_again_button.pack(pady=10)  # Show the Play Again button

# --- Draw simple shape ---
def draw_choice(canvas, choice, color):
    canvas.create_rectangle(10, 10, 90, 90, fill=color)
    canvas.create_text(50, 50, text=choice.capitalize(), fill="white", font=("Arial", 10, "bold"))

# --- Play again logic ---
def play_again():
    result_text.set("Make your move!")
    user_canvas.delete("all")
    comp_canvas.delete("all")
    play_again_button.pack_forget()  # Hide the Play Again button until next round

# --- Reset scores ---
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    play_again()
    play_again_button.pack_forget()

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock-Paper-Scissors (No Images)")
root.geometry("500x600")
root.configure(bg="#222222")

user_score_label = tk.Label(root, text="Your Score: 0", font=("Helvetica", 14), fg="white", bg="#222222")
user_score_label.pack(pady=5)

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Helvetica", 14), fg="white", bg="#222222")
computer_score_label.pack(pady=5)

user_canvas = tk.Canvas(root, width=100, height=100, bg="#444444")
user_canvas.pack(pady=10)

comp_canvas = tk.Canvas(root, width=100, height=100, bg="#444444")
comp_canvas.pack(pady=10)

result_text = tk.StringVar()
result_text.set("Make your move!")
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 14), fg="yellow", bg="#222222")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#222222")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: on_choice("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: on_choice("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: on_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Scores", font=("Helvetica", 12), bg="red", fg="white", command=reset_scores)
reset_button.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 12), bg="green", fg="white", command=play_again)
play_again_button.pack_forget()  # Hide at start

root.mainloop()
