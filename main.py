import random
import tkinter as tk
from tkinter import messagebox

def shake_8ball():
    responses = [
        ("It is certain", 0.05),
        ("It is decidedly so", 0.05),
        ("Without a doubt", 0.05),
        ("Yes, definitely", 0.05),
        ("You may rely on it", 0.05),
        ("As I see it, yes", 0.1),
        ("Most likely", 0.1),
        ("Outlook good", 0.1),
        ("Yes", 0.1),
        ("Signs point to yes", 0.1),
        ("Reply hazy, try again", 0.05),
        ("Ask again later", 0.05),
        ("Better not tell you now", 0.05),
        ("Cannot predict now", 0.05),
        ("Concentrate and ask again", 0.05),
        ("Don't count on it", 0.05),
        ("My reply is no", 0.05),
        ("My sources say no", 0.05),
        ("Outlook not so good", 0.05),
        ("Very doubtful", 0.05)
    ]
    
    responses_list, probabilities = zip(*responses)
    return random.choices(responses_list, probabilities, k=1)[0]

def on_shake():
    answer = shake_8ball()
    messagebox.showinfo("Magic 8 Ball", answer)

# Main window
root = tk.Tk()
root.title("Magic 8 Ball")

# label
label = tk.Label(root, text="Ask the Magic 8 Ball a question:")
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Shake Ball", command=on_shake)
button.pack(pady=20)

# Main loop
root.mainloop()
