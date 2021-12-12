from tkinter import *
import os
from tkinter import messagebox
from tkinter import filedialog


window = Tk()
window.title('File Manager')
window.geometry('475x460')
window['background'] = '#F0F0F0'
window.resizable(False, False)


class ShowError(Exception):
    """class for handling errors and then displaying a warning window"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except Exception as e:
            messagebox.showerror(e, 'There is no such directory')


def choose_dir():
    """this function outputs directory to entry field"""
    directory = filedialog.askdirectory()
    txt.insert(0, directory)
    return directory


def get_directory():
    """this function returns the input text from the entry field"""
    entry_dir = txt.get()
    return entry_dir


@ShowError  # using a decorator
def show():
    """this function outputs files from the selected directory"""
    files = os.listdir(path=get_directory())
    if os.path.exists(get_directory()):
        for i in files:
            print(i, '\n')
            outputwin.insert(1.0, i + '\n')


def delete_info():
    """this function deletes previously entered information"""
    txt.delete(0, END)
    outputwin.delete(1.0, END)


lbl = Label(text='directory:', fg='black', bg='#F0F0F0', )
lbl.grid(column=0, row=0)

txt = Entry(width=30)
txt.grid(column=1, row=0)

outputwin = Text(height=30, width=40, fg='black', bg='white')
outputwin.grid(row=3, column=0, columnspan=3, sticky="nwes")

btn = Button(text='click to select', width=10, command=choose_dir, fg='green')
btn.grid(column=2, row=0)
btn2 = Button(text='show files', width=10, command=show, fg='green')
btn2.grid(column=2, row=1)
btn3 = Button(text='reset', command=delete_info, fg='red')
btn3.grid(column=0, row=1, columnspan=2, sticky='nwes')

window.mainloop()
