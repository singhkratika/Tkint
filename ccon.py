from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
from currency_converter import CurrencyConverter
cor0="#FFFFFF"
cor1="#333333"
cor2="#EB5D51"

window=Tk()
a=CurrencyConverter()
window.geometry("300x320")
window.title("Converter")
window.config(bg=cor0)
window.resizable(height=FALSE,width=FALSE)

top=Frame(window,width=300,height=60,bg=cor2)
top.grid(row=0,column=0)

main=Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)

def convert():
	currency_1=combo1.get()
	currency_2=combo2.get()
	amount=value.get()
	if currency_2=="USD":
		symbol="$"
	elif currency_2=="INR":
		symbol="₹"
	elif currency_2=="EUR":
		symbol="€"
	elif currency_2=="BRL":
		symbol="R$"
	elif currency_2=="CAD":
		symbol="CA $"
	data=a.convert(amount,currency_1,currency_2)
	data = round(data, 2)
	result["text"]=symbol+" "+str(data)

icon=Image.open("th.jpg")
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)

app_name=Label(top,image=icon,compound=LEFT,text="Currency Converter",height=5,padx=13,pady=30,anchor=CENTER,font=("Arial 16 bold"),bg=cor2,fg=cor0)
app_name.place(x=0,y=0)

result=Label(main,text=" ",relief="solid",width=16,height=2,pady=7,anchor=CENTER,font=("Ivy 15 bold"),bg=cor0,fg=cor1)
result.place(x=50,y=10)

currency=["CAD","BRL","EUR","INR","USD"]

from_label=Label(main,text="From",relief="flat",width=8,height=1,pady=0,padx=0,anchor=NW,font=("Ivy 10 bold"),bg=cor0,fg=cor1)
from_label.place(x=48,y=90)

combo1=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo1["values"]=(currency)
combo1.place(x=50,y=115)

to_label=Label(main,text="To",relief="flat",width=8,height=1,pady=0,padx=0,anchor=NW,font=("Ivy 10 bold"),bg=cor0,fg=cor1)
to_label.place(x=158,y=90)

combo2=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo2["values"]=(currency)
combo2.place(x=160,y=115)

value=Entry(main,width=22, justify=CENTER, font=("Ivy 12 bold"),relief=SOLID)
value.place(x=50,y=155)

button=Button(main,text="Converter",font=("Ivy 12 bold"),width=19,height=1, padx=5, bg=cor2,fg=cor0,command=convert)
button.place(x=50, y=210)

window.mainloop()