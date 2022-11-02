import tkinter as tk
from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32gui
import win32con
win = tk.Tk()
win.title("Tinted")
win.geometry("1900x1000")
win.attributes('-alpha',1)
win.configure(bg='black')

sec = StringVar()
Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=1720, y=900)
sec.set('00')
mins= StringVar()
Entry(win, textvariable = mins, width =2, font = 'Helvetica 14').place(x=1680, y=900)
mins.set('00')
hrs= StringVar()
Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=1640, y=900)
hrs.set('00')

def pink():
    messagebox.showinfo("", "Remember to look away from your screen every 20 min to protect your eyes.")
    # hide the button
    for i in range(1,100):

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
          times -= 1


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
win.title("Applepie")
win.attributes('-transparentcolor', 'white', '-topmost', 1)
win.config(bg='white') 
win.attributes("-alpha", 0.25)
win.wm_attributes("-topmost", 1)
bg = Canvas(win, width=width, height=height, bg='white')

setClickthrough(bg.winfo_id())

frame = ImageTk.PhotoImage(file="Pink.png")
bg.create_image(1920/2, 1080/2, image=frame)
bg.pack()

b1 = tk.Button(win, text='START', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10),  command = pink).place(x=2667, y=925)
win.bind('<Return>', lambda event:pink())
win.mainloop()
