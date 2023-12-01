from  tkinter import *
import  random
from tkinter import messagebox
import threading
import pygame
import json
import tkinter as tk
from PIL import ImageTk,Image


root = tk.Tk()
root.title("Quiz Game")
root.geometry('600x550')
root.configure(background='black')
root.resizable(False,False)


title = Label(root, text='QUIZ GAME USING PYTHON', font=("Comic Sans MS", 16, "bold"),background='#000',foreground='white')
title.place(x=150,y=30)

content1 = Label(root, text='Guess A Number', font=("Comic Sans MS", 16, "bold"),background='#000',foreground='white')
content1.place(x=213,y=80)
content1 = Label(root, text='Between 1 to 100!', font=("Comic Sans MS", 16, "bold"),background='#000',foreground='white')
content1.place(x=205,y=110)

image_path = 'Guess-a-number-removebg-preview.png'
photo_image = tk.PhotoImage(file=image_path)
small_image = photo_image.subsample(2, 2)
image_label = tk.Label(root, image=small_image, background='#000')
image_label.place(x=170, y=160)

answer = random.randint(1, 100)
print(answer)
count = 10
pygame.mixer.init()
def checkTheAnswer():
    user_input = ans_place.get()
    global count
    def play_sound(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    if count == 0:
        showAnswer.config(text=f'Out Of Chances !!!')
    else:
        if int(user_input) > answer:
            count -= 1
            showAnswer.config(text=f'It\'s Too High, you have {count} chances!!!')
            showAnswer.config(fg="Red")
            play_sound('negative_beeps-6008.mp3')

        elif int(user_input) < answer:
            count -= 1
            showAnswer.config(text=f'It\'s Too Low, you have {count} chances!!!')
            play_sound('negative_beeps-6008.mp3')
            showAnswer.config(fg="Red")

        elif len(user_input) > 2:
            messagebox.showerror('Enter Valid Input')
        else:
            showAnswer.config(text='Congratulations! You Guessed It!')
            showAnswer.config(fg="Green")
            play_sound('correct-6033.mp3')


def validate_input(char, current_value):
    return char.isdigit() and len(current_value) <= 2
validate_cmd = root.register(validate_input)


def clear_placeholder(event):
    if ans_var.get() == "Enter a value":
        ans_var.set("")
        ans_place.config(fg='black')

def restore_placeholder(event):
    if not ans_var.get():
        ans_var.set("Enter a value")
        ans_place.config(fg='grey')

validate_cmd = root.register(validate_input)

# Create StringVar for Entry
ans_var = tk.StringVar()

# Create Entry widget with placeholder
ans_place = tk.Entry(root,textvariable=ans_var,font=('verdana', 18, 'bold'),validate="key",validatecommand=(validate_cmd, "%S", "%P"),justify="center",width=13)
ans_var.set("Enter a value")
ans_place.config(fg='grey')
ans_place.bind("<FocusIn>", clear_placeholder)
ans_place.bind("<FocusOut>", restore_placeholder)
ans_place.place(x=183, y=330)


check = Button(root, text='Verify', command=checkTheAnswer, width=10, height=2, background='blue',fg='white')
check.place(x=210, y=380)

def refreshAnswer():
    global answer, count
    answer = random.randint(1, 100)
    count = 10
    showAnswer.config(text='')
    ans_var.set("")
    ans_place.config(fg='grey')
    print(answer)

refresh = Button(root, text='Refresh', command=refreshAnswer, width=10, height=2, background='yellow')
refresh.place(x=300, y=380)

showAnswer = Label(root, text='', background='#000', font=('verdana',18,'bold'),foreground='green')
showAnswer.place(relx=0.5, rely=0.9, anchor="s")

root.mainloop()