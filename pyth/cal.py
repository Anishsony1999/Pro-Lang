import tkinter as tk

def butten_click(val):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END,current + val)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except Exception as e :
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")
    
def clear():
    entry.delete(0,tk.END)


root = tk.Tk()

root.title("calculator")

entry = tk.Entry(root,width=16,font=("robot",26),borderwidth=2,relief="solid",justify="right")
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
]

for (text,row,col) in buttons:
    if text == '=':
        button = tk.Button(root,text=text,width=10,height=2,command=evaluate)
    else:
        button = tk.Button(root,text=text,width=5,height=2,command=lambda val=text : butten_click(val))
    button.grid(row=row,column=col,padx=5,pady=5)

clear_butten = tk.Button(root,text="C",command=clear)
clear_butten.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

root.mainloop()