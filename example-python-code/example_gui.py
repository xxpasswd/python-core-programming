from tkinter import *

class AlarmGui:
    def __init__(self):
        self.top = Tk()
        self.top.geometry('200x150')
        self.lable = Label(self.top, text=title)
        self.lable.pack()
        self.lable2 = Label(self.top)
        self.lable2.pack()
        # self.diren = Entry(self.top)
        # self.diren.pack()
        self.button = Button(self.top, text='execute', command=self.set_string)
        self.button.pack()

    def set_string(self):
        # text = self.diren.get()
        self.lable2.config(text='保存成功')

if __name__ == '__main__':
    AlarmGui()
    mainloop()