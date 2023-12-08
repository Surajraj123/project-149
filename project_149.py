from tkinter import *
import random

root = Tk()
root.title("GENERATE RANDOM ALPHABETS")
root.geometry("400x400")
generated_word_number = Label(root)

def random_alphabet():
    list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_no5 = random.randint(1, 26)
    random_alpha1 = list1[random_no1]
    random_alpha2 = list1[random_no2]
    random_alpha3 = list1[random_no3]
    random_alpha4 = list1[random_no4]
    random_alpha5 = list1[random_no5]
    generated_word_number["text"] = "Random Word are:- " + str(random_alpha1) + str(random_alpha2) + str(random_alpha3) + str(random_alpha4) + str(random_alpha5)
    
btn1 = Button(root, text = "Generate Random Alphabets", command = random_alphabet, bg = "blue", fg = "white")
btn1.place(relx= 0.5, rely=0.5, anchor=CENTER)
generated_word_number.place(relx= 0.5, rely= 0.6, anchor=CENTER)

root.mainloop()

