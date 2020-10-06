import mysql.connector
import mysql
from tkinter import *
from tkinter import messagebox
import os

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Shop")

root1 = Tk()
en1 = StringVar()
en2 = StringVar()
en3 = StringVar()


class ShopP:
    def __init__(self, master):
        master.geometry("1920x1080")
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")

        self.canvas = Canvas(self.frame, width=200, height=159)
        self.canvas.place(x=0, y=0)
        self.photo1 = PhotoImage(file="shop.png")
        self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)

        self.label1 = Label(self.frame, text="A's Supermarket", font="Consolas 40 bold")
        self.label1.place(x=550, y=60)

        self.frame2 = Frame(self.frame, bg="#9933ff")
        self.frame2.place(x=0, y=190)
        self.button1 = Button(self.frame2, font="30", text="Home", bg="#a64dff", command=self.ref)
        self.button2 = Label(self.frame2, font="30", text="Shop", bg="#9933ff")
        self.button3 = Button(self.frame2, font="30", bg="#a64dff", text="bill", command=self.ref1)
        self.photo2 = PhotoImage(file="exit.png")
        self.button4 = Button(self.frame2, image=self.photo2, font="30", command=self.qu)
        self.button1.pack(side=LEFT, padx=160)
        self.button2.pack(side=LEFT, padx=160)
        self.button3.pack(side=LEFT, padx=160)
        self.button4.pack(side=RIGHT, padx=180)
        self.frame3 = Frame(master, bg="#9933ff", width=800, height=470)
        self.button5 = Button(self.frame3, text="Update", command=self.update)
        self.button5.place(x=270, y=0)
        self.entry1 = Entry(self.frame3, textvariable=en1, width=3, font="0 14")
        self.entry1.place(x=320, y=0)
        self.entry2 = Entry(self.frame3, textvariable=en2, width=10, font="0 14")
        self.entry2.place(x=370, y=0)
        self.entry3 = Entry(self.frame3, textvariable=en3, width=3, font="0 14")
        self.entry3.place(x=490, y=0)
        self.button6 = Button(self.frame3, text="Show", command=self.Show)
        self.button6.place(x=530, y=0)
        self.t = Text(self.frame3, bd=4)
        self.t.place(x=75, y=30)
        self.frame3.place(x=350, y=300)
        self.frame.pack()

    def update(self):
        m1cursor = mydb.cursor()
        sql = "INSERT INTO items (Product_Id,Product_Name, Product_Quantity) VALUES (%s, %s, %s)"
        val = (en1.get(), en2.get(), en3.get())
        m1cursor.execute(sql, val)
        mydb.commit()

    def Show(self):
        self.t.delete(1.0, END)
        mcursor = mydb.cursor()
        mcursor.execute("select Product_Name,Product_Quantity from items")
        myresult = mcursor.fetchall()
        for column in myresult:
            self.t.insert(END, column)
            self.t.insert(END, "\n")

    def qu(self):
        answer = messagebox.askquestion("Exit", "Do you really want to exit?")
        if answer == "yes":
            root1.quit()

    def ref(self):
        root1.destroy()
        os.system('HomePage.py')


    def ref1(self):
        root1.destroy()
        os.system('BillPage.py')


# def donothing():
#     pass

root1.title("Supermarket System : ShopPage")
# root1.protocol('WM_DELETE_WINDOW', donothing)
f = ShopP(root1)
root1.mainloop()
