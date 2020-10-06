from tkinter import *

root = Tk()

data = StringVar()
qnt = IntVar()


class ShopP:
    def __init__(self, master):
        self.frame = Frame(master, width=1920, height=1080, bg="#a64dff")
        self.Lb = Listbox(self.frame, selectmode=MULTIPLE)
        self.Lb.insert(1, "Pen")
        self.Lb.insert(2, "Pencil")
        self.Lb.insert(3, "Paper")
        self.Lb.pack()
        self.Button3 = Button(self.frame, text="+", command=self.add1).pack()
        self.entry1 = Entry(self.frame, textvariable=qnt).pack()
        self.Button4 = Button(self.frame, text="-", command=self.sub).pack()
        self.button1 = Button(self.frame, text="add", command=self.show).pack()
        self.button2 = Button(self.frame, text="remove").pack()
        self.tx = Text(self.frame, width=20, height=10)
        self.tx.pack()
        self.frame.pack()

    def add1(self):
        qnt.set(qnt.get() + 1)

    def sub(self):
        while qnt.get() != 1:
            qnt.set(qnt.get() - 1)

    # def add(self):
    #     data = self.Lb.get(ACTIVE)

    def show(self):
        qnt.set(1)
        items = self.Lb.curselection()
        self.tx.insert(END, self.Lb.get(items))


b = ShopP(root)
root.mainloop()
