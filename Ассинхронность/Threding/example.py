from tkinter  import  tkinter 
import tkinter as tk 
import tkinter as ttk 
import time 
from threading  import Thread


def thread_sleep(p):
    if not p.is_aslive():
        lab['text'] = int(lab['text']) + 10

def new_thread():
    t1 = Thread(target=thread_sleep)
    t1.start




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x300')

    btn = ttk.Button(root, text='Run', command=new_thread)
    btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    lab = ttk.Label(root, text='0', font=5)
    lab.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    root.mainloop()

