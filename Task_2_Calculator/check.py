import tkinter as tk

def button_click(text):
    label.config(text=f"Button Clicked: {text}")

root = tk.Tk()
root.title("Get Text of Clicked Button")

label = tk.Label(root, text="Click a button.")
label.pack()

button_texts = ["Button 1", "Button 2", "Button 3"]

for text in button_texts:
    button = tk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.pack()

root.mainloop()