"""
Пример проблемы ожидания выполнения задачи
"""

from tkinter import ttk
import tkinter as tk
import time

root = tk.Tk()
root.geometry('300x300')


def main():
    btn = ttk.Button(root, text='Run', command=sleep_func)
    btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


def sleep_func():
    time.sleep(10)
    lab['text'] = 'после сна'


if __name__ == '__main__':
    main()
    lab = ttk.Label(root, text='до нажатия кнопки')
    lab.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    root.mainloop()
