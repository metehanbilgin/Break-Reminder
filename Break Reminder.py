import tkinter as tk
from tkinter import messagebox, font
import time
from plyer import notification
import threading

def notify_user():
    notification.notify(
        title="Break Time!", 
        message="1 hour has passed. Please take a break!"
    )

def start_timer():
    while True:  
        time.sleep(3600) 
        notify_user()  
        messagebox.showinfo("Break Time", "1 hour has passed. Please take a break!")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def create_gui():
    root = tk.Tk()
    root.title("Break Reminder")  
    root.geometry("400x200")
    root.configure(bg="#2E3440")  
   
    root.iconbitmap("")
    
    
    center_window(root, 400, 200)

    custom_font = font.Font(family="Helvetica", size=16, weight="bold")
    

    label = tk.Label(
        root,
        text="Break Reminder is Active!",
        font=custom_font,
        fg="#FFFFFF",
        bg="#2E3440"  
        
    )
    label.pack(expand=True)  

    timer_thread = threading.Thread(target=start_timer)
    timer_thread.daemon = True  
    timer_thread.start()

    root.mainloop()

if __name__ == "__main__":
    create_gui()