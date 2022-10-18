
import tkinter as tk
from tkinter.ttk import Combobox, Treeview
import csv
import os


###############      FRAME     ############
win = tk.Tk()
win.title("STUDENT MANAGEMENT PROJECT")
x = win.winfo_screenwidth()
y = win.winfo_screenheight()
win.geometry("{}x{}+{}+{}".format(x,y,0,0))
win.config(bg='teal')

lbl_frame = tk.Label(win, text="STUDENT MANAGEMENT PROJECT", bd=4, 
    bg='white', font=('arial', 24, 'bold'), 
    fg='black', relief=tk.GROOVE)
lbl_frame.pack(fill=tk.X)
###############  FRAME ENTRY   ############
ent_frame = tk.Frame(win, bg='white')
ent_frame.place(x=5, y=50, width=400, height=740)
lbl_menu = tk.Label(ent_frame, text='ENTRY THIS',bd=4, 
    bg='teal', font=('ROBOTO', 20, 'bold'), 
    fg='black', relief=tk.GROOVE) 
lbl_menu.pack(fill=tk.X)

# LABELS
lbl_ID = tk.Label(ent_frame, text="NUMBER ID", font=('times new roman', 20, 'bold'), bg='white')
lbl_ID.place(x=10, y=70)

lbl_GENDER = tk.Label(ent_frame, text="GENDER", font=('times new roman', 20, 'bold'), bg='white')
lbl_GENDER.place(x=250, y=70)

lbl_FNAME = tk.Label(ent_frame, text="FULL NAME", font=('times new roman', 20, 'bold'), bg='white')
lbl_FNAME.place(x=10, y=150)

lbl_AGE = tk.Label(ent_frame, text="AGE", font=('times new roman', 20, 'bold'), bg='white')
lbl_AGE.place(x=10, y=230)

lbl_DOB = tk.Label(ent_frame, text="BIRTHDAY", font=('times new roman', 20, 'bold'), bg='white')
lbl_DOB.place(x=10, y=310)

lbl_EMAIL = tk.Label(ent_frame, text="EMAIL", font=('times new roman', 20, 'bold'), bg='white')
lbl_EMAIL.place(x=10, y=390)

lbl_ADDRESS = tk.Label(ent_frame, text="ADDRESS", font=('times new roman', 20, 'bold'), bg='white')
lbl_ADDRESS.place(x=10, y=470)

lbl_MARK = tk.Label(ent_frame, text="TOTAL MARK", font=('times new roman', 20, 'bold'), bg='white')
lbl_MARK.place(x=10, y=610)


# ENTRY
ent_ID = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_ID.place(x=10, y=110, width=200)

ccb_GENDER = Combobox(ent_frame, values=['MALE', 'FEMALE'], font=('times new roman', 15))
ccb_GENDER.place(x=250, y=110, width=100)

ent_FNAME = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_FNAME.place(x=10, y=190, width=350)

ent_AGE = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_AGE.place(x=10, y=270, width=350)

ent_DOB = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_DOB.place(x=10, y=350, width=350)

ent_EMAIL = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_EMAIL.place(x=10, y=430, width=350)

ent_ADDRESS = tk.Text(ent_frame, font=('times new roman', 15), bd=2)
ent_ADDRESS.place(x=10, y=510, width=350, height=100)

ent_MARK = tk.Entry(ent_frame, font=('times new roman', 15), bd=2)
ent_MARK.place(x=10, y=650, width=350)

###############   DATABASE   #############
def open_database():
    file = open('database.csv', 'r')
    with file:
        data = []
        read = csv.reader(file)
        for row in read:
            data.append(row)
    return data

def remove_data():
    os.remove('database.csv')

def write_data(data):
    file = open('database.csv', 'a+', newline="")
    with file:
        write = csv.writer(file)
        write.writerows(data)

# database = [
#     ['01', 'DINH NHAT ANH', 'MALE', '26', '22/01/1996', 'ANH@GMAIL.COM', '32 XT HD', '9'],
#     ['02', 'DOAN VAN HAU', 'MALE', '22', '05/06/2000', 'HAU@GMAIL.COM', '25 VT HN', '8'],
#     ['03', 'NGUYEN THANH TAM', 'FEMALE', '20', '14/02/2002', 'TAM@GMAIL.COM', '4 QN DN', '9'],
#     ['04', 'PHAM NHAT DONG', 'MALE', '20', '20/10/2002', 'DONG@GMAIL.COM', '48 XT HD', '7'],
#     ['05', 'NGO ANH DUONG', 'FEMALE', '21', '01/01/2001', 'DUONG@GMAIL.COM', '6 TH XT', '8'],
# ]

###############   MAIN   ################
# remove_data()
# write_data(database)

database = open_database()

########  FRAME TREE VIEW  ########
tv_frame = tk.Frame(win, bg='white')
tv_frame.place(x=450, y=50, width=1040, height=600)

lbl_TV = tk.Label(tv_frame, text='TREE VIEW',bd=3, 
    bg='teal', font=('ROBOTO', 20, 'bold'), 
    fg='black', relief=tk.GROOVE) 
lbl_TV.pack(fill=tk.X)

MY_TREE = Treeview(tv_frame)

MY_TREE['columns'] = ('ID', 'NAME', 'GENDER', 'AGE', 'BIRTHDAY', 'EMAIL', 'ADDRESS', 'MARK')
# COLUMNS
MY_TREE.column('#0', width=0, stretch=tk.NO)
MY_TREE.column('ID', width=50, anchor=tk.CENTER)
MY_TREE.column('NAME', width=150)
MY_TREE.column('GENDER', width=50)
MY_TREE.column('AGE', width=50)
MY_TREE.column('BIRTHDAY', width=100)
MY_TREE.column('EMAIL', width=150)
MY_TREE.column('ADDRESS', width=200)
MY_TREE.column('MARK', width=70, anchor=tk.CENTER)

