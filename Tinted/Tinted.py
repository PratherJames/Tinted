import tkinter as tk
from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32gui
import win32con
import random

win = tk.Tk()
win.title("Pink-Out")
win.geometry("640x480")
win.attributes('-alpha',1)
win.configure(bg='black')

sec = StringVar()
Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=20, y=90)
sec.set('00')
mins= StringVar()
Entry(win, textvariable = mins, width =2, font = 'Helvetica 14').place(x=50, y=90)
mins.set('00')
hrs= StringVar()
Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=80, y=90)
hrs.set('00')
one = "Reduce exposure to digital screens, prolonged usage can increase risk of photosensitive effects."
two = "The recommended viewing distance for a computer screen is at least 2 feet, and 8 feet from the T.V."
three = "If suddenly exposed to a trigger, covering one eye is proven to reduce the photosensitive effect"
four = "Common triggers are flashing lights, contrasting visual patterns (such as stripes or checks), and overexposure to electronics."
def pink():
    messagebox.showinfo("", "Remember to look away from your screen every 20 min to protect your eyes.")
    # hide the button
    for i in range(1, 1999):
        times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
        while times > -1:
          minute,second = (times // 60 , times % 60)
          hour =0
          if minute > 60:
             hour , minute = (minute // 60 , minute % 60)
          sec.set(second)
          mins.set(minute)
          hrs.set(hour)
          #Update the time
          win.update()
          time.sleep(1)
          if(times == 0):
             sec.set('00')
             mins.set('20')
             hrs.set('00')
             messagebox.showinfo("", "Take a break")
             messagebox.showinfo("", random.choice([one, two, three, four]))
          times -= 1

b1 = tk.Button(win, text='START', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10),  command = pink).place(x=26, y=25)
def setClickthrough(hwnd):
    print("setting window properties")
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

width = 1920
height = 1080

win.geometry('%dx%d' % (width, height))
win.title("Tinted")
win.attributes('-transparentcolor', 'white', '-topmost', 1)
win.config(bg='white') 
win.attributes("-alpha", 0.25)
win.wm_attributes("-topmost", 1)
bg = Canvas(win, width=width, height=height, bg='white')

setClickthrough(bg.winfo_id())

frame = ImageTk.PhotoImage(file="Green.png")
bg.create_image(1920/2, 1080/2, image=frame)
bg.pack()

b1 = tk.Button(win, text='START', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10),  command = pink).place(x=2667, y=925)
win.bind('<Return>', lambda event:pink())
win.mainloop()

