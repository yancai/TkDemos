# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'yancai'

"""
Just a photo viewer
"""

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, Button, CENTER
from ttk import Frame, Style
import tkFileDialog


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        button_open = Button(self, text="open", command=self.onOpen)
        button_open.pack()

    def onOpen(self):

        ftypes = [('Image files', '*.jpg'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            img = self.load_image(fl)
            label_img = Label(self,
                              image=img,
                              width=750,
                              height=550,
                              justify=CENTER,
                              # background="#33333333",
                              )
            label_img.image = img
            label_img.place(x=0, y=0)
            label_img.pack(fill=BOTH)

    def load_image(self, filename):
        img = Image.open(filename)
        img = img.resize((500, 400), Image.BICUBIC)
        pto = ImageTk.PhotoImage(img)

        return pto


def main():

    root = Tk()
    root.geometry("800x600")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()