# HEADING
MY_TREE.heading('#0', text='', anchor=tk.W)
MY_TREE.heading('ID', text='ID', anchor=tk.CENTER)
MY_TREE.heading('NAME', text='FULL NAME', anchor=tk.W)
MY_TREE.heading('GENDER', text='GENDER', anchor=tk.CENTER)
MY_TREE.heading('AGE', text='AGE', anchor=tk.CENTER)
MY_TREE.heading('BIRTHDAY', text='BIRTHDAY', anchor=tk.W)
MY_TREE.heading('EMAIL', text='EMAIL', anchor=tk.W)
MY_TREE.heading('ADDRESS', text='ADDRESS', anchor=tk.W)
MY_TREE.heading('MARK', text='MARK', anchor=tk.CENTER)


global count
count = 0
for record in database:
    MY_TREE.insert(parent="", index="end", iid=count, text="", 
        values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
    count += 1


MY_TREE.pack(padx=5, pady=10, fill=tk.BOTH, expand=True)

#===========   FUNCTION   ====================

def loop_treeview():
    new_data = []
    for id in MY_TREE.get_children():
        idx, name, gen, age, bod, eml, addr, mark = MY_TREE.item(id)['values']
        data = [idx, name, gen, age, bod, eml, addr, mark]
        new_data.append(data)
    return new_data

def add_record():
    global count
    MY_TREE.insert(parent="", index="end",iid=count, text="", 
        values=(ent_ID.get(), ent_FNAME.get(), ccb_GENDER.get(), 
        ent_AGE.get(), ent_DOB.get(), ent_EMAIL.get(), 
        ent_ADDRESS.get("1.0", tk.END), ent_MARK.get())
        )
    count += 1
    data = []
    data.append([ent_ID.get(), ent_FNAME.get(), ccb_GENDER.get(), 
        ent_AGE.get(), ent_DOB.get(), ent_EMAIL.get(), 
        ent_ADDRESS.get("1.0", tk.END), ent_MARK.get()])
    remove_data()
    write_data(data)

    ent_ID.delete(0, tk.END)
    ent_FNAME.delete(0, tk.END)
    ccb_GENDER.delete(0, tk.END)
    ent_AGE.delete(0, tk.END)
    ent_DOB.delete(0, tk.END)
    ent_EMAIL.delete(0, tk.END)
    ent_ADDRESS.delete(1.0, tk.END)
    ent_MARK.delete(0, tk.END)

def update_record():
    
    selected = MY_TREE.focus()
    MY_TREE.item(selected, text="", 
        values=(ent_ID.get(), ent_FNAME.get(), ccb_GENDER.get(), 
            ent_AGE.get(), ent_DOB.get(), ent_EMAIL.get(), 
            ent_ADDRESS.get("1.0", tk.END), ent_MARK.get()))

    ent_ID.delete(0, tk.END)
    ent_FNAME.delete(0, tk.END)
    ccb_GENDER.delete(0, tk.END)
    ent_AGE.delete(0, tk.END)
    ent_DOB.delete(0, tk.END)
    ent_EMAIL.delete(0, tk.END)
    ent_ADDRESS.delete(1.0, tk.END)
    ent_MARK.delete(0, tk.END)
    new_data = loop_treeview()
    remove_data()
    write_data(new_data)

def remove_record():
    x = MY_TREE.selection()[0]
    MY_TREE.delete(x)
    new_data = loop_treeview()
    remove_data()
    write_data(new_data)

def select_record():
    ent_ID.delete(0, tk.END)
    ent_FNAME.delete(0, tk.END)
    ccb_GENDER.delete(0, tk.END)
    ent_AGE.delete(0, tk.END)
    ent_DOB.delete(0, tk.END)
    ent_EMAIL.delete(0, tk.END)
    ent_ADDRESS.delete(1.0, tk.END)
    ent_MARK.delete(0, tk.END)

    selected = MY_TREE.focus()
    values = MY_TREE.item(selected, 'values')
    
    
    ent_ID.insert(0, values[0])
    ent_FNAME.insert(0, values[1])
    ccb_GENDER.insert(0, values[2])
    ent_AGE.insert(0, values[3])
    ent_DOB.insert(0, values[4])
    ent_EMAIL.insert(0, values[5])
    ent_ADDRESS.insert(1.0, values[6])
    ent_MARK.insert(0, values[7])


########  FRAME BUTTONS  ########
btn_frame = tk.Frame(win, bg='teal')
btn_frame.place(x=470, y=660, width=1000, height=120)
# Buttons
btn_Add = tk.Button(btn_frame, text="ADD", bd=2, 
    background='teal', relief=tk.GROOVE,
    font=('ROBOTO', 20, 'bold'), width=14, command=add_record)
btn_Add.grid(row=0, column=0)

btn_Update = tk.Button(btn_frame, text="UPDATE", bd=2, 
    background='teal', relief=tk.GROOVE,
    font=('ROBOTO', 20, 'bold'), width=14, command=update_record)
btn_Update.grid(row=0, column=1, padx=20)

btn_Remove = tk.Button(btn_frame, text="REMOVE", bd=2, 
    background='teal', relief=tk.GROOVE,
    font=('ROBOTO', 20, 'bold'), width=14, command=remove_record)
btn_Remove.grid(row=0, column=2, padx=5)

btn_Select = tk.Button(btn_frame, text="SELECT", bd=2, 
    background='teal', relief=tk.GROOVE,
    font=('ROBOTO', 20, 'bold'), width=14, command=select_record)
btn_Select.grid(row=0, column=3, padx=10)


win.mainloop()

