from tkinter import *

myGUI = Tk()
myGUI.geometry('175x200')
myGUI.title('Calculator')

def oneClick(event) :
    length = len(entry.get())
    entry.insert(length, '1')

def twoClick(event) :
    length = len(entry.get())
    entry.insert(length, '2')

def threeClick(event) :
    length = len(entry.get())
    entry.insert(length, '3')

def fourClick(event) :
    length = len(entry.get())
    entry.insert(length, '4')

def fiveClick(event) :
    length = len(entry.get())
    entry.insert(length, '5')
    
def sixClick(event) :
    length = len(entry.get())
    entry.insert(length, '6')

def sevenClick(event) :
    length = len(entry.get())
    entry.insert(length, '7')

def eightClick(event) :
    length = len(entry.get())
    entry.insert(length, '8')

def nineClick(event) :
    length = len(entry.get())
    entry.insert(length, '9')

def zeroClick(event) :
    length = len(entry.get())
    entry.insert(length, '0')

def plusClick(event) :
    length = len(entry.get())
    entry.insert(length, '+')

def minusClick(event) :
    length = len(entry.get())
    entry.insert(length, '-')

def multiplyClick(event) :
    length = len(entry.get())
    entry.insert(length, '*')

def divideClick(event) :
    length = len(entry.get())
    entry.insert(length, '/')

def clearClick(event) :
    entry.delete(0, END)

def equals(event) :
    thing = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(eval(thing)))

frameOne = Frame(myGUI)
frameOne.pack(side=TOP)
frameTwo = Frame(myGUI)
frameTwo.pack(side=TOP)
frameThree = Frame(myGUI)
frameThree.pack(side=TOP)
frameFour = Frame(myGUI)
frameFour.pack(side=TOP)
frameFive = Frame(myGUI)
frameFive.pack(side=TOP)
frameSix = Frame(myGUI)
frameSix.pack(side=TOP)
frameSeven = Frame(myGUI)
frameSeven.pack(side=TOP)

buttonOne = Button(frameTwo, text='1', padx=20)
buttonOne.pack(side=LEFT)
buttonOne.bind('<Button-1>', oneClick)
buttonTwo = Button(frameTwo, text='2', padx=20)
buttonTwo.pack(side=LEFT)
buttonTwo.bind('<Button-1>', twoClick)
buttonThree = Button(frameTwo, text='3', padx=20)
buttonThree.pack(side=LEFT)
buttonThree.bind('<Button-1>', threeClick)
buttonFour = Button(frameThree, text='4', padx=20)
buttonFour.pack(side=LEFT)
buttonFour.bind('<Button-1>', fourClick)
buttonFive = Button(frameThree, text='5', padx=20)
buttonFive.pack(side=LEFT)
buttonFive.bind('<Button-1>', fiveClick)
buttonSix = Button(frameThree, text='6', padx=20)
buttonSix.pack(side=LEFT)
buttonSix.bind('<Button-1>', sixClick)
buttonSeven = Button(frameFour, text='7', padx=20)
buttonSeven.pack(side=LEFT)
buttonSeven.bind('<Button-1>', sevenClick)
buttonEight = Button(frameFour, text='8', padx=20)
buttonEight.pack(side=LEFT)
buttonEight.bind('<Button-1>', eightClick)
buttonNine = Button(frameFour, text='9', padx=20)
buttonNine.pack(side=LEFT)
buttonNine.bind('<Button-1>', nineClick)
buttonPlus = Button(frameFive, text='+', padx=20)
buttonPlus.pack(side=LEFT)
buttonPlus.bind('<Button-1>', plusClick)
buttonZero = Button(frameFive, text='0', padx=20)
buttonZero.pack(side=LEFT)
buttonZero.bind('<Button-1>', zeroClick)
buttonMinus = Button(frameFive, text='-', padx=20)
buttonMinus.pack(side=LEFT)
buttonMinus.bind('<Button-1>', minusClick)
buttonMultiply = Button(frameSix, text='*', padx=20)
buttonMultiply.pack(side=LEFT)
buttonMultiply.bind('<Button-1>', multiplyClick)
buttonEquals = Button(frameSix, text='=', padx=20)
buttonEquals.pack(side=LEFT)
buttonEquals.bind('<Button-1>', equals)
buttonDivide = Button(frameSix, text='/', padx=20)
buttonDivide.pack(side=LEFT)
buttonDivide.bind('<Button-1>', divideClick)
buttonClear = Button(frameSeven, text="Clear", padx = 50)
buttonClear.pack(side=LEFT)
buttonClear.bind('<Button-1>', clearClick)

entry = Entry(frameOne, justify=RIGHT)
entry.bind('<Return>', equals)
entry.pack()
