import random

import tkinter as tk
from tkinter import *
import tkinter.messagebox as mbox


class PasswordGenerator:  
    """
        This class is used to generate a strong password for user.
    """  
    special_characters_list = [chr(i) for i in range(33,48)] + [chr(i) for i in range(58,65)] + [chr(i) for i in range(91,97)] + [chr(i) for i in range(123,127)] #contains all special charaters
    all_cap_alphabets = [chr(i) for i in range(65,91)] # contains all capital alphbets
    all_small_alphabets = [chr(i) for i in range(97,123)] # contains all small alphabets
    all_nums = [str(i) for i in range(0,10)] # contains all nums 0 to 9

    set_of_characters = special_characters_list + all_cap_alphabets + all_small_alphabets + all_nums # contains all list in one.


    def __init__(self):
        pass
    
    def generatePassword(self,length=8):
        """
        The generatePassword() method by default has 8 characters long password.

        Length less than 4 is not acceptable, by the way this is not a good practice to have password 4 characters long password.

        PASSWORD MUST BE ATLEAST 8 CHARACTERS LONG.
        """
        if (length < 8):
            mbox.showwarning("Warning","A Strong password must be minimum of 8 characters long.")
            return ""
            

        else:
            password = []
            password.append(random.choice(self.special_characters_list)) # appending random special character from the given list
            password.append(random.choice(self.all_cap_alphabets)) # appending random capital alphabet from the given list
            password.append(random.choice(self.all_small_alphabets)) # appending random small alphabets from the given list.
            password.append(random.choice(self.all_nums)) # appending random numbers from 0 to 9 from the given list.

            length -= 4 # out of specified length, 4 places are already covered above.

            # Now, running loop for remaining length.
            for i in range(length):
                password.append(random.choice(self.set_of_characters)) # appending characters from the set of all characters.
            
        random.shuffle(password) # shuffling the list.
        
    
        password = "".join(str(i) for i in password) # converting list to string.
        return password



        

    

class MainApp:
    

    def __init__(self):
        def reset(event):
            username.delete("1.0","end")
            passLength.delete("1.0","end")
            generatedPass.delete("1.0","end")
        
        def accept(event):
            if len(generatedPass.get("1.0","end"))==1:
                mbox.showerror("Error", "Nothing to copy on clipboard!")
            else:
                # print(generatedPass.get("1.0","end"),len(generatedPass.get("1.0","end")),end="\n")
                root.clipboard_clear()
                root.clipboard_append(generatedPass.get("1.0","end-1c"))
                # root.update()
                mbox.showinfo("Information","Password is copied to clipboard!")


        root = Tk()

        # root window title and dimension
        root.title("Random Password Generator")
        # Set geometry (widthxheight)
        root.geometry('500x400')
        root.resizable(width=False, height=False)

        # root = Frame()
        # self.main_frame = Frame()

        # root.columnconfigure(0,weight=1)
        # root.rowconfigure(0,weight=1)
        # root.rowconfigure(2,weight=1)
        # root.rowconfigure(3,weight=1)


        

        # heading=ttk.Label(root, text="Hello World!")
        # heading.grid(column=0, row=0)

        titleLable = Label(root, text="Password Generator", anchor="center", fg="#003153", font='Helvetica 18 bold underline')

        usernameLabel = Label(root, text="Enter user name: ", anchor="w")
        username=Text(root,bg="#ffffff",height=1, width=20)

        passLengthLabel = Label(root, text="Enter password length: ", anchor="w")

        # global passLength
        passLength=Text(root, height=1, width=20)

        generatedPassLabel = Label(root, text="Generated   password: ", anchor="w")
        generatedPass = Text(root, height=1, width=20, fg="#07a607")

        generatePassbtn = Button(root, text="GENERATE PASSWORD", bg="#0b0bba", fg="#ffffff", command=lambda: self.passwordGeneration(passLength.get("1.0","end-1c"), generatedPass, username))

        canvas_accept = Canvas(root, width=100, height=40, highlightthickness=0)
        accept_rectangle = canvas_accept.create_rectangle(20, 10, 80, 30, outline="black", fill="white")
        accept_text = canvas_accept.create_text(50, 20, text="ACCEPT")
        canvas_accept.tag_bind(accept_rectangle,"button-accept")
        canvas_accept.tag_bind(accept_text,"text-accept")
        canvas_accept.bind("<Button-1>",accept)



        # accept = Button(root, text="ACCEPT", fg="#0b0bba", bg="#ffffff")
        # reset = Button(root, text="RESET", fg="#0b0bba",  bg="#ffffff")

        canvas_reset = Canvas(root, width=100, height=40, highlightthickness=0)
        reset_rectangle = canvas_reset.create_rectangle(20, 10, 80, 30, outline="black", fill="white")
        reset_text = canvas_reset.create_text(50, 20, text="RESET")
        canvas_reset.tag_bind(reset_rectangle,"button-reset")
        canvas_reset.tag_bind(reset_text,"text-reset")
        canvas_reset.bind("<Button-1>", reset)

            


        
        
        
        titleLable.grid(column=1, row=0)

        usernameLabel.grid(column=0, row=1)
        username.grid(column=1, row=1)

        passLengthLabel.grid(column=0, row=2)
        passLength.grid(column=1, row=2 )

        generatedPassLabel.grid(column=0, row=3)
        generatedPass.grid(column=1, row=3 )

        generatePassbtn.grid(column=1, row=4)
        # accept.grid(column=1, row=5)
        # reset.grid(column=1, row=6)
        canvas_accept.grid(column=1, row=5)
        canvas_reset.grid(column=1, row=6)

        # root.place(in_=self.main_frame, anchor="c", relx=.50, rely=.50)


        

        # all widgets will be here
        # Execute Tkinter
        root.mainloop()

    

        
    def passwordGeneration(self, length, geneartedPassField, usernameField):
        
            if len(usernameField.get("1.0","end-1c"))!=0:
                try: 
                    length = int(length)

                    password = PasswordGenerator()
                    geneartedPassField.delete("1.0","end")
                    geneartedPassField.insert("1.0",password.generatePassword(length))

                except Exception as e:
                    if length < 4:
                        mbox.showwarning("Warning",length)
                    else:
                        mbox.showwarning("Warning", "Enter password length as positive number!" )

            else:
                mbox.showwarning("Warning", "Please enter username!")


        

    def acceptPassword(self):
        pass

    def resetPassword(self, event, username, passlength, generatedPass):
        """How to work with event on Canvas"""
        username.delete("1.0","end")
        passlength.delete("1.0","end")
        generatedPass.delete("1.0","end")
        pass

if __name__ == "__main__":
    app = MainApp()
    
    
