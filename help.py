from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK", font=("Times New Roman",35,"bold"), bg="dark blue", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Images\wp8358553.webp")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=730)

        dev_lablel=Label(f_lbl,text="Email: 1914416.cse.coe@cgc.edu.in",font=("Times New Roman",17,"bold"),bg="White")
        dev_lablel.place(x=550,y=280)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()