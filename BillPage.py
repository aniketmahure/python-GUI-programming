from tkinter import *
from tkinter import messagebox
import os
from tkinter import Tk
import mysql.connector

mydb2 = mysql.connector.connect(host="localhost", user="root", password="", database="Shop")

root2 = Tk()

qnt = IntVar()
s = StringVar()
Entry1 = StringVar()
Entry2 = StringVar()


class ShopP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")

        self.canvas = Canvas(self.frame, width=200, height=159, bg="#a64dff")
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="buy.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="Consolas 40 bold", bg="#a64dff")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame, bg="#9933ff")
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="0 15", text="Home", command=ref, bg="#a64dff")
        self.button2 = Button(self.frame2, font="0 15", text="Shop", command=ref1, bg="#a64dff")
        self.button3 = Label(self.frame2, font="0 15", text="Bill", bg="#9933ff")
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, text="Quit", image=self.photo2, command=qu, bg="#a64dff")
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)
        self.frame4 = Frame(self.frame, bg="#a64dff", height=475)
        self.frame4.place(x=100, y=290)
        self.frame3 = Frame(self.frame, bg="#9933ff", width=825, height=475)
        self.frame3.place(x=600, y=290)
        self.Entry = Entry(self.frame4, textvariable=s).grid(row=0, column=0)
        s.set("Search")
        self.button5 = Button(self.frame4, text="search").grid(row=0, column=1)
        self.label2 = Label(self.frame4, text="Items").grid(row=1, column=0)
        self.button6 = Button(self.frame4, text="+", command=self.add).grid(row=2, rowspan=1, column=4)
        self.Entry3 = Entry(self.frame4, width=4, textvariable=qnt).grid(row=2, column=5)
        qnt.set(1)
        self.button7 = Button(self.frame4, text="-", command=self.sub).grid(row=2, column=6)
        self.button8 = Button(self.frame4, text="Add", command=self.add1).grid(row=3, column=4)
        self.button9 = Button(self.frame4, text="Clear", command=self.remov).grid(row=3, column=5)

        self.Lb1 = Listbox(self.frame4, font="0 10")
        mcursor = mydb2.cursor()
        mcursor.execute("select Product_Name from items")
        myresult = mcursor.fetchall()
        for column in myresult:
            self.Lb1.insert(1, column)
        self.Lb1.grid(row=2, column=0)

        self.label5 = Label(self.frame3, text="Customer Name").grid(row=0, column=0)
        self.Entry1 = Entry(self.frame3, bd=8).grid(row=0, column=1)
        self.label6 = Label(self.frame3, text="Mobile No").grid(row=1, column=0)
        self.Entry2 = Entry(self.frame3, bd=8).grid(row=1, column=1)
        self.label7 = Label(self.frame3, text="Selected Items").grid(row=2, columnspan=2)

        self.t = Text(self.frame3, height=7, width=30, bd=8)
        self.t.grid(row=3, column=0)
        self.button10 = Button(self.frame3, text="Total").grid(row=4, columnspan=3)
        self.label8 = Label(self.frame3, text="Total Items").grid(row=5, column=0)
        self.label9 = Label(self.frame3).grid(row=6, column=0)
        self.label10 = Label(self.frame3, text="Total Amount").grid(row=5, column=1)
        self.label11 = Label(self.frame3).grid(row=6, column=1)
        self.frame.pack()

    def add(self):
        qnt.set(qnt.get() + 1)

    def sub(self):
        while qnt.get() != 1:
            qnt.set(qnt.get() - 1)

    def add1(self):
        items1 = self.Lb1.curselection()
        self.t.insert(END, self.Lb1.get(items1), "", qnt.get())
        # if self.Lb1.get(items1) == 'Biscuits':
        # count = qnt.get() + count
        # print(count)
        self.t.insert(END, "\n")
        qnt.set(1)

    def remov(self):
        self.t.delete(1.0, END)

    def total(self):
        count = 0
        tn = count + qnt.get()
        print(tn)


def qu():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root2.quit()


def donothing():
    pass


def ref():
    root2.destroy()
    os.system('HomePage.py')


def ref1():
    root2.destroy()
    os.system('shopPage.py')

# root2.protocol('WM_DELETE_WINDOW', donothing)
f = ShopP(root2)
root2.mainloop()
root2.resizable(False, False)
root2.title("Supermarket System : BillPage")
