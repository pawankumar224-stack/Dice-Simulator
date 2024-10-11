import tkinter as tk
from PIL import Image,ImageTk
import random

container = tk.Tk()
container.geometry("550x400")
container.title("Dice Roller")

dice = ["dice_1.png","dice_2.png","dice_3.png","dice_4.png","dice_5.png","dice_6.png"]
img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
img2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

lab1 = tk.Label(container,image=img1)
lab2 = tk.Label(container,image=img2)

lab1.image = img1
lab2.image = img2

lab1.place(x = 20, y = 30)
lab2.place(x = 300, y = 30)

def dice_roll():
    img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lab1.configure(image = img1)
    lab1.image = img1

    img2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lab2.configure(image = img2)
    lab2.image = img2

butt = tk.Button(container, text = "ROLL", bg = "gold", fg = "black",font = "Times 20 bold" , command = dice_roll)
butt.place(x = 230, y = 300)      

container.mainloop()