from tkinter import *

class ToDoListApp():
    def __init__(self):
        root=Tk()
        root.title("To Do List")
        root.geometry("800x600")

        todoFrame = Frame(root)

        head_canvas = Canvas(todoFrame, width=800, height=200)
        head_rectangle = head_canvas.create_rectangle(0,0,800,100, fill="#19d319")
        head_text = head_canvas.create_text(100, 50, text="ToDo List", font=("Comic Sans MS", 28, "bold"))        
        head_canvas.grid(column=0, row=1)

        addItemLabel = Label(todoFrame, text="Add Items")

        addItemText = Text(todoFrame, height=1, width=30)

        addItemLabel.grid(column=0, row=2, sticky=W)



        todoFrame.pack()


        root.mainloop()
        pass

if __name__=="__main__":
    app = ToDoListApp()