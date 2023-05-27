import tkinter as tk
from tkinter import messagebox


def show_message():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askokcancel("Сообщение", "Введите капчу и нажмите ок!")
    if result:
        return True
    else:
        return 'driver.quit()'
