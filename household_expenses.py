import tkinter as tk
from tkinter import ttk
import datetime
today_date = datetime.datetime.today().strftime('%Y-%m-%d')
root = tk.Tk()
root.title("Home spends")
root.geometry('800x600')
root.minsize(width=800, height=600)
a = 0
def add_position():
    if (entry1.get() != '' and entry2.get() != '' and entry3.get() != '' 
        and (entry2.get().replace(".", "", 1).isdigit() == True or entry2.get().replace(",", "", 1).isdigit()) == True): #isdigit() checks is value digits, replace 1 (means one instane is exchanged)
        global a
        a = a + 1
        activity = entry1.get()
        value = float(entry2.get().replace(',','.')) #replacing if comma appears
        date = entry3.get()
        tree.insert('', 'end', text = a, values=(activity, value, date))
        #tree.configure(background='#334353')
        clear_entry = tk.StringVar(frame, value = '')
        #entry1.delete(0, 'end') #from 0 position to end
        #entry2.delete(0, 'end')
        
def edit_position():
    activity = ("zakupy w biedro")
    value = 150.15
    date = "2019-04-05"
    #at = tk.StringVar(frame, value = activity)
    entry1.delete(0, tk.END)
    entry1.insert(0, activity)
    entry2.delete(0, tk.END)
    entry2.insert(0, value)
    entry3.delete(0, tk.END)
    entry3.insert(0, date)

def delete_position():
    try:
        selected_item = tree.selection()[0] #get selected row
        tree.delete(selected_item)
    except:
        pass
    
    
#class DataTree:
#    def __init__(self, master):
        
        
        
        
        



#------creating menu bar--------
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu, tearoff=0) #tearoff can undock menu
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "New")
filemenu.add_separator()
filemenu.add_command(label = "Open")
filemenu.add_command(label = "Save")
filemenu.add_command(label = "Save As..")
filemenu.add_command(label = "Exit", command = quit)

button1 = ttk.Button(root, text='Add', command = add_position).grid(row=0, column=6)
button2 = ttk.Button(root, text='Edit', command = edit_position).grid(row=0, column=7)
button3 = ttk.Button(root, text='Delete', command = delete_position).grid(row=0, column=8)

entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = ttk.Entry(root)
entry2.grid(row=0, column=3)
td = tk.StringVar(root, value = today_date)
entry3 = ttk.Entry(root, textvariable = td)
entry3.grid(row=0, column=5)



ttk.Label(root, text="Activity").grid(row=0, column=0)
ttk.Label(root, text="Value [z³]").grid(row=0, column=2)
ttk.Label(root, text="Date").grid(row=0, column=4)



#---- frame ----
frame = tk.Frame(root, bg='#80c1ff')
#frame.place(relx=0.01, rely=0.1, relwidth=0.9, relheight=0.9, width=100)
#frame.place(x=10, y=10, relwidth=0.9, relheight=0.9, width=100)
frame.grid(row=1, column=0, columnspan=8)


tree = ttk.Treeview(frame, height=10, columns=('ID', 'Activities', 'Value[PLN]', 'Date'))
vsb = ttk.Scrollbar(orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

tree.heading('#0', text='ID', anchor=tk.CENTER)
tree.heading('#1', text='Activities', anchor=tk.CENTER)
tree.heading('#2', text='Value[PLN]', anchor=tk.CENTER)
tree.heading('#3', text='Date', anchor=tk.CENTER)

tree.column('#0', stretch=tk.NO, width=50)
tree.column('#1', stretch=tk.YES, minwidth=50, width=100)
tree.column('#2', stretch=tk.YES, minwidth=50, width=100)
tree.column('#3', stretch=tk.YES, minwidth=50, width=100)

label1 = ttk.Label(root, text='Sum:')
label1.grid(row=2,column=0)


#tree.insert('', 1, text="1", values=("text","przykładowy","01-01-2018"))
#tree.insert('', 2, text="3")
#tree.insert('', 'end', text="2")

tree.grid(row=1, column=0, columnspan=9, sticky='NSEW', in_=frame)
vsb.grid(column=9, row=0, rowspan=3, sticky='ns', in_=frame)



if __name__ == "__main__":
    root.mainloop()
