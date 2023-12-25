import tkinter as tk
from tkinter import messagebox
import datetime
import time

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up!")
            break
        time.sleep(1)

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("500x400")

label = tk.Label(root,foreground="white" ,text="Enter alarm time (HH:MM):")
label.pack(anchor="center")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()
