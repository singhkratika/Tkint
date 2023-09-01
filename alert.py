from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Alert Message Box")
root.geometry("200x200")
def msg():
 messagebox.showwarning("Alert Box","stop virus found")
button=Button(root,text="ok",command=msg)
button.place(x=100,y=100)


root.mainloop()