from tkinter import *
import mysql.connector

mydb3 = mysql.connector.connect(host="localhost", user="root", password="", database="Shop")

root = Tk()

root.geometry("1920x1080")
fame = Frame(root, bg="#a64dff").pack()
m1cursor = mydb3.cursor()
sql = "INSERT INTO items (Product_Id,Product_Name, Product_Quantity) VALUES (%s, %s, %s)"
val = (7, 'A', 20)
m1cursor.execute(sql, val)
mydb3.commit()
root.mainloop()
