from tkinter import *
import mysql.connector

mydb3 = mysql.connector.connect(host="localhost", user="root", password="", database="Shop")

root = Tk()
root.title("Supermarket System : HomePage")
root.overrideredirect(True)
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(False, False)
root.configure(background="black")


root.geometry("1920x1080")
fame = Frame(root, bg="red").pack()
m1cursor = mydb3.cursor()
sql = "INSERT INTO items (Product_Id,Product_Name, Product_Quantity) VALUES (%s, %s, %s)"
val = (7, 'A', 20)
m1cursor.execute(sql, val)
mydb3.commit()
root.mainloop()
