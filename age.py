from tkinter import*
from datetime import date
def calculator():
 global result
 result=str(entry.get())
 today=date.today()
 dob_date=result.split("/")
 date1=int(dob_date[0])
 month=int(dob_date[1])
 year=int(dob_date[2])
 dob=date(year,month,date1)
 numberOfDays = (today-dob).days
 age = numberOfDays // 365
 label=Label(root,text="your age is"+str(age))
 label.pack()

root=Tk()
root.geometry("300x300")
entry=Entry(root)
entry.pack()

button=Button(root,text="Age",command=calculator)
button.pack()
root.mainloop()