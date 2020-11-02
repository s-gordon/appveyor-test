#!/usr/bin/env python


from tkinter import Tk, Label, mainloop

def main():
    # initialize application
    # define a dummy widget
    parent_widget = Tk()
    label_widget = Label(parent_widget, text="Hello, world!")
    label_widget.pack()

    # start app event loop
    mainloop()


if __name__ == "__main__":
    main()
