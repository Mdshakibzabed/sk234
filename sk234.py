from tkinter import *

# Creating a frame for the calculator
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# Creating a button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class CalculatorApp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        # Display widget
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES, fill=BOTH)

        # Buttons
        for num in ("789/", "456*", "123-", "0.+"):
            fLine = iCalc(self, TOP)
            for char in num:
                button(fLine, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

        # Equal button
        fLine = iCalc(self, TOP)
        button(fLine, LEFT, '=', lambda storeObj=display: storeObj.set(eval(storeObj.get())))

        # Clear button
        fLine = iCalc(self, BOTTOM)
        button(fLine, LEFT, 'C', lambda storeObj=display: storeObj.set(''))

if __name__ == '__main__':
    CalculatorApp().mainloop()
