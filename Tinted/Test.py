import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from PIL import ImageTk, Image
import win32gui, win32con

def setClickthrough(hwnd):
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

def setAttributes(hwnd, attributeList):
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    for attribute in attributeList:
        styles |= attribute
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)

root = tk.Tk()
root.geometry("400x200")

time_label = tk.Label(root, text="")
time_label.pack(pady=10)

instructions_label = tk.Label(root, text="Enter the desired countdown time in minutes:")
instructions_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

def button_click(event):
    global stopped
    stopped = False
    try:
        count = int(entry.get()) * 60
        if count <= 0:
            raise ValueError("Countdown time should be a positive integer.")
        countdown(count)
        entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

entry.bind("<Return>", button_click)

def stop_timer():
    global stopped
    stopped = True

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack(pady=10)

def countdown(count):
    mins, secs = divmod(count, 60)
    time_label.configure(text="{:02d}:{:02d}".format(mins, secs))
    if count > 0 and not stopped:
        root.after(1000, countdown, count-1)
    elif not stopped:
        message_box = messagebox.showinfo("Timer", "Time's up!")
        time_label.configure(text="")
        try:
            count = int(entry.get()) * 60
            if count <= 0:
                raise ValueError("Countdown time should be a positive integer.")
            root.after(20000, countdown, count)
            entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

stopped = False

# create the first window
win1 = tk.Toplevel(root)
win1.attributes('-transparentcolor', 'white', '-topmost', 1)
win1.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
setAttributes(win1.winfo_id(), [win32con.WS_EX_LAYERED, win32con.WS_EX_TRANSPARENT])

canvas1 = Canvas(win1, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas1.pack()

img1 = Image.open("Pink.png").convert("RGBA")
img1 = img1.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
alpha = Image.new("L", img1.size, 128)
img1.putalpha(alpha)
img1 = ImageTk.PhotoImage(img1)

canvas1.create_image(0, 0, image=img1, anchor="nw")

# create the second window
win2 = tk.Toplevel(root)
win2.attributes('-transparentcolor', 'white', '-topmost', 1)
win2.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
setAttributes(win2.winfo_id(), [win32con.WS_EX_LAYERED, win32con.WS_EX_TRANSPARENT])

canvas2 = Canvas(win2, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas2.pack()

img2 = Image.open("Green.png").convert("RGBA")
img2 = img2.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
alpha = Image.new("L", img2.size, 128)
img2.putalpha(alpha)
img2 = ImageTk.PhotoImage(img2)

canvas2.create_image(0, 0, image=img2, anchor="nw")

# create the third window
win3 = tk.Toplevel(root)
win3.attributes('-transparentcolor', 'white', '-topmost', 1)
win3.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
setAttributes(win3.winfo_id(), [win32con.WS_EX_LAYERED, win32con.WS_EX_TRANSPARENT])

canvas3 = Canvas(win3, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas3.pack()

img3 = Image.open("Blue.png").convert("RGBA")
img3 = img3.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
alpha = Image.new("L", img3.size, 128)
img3.putalpha(alpha)
img3 = ImageTk.PhotoImage(img3)

canvas3.create_image(0, 0, image=img3, anchor="nw")

root.mainloop()