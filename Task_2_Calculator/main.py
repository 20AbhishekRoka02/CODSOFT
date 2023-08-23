"""Code to make a GUI Calculator"""
from tkinter import *
from math import sqrt
import tkinter.messagebox as mbox

result = "" #string to store results
contenttocalculate = [] #list that will content numbers that are being operated.

displaytext = "" #text that will be displayed on screen.
displayHandlingKeys = ["C", "\u2190", "=", "."] #Keys that handle calculator and numbers
numbers = [str(i) for i in range(10)] #list of all number 0-9
operators = ["+","-","*","/"] #Basic operatiors
unaryOperators = ["!",chr(8730)] #Unary opeartors such as Factorial and Square root.

class CalculatorOperation():

    """This class contains methods for Calculator operations like display handling and mathematical operations """
    def __init__(self):        
        pass

    def btnClickEvent(self, selectedCharacter):
        """Method controls events to be executed."""
        # getting global variables
        global displayHandlingKeys, numbers, unaryOperators, operators, contenttocalculate, displaytext, result
            
        if selectedCharacter not in displayHandlingKeys:
            if selectedCharacter in numbers:
                if len(result) != 0:
                    if result[-1] in operators:
                        # for instance, if result contains "23+", so contenttocalculate list must get clear to store numbers
                        contenttocalculate.clear()

                result += str(selectedCharacter) # for instance, here, result will be "23+6", if selectedCharacter is 6 and result was "23+", otherwise it will be "236".
                contenttocalculate.append(selectedCharacter) # and, contenttocalculate will append the number.

            elif selectedCharacter in unaryOperators:
                if selectedCharacter == unaryOperators[0]: 
                    # case of factorial
                    result = self.factorial(int(eval("".join(contenttocalculate)))) # for instance, structure is: result = self.factorial(int(eval("".join(['2','3','+','6']))), if contenttocalculate is ['2','3','+','6']
                    contenttocalculate.clear() # truncating the list
                    contenttocalculate.append(result) # appending result to the list.
                else: 
                    # case of square root
                    result = self.squareRoot(eval("".join(contenttocalculate))) # for instance, structure is: result = self.squareRoot(eval("".join(['2','3','+','6'])), if contenttocalculate is ['2','3','+','6']
                    contenttocalculate.clear() # truncating the list
                    contenttocalculate.append(result) # appending result to the list.
                
            elif selectedCharacter in operators:
                
                try:
                    result = str(eval(result)) # see, eval() can't evaluate if result is "23+". eval() is used because, if result is "23+6", then on selection of any operator, result will be "29", and can add more operators. It is also to avoid case like "23++" or "23+/"
                    contenttocalculate.clear() # if everything went good, truncating the list
                    contenttocalculate.append(result) # appending the value.
                except Exception as e:
                    pass
                result += selectedCharacter # concatinating the operator to result string.

                
        else:
            if selectedCharacter=="C":
                self.clear()     
            
            elif selectedCharacter=="\u2190":
                self.backspace() 
                
            elif selectedCharacter == "=":
                self.equalTo()
            
            elif selectedCharacter == ".":
                self.decimal()
                
            
            
        displaytext.set("".join(contenttocalculate)) # Setting text to be displayed on screen.
        

    
    def factorial(self, num):    
        """iterative algorithm for factorial. 
        Here, factorial for 0 is assumed to be 1.
        and, factorial get calculated for Integers only.
        No number less than 0 accepted."""
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
        """Square root of number by using sqrt() method of math"""
        return str(sqrt(num))
    
    def clear(self):
        """Resetting the result and contenttocalculate variables."""
        global result, contenttocalculate
        result=""
        contenttocalculate.clear()     
        
    def backspace(self):
        """ remvoing Last element (being number) from result and contenttocalcualte variables."""
        global result, operators, contenttocalculate
        if result[-1] not in operators:
            result = result[:-1]
            contenttocalculate.pop()

    def equalTo(self):
        """Return result of equal to operation."""
        global result, contenttocalculate
        try:
            result = eval(result)
            contenttocalculate.clear()
            contenttocalculate.append(str(result))
        except Exception as e:
            pass

    def decimal(self):
        """Method to handle, when user selects '.' (dcimal) in calculator."""
        global result, contenttocalculate

        if result[-1] in operators:
            # if result is "23+", then on this case, on clicking '.', result will be "23+0."
            result += "0."
            contenttocalculate.clear()
            contenttocalculate.append("0.")
        elif len(result)==0:
            # if there is nothing in result andb contenttocalculate, simply add "0."
            result += "0."
            contenttocalculate.append("0.")
        else:
            # otherwise, there will be numbers, so, simply add '.' such as "23."
            result += "."
            contenttocalculate.append(".")
        

class Calculator():
    """Calculator GUI class to handle GUI working."""
    def __init__(self):                 
            
        root = Tk()

        # root window title and dimension
        root.title("Calculator GUI")
        # Set geometry (widthxheight)
        root.geometry('340x560')        
        root.configure(bg="#eee9e9")

        # getting global variable displaytext.
        global displaytext
        displaytext = StringVar() # creating object of class StringVar.
        display = Entry(root, width=300, textvariable=displaytext,font=("Segoe UI bold", 50),  cursor="arrow")        
        display.pack()

        # Buttons -> list of symbols that will be displayed on Calculator.
        symbolSet = ["C",chr(8730), "/","\u2190", 7,8,9, "*", 4,5,6,"-",1,2,3,"+","!",0,".","="]

        # Creating frame to add and display buttons 
        btnFrame = Frame(root)
        btnFrame.pack()

        # creating object of class CalculatorOperations
        calculate = CalculatorOperation()

        # nested function to add buttons on screen.
        def btnSet(symbol, index):
            # buttons to be dispalyed                        
            btn= Button(btnFrame,text=str(symbol), font=("Segoe UI", 23), padx=20, pady=10, command=lambda t=symbol: calculate.btnClickEvent(str(t)))
            btn.grid(row=index//4, column=index%4, sticky="nsew") # Giving position to buttons in frame.
            

        # adding buttons in frame
        for symbol in symbolSet:
            btnSet(symbol, symbolSet.index(symbol))
        
        root.mainloop()

    
    

        
        
    

if __name__=="__main__":
    app = Calculator()