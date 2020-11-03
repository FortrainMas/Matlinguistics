from tkinter import *
from tkinter import messagebox 

#Button commands(but why them can be visible only there)
def setOperationPlus():
    global currentOperation
    currentOperation = '+'

def setOperationMinus():
    global currentOperation
    currentOperation = '-'
    
def setOperationDevide():
    global currentOperation
    currentOperation = '/'

def setOperationMultiply():
    global currentOperation
    currentOperation = '*'
def equal():
    #Get data
    global value1
    global value2
    try:
        val1 = int(value1.get())
        val2 = int(value2.get())
    except:
        messagebox.showinfo("Калькулятор", "Не правильные данные") 
        return
    result = 0
    #Do stuff
    if(currentOperation == ''):
        pass
    elif(currentOperation == '+'):
        result = val1 + val2
    elif(currentOperation == '-'):
        result = val1 - val2
    elif(currentOperation == '/'):
        result = val1 / val2
    elif(currentOperation == '*'):
        result = val1 * val2
    #Show result
    global label
    textResult = 'Результат: ' + str(result)
    label.config(text = textResult)



#Window initializer
root = Tk()
root.title("Калькулятор")
root.geometry("225x450")

#Important variables
currentOperation = ''
value1 = StringVar()
value2 = StringVar()
labelText = 'Здесь будет ответ'

#Init textBoxes
value1_entry = Entry(textvariable=value1, width = 20)
value1_entry.place(relx=.1, rely=.1)
value2_entry = Entry(textvariable=value2, width = 20)
value2_entry.place(relx=.1, rely=.2)

#Init label
label = Label(text=labelText, justify=LEFT)
label.place(relx=.1, rely=.3)

#Init buttons
plusButton = Button(text="+",           
             background="#555",     
             foreground="#ccc",     
             padx="20",             
             pady="8",              
             font="16",
             width="2",
             command=setOperationPlus            
             )
plusButton.place(relx=.1, rely=.45)
minusButton = Button(text="-",           
             background="#555",     
             foreground="#ccc",     
             padx="20",             
             pady="8",              
             font="16",
             width="2",
             command=setOperationMinus              
             )
minusButton.place(relx=.50, rely=.45)
multiplyButton = Button(text="*",           
             background="#555",     
             foreground="#ccc",     
             padx="20",             
             pady="8",              
             font="16",
             width="2",
             command=setOperationMultiply
             )
multiplyButton.place(relx=.50, rely=.60)
devideButton = Button(text="/",           
             background="#555",     
             foreground="#ccc",     
             padx="20",             
             pady="8",              
             font="16",
             width="2",
             command=setOperationDevide              
             )
devideButton.place(relx=.10, rely=.60)
equalButton = Button(text="=",           
             background="#555",     
             foreground="#ccc",     
             padx="20",             
             pady="8",              
             font="16",
             width="10",
             command=equal            
             )
equalButton.place(relx=.10, rely=.80)

root.mainloop()




