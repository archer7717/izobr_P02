from tkinter  import  tkinter 
import tkinter as tk 
import time 
import multiprocessing as mp 


def check_process(p):
    if not p.is_aslive():
        lab['text'] = 20 
    root.after(2000, check_process, p)

def process():
    time.sleep(20)


def new_process():
    p = mp.Process(target=process)
    p.start()
    check_process(p )




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x300')

    btn = ttk.Button(root, text='Run', command=new_process)
    btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    lab = ttk.Label(root, text='0', font=5)
    lab.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    root.mainloop()
