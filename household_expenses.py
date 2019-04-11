import tkinter as tk
from tkinter import ttk
import datetime
today_date = datetime.datetime.today().strftime('%d-%m-%Y')

root = tk.Tk()
root.title("Home spends")
root.geometry('800x600')
root.minsize(width=800, height=600)


frame = tk.Frame(root, bg='#80c1ff')
#frame.place(relx=0.01, rely=0.1, relwidth=0.9, relheight=0.9, width=100)
frame.place(x=10, y=10, relwidth=0.9, relheight=0.9, width=100)

ttk.Label(frame, text="Activity").grid(row=0, column=0)
ttk.Label(frame, text="Value [zł]").grid(row=0, column=2)
ttk.Label(frame, text="Date").grid(row=0, column=4)

entry1 = ttk.Entry(frame).grid(row=0, column=1)
entry2 = ttk.Entry(frame).grid(row=0, column=3)
entry3 = ttk.Entry(frame, textvariable = today_date).grid(row=0, column=5)
#entry3.insert(0,"cokolwiek")

button1 = ttk.Button(frame,text='Add').grid(row=0, column=6)
button2 = ttk.Button(frame,text='Edit').grid(row=0, column=7)
button3 = ttk.Button(frame,text='Delete').grid(row=0, column=8)

tree = ttk.Treeview(frame, height=10, columns=('ID', 'Activities', 'Value[PLN]', 'Date'))


tree.heading('#0', text='ID', anchor=tk.CENTER)
tree.heading('#1', text='Activities', anchor=tk.CENTER)
tree.heading('#2', text='Value[PLN]', anchor=tk.CENTER)
tree.heading('#3', text='Date', anchor=tk.CENTER)

tree.column('#0', stretch=tk.NO, width=50)
tree.column('#1', stretch=tk.YES, minwidth=50, width=100)
tree.column('#2', stretch=tk.YES, minwidth=50, width=100)
tree.column('#3', stretch=tk.YES, minwidth=50, width=100)

tree.insert('', 1, text="1",values=("text","przykładowy","01-01-2018"))
tree.insert('', 2, text="3")
tree.insert('', 'end', text="2")

tree.grid(row=2, column=0, columnspan=9, sticky='NSEW')


if __name__ == "__main__":
    root.mainloop()

