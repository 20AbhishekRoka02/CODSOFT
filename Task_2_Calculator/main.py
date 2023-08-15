"""Code to make a GUI Calculator"""
from tkinter import *
from math import sqrt
import tkinter.messagebox as mbox
result = ""
contenttocalculate = []
# userEventBuffer=""
displaytext = ""
displayHandlingKeys = ["C", "\u2190", "=", "."]
numbers = [str(i) for i in range(10)]
operators = ["+","-","*","/"]
unaryOperators = ["!",chr(8730)]
class CalculatorOperation():
    def __init__(self):        
        pass

    def btnClickEvent(self, selectedCharacter):
        global displayHandlingKeys, numbers, unaryOperators, operators, contenttocalculate, displaytext, result
            
        if selectedCharacter not in displayHandlingKeys:
            if selectedCharacter in numbers:
                if len(result) != 0:
                    if result[-1] in operators:
                        contenttocalculate.clear()

                result += str(selectedCharacter)
                contenttocalculate.append(selectedCharacter)            

            elif selectedCharacter in unaryOperators:
                if selectedCharacter == unaryOperators[0]: 
                    result = self.factorial(int(eval("".join(contenttocalculate))))
                    contenttocalculate.clear()
                    contenttocalculate.append(result)
                else: 
                    result = self.squareRoot(eval("".join(contenttocalculate)))
                    contenttocalculate.clear()
                    contenttocalculate.append(result)
                
            elif selectedCharacter in operators:
                
                try:
                    result = str(eval(result))
                    contenttocalculate.clear()
                    contenttocalculate.append(result)
                except Exception as e:
                    pass
                result += selectedCharacter

                pass
        else:
            if selectedCharacter=="C":
                self.clear()      
            
            elif selectedCharacter=="\u2190":
                self.backspace()
                
            elif selectedCharacter == "=":
                self.equalTo()
            
            elif selectedCharacter == ".":
                self.decimal()
                
                pass
            
        displaytext.set("".join(contenttocalculate))
        # displaytext.set(result)

    
    def factorial(self, num):    
        fact = 1
        if num < 0:
            mbox.showerror("Error", "Only +ve numbers accepted")
            fact = -1
        elif num in [0,1]:
            fact = 1
        else:
            fact=1
            for i in range(2,num+1): 
                fact *=i
        return str(fact)


        

    def squareRoot(self, num):
        return str(sqrt(num))
    
    def clear(self):
        global result, contenttocalculate
        result=""
        contenttocalculate.clear()     
        
    def backspace(self):
        global result, operators, contenttocalculate
        if result[-1] not in operators:
            result = result[:-1]
            contenttocalculate.pop()

    def equalTo(self):
        global result, contenttocalculate
        try:
            result = eval(result)
            contenttocalculate.clear()
            contenttocalculate.append(str(result))
        except Exception as e:
            pass

    def decimal(self):
        global result, contenttocalculate

        if result[-1] in operators:
            result += "0."
            contenttocalculate.clear()
            contenttocalculate.append("0.")
        elif len(result)==0:
            result += "0."
            contenttocalculate.append("0.")
        else:
            result += "."
            contenttocalculate.append(".")
        pass

class Calculator():
    def __init__(self):                 
            
        root = Tk()

        # root window title and dimension
        root.title("Calculator GUI")
        # Set geometry (widthxheight)
        root.geometry('340x560')
        # root.resizable(width=False, height=False)
        root.configure(bg="#eee9e9")

        # displaycontent = []
        global displaytext
        displaytext = StringVar()
        display = Entry(root, width=300, textvariable=displaytext,font=("Segoe UI bold", 50),  cursor="arrow")
        # display.grid(row=0, column=0)
        display.pack()

        # Buttons
        symbolSet = ["C",chr(8730), "/","\u2190", 7,8,9, "*", 4,5,6,"-",1,2,3,"+","!",0,".","="]

        btnFrame = Frame(root)
        btnFrame.pack()


        calculate = CalculatorOperation()


        def btnSet(symbol, index):                        
            btn= Button(btnFrame,text=str(symbol), font=("Segoe UI", 23), padx=20, pady=10, command=lambda t=symbol: calculate.btnClickEvent(str(t)))
            btn.grid(row=index//4, column=index%4, sticky="nsew")
            

        # map(btnSet, numbers)
        for symbol in symbolSet:
            btnSet(symbol, symbolSet.index(symbol))
        # for i in range(10):
        #     btn = Button(root, text=str(i))
        #     btn.grid(row=(i%4)+1, column=i%4)
        


        root.mainloop()

        pass
    

        
        
        pass

if __name__=="__main__":
    app = Calculator()