import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk
def eat(event):
    print("Вкуснятина")
def make(event):
    print ("Бутер с колбасой готов")
root = tk.Tk()
root.title("Sandwich")
tk.Button(root, text="Make me a Sandwich").pack()
tk.Button(root, text="Eat my Sandwich").pack()

tk.mainloop()