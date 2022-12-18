from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        # 1
        img=Image.open(r"Images\images.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        #First image Or First Label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #2
        img1=Image.open(r"Images\facialrecognition.webp")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #3
        img2=Image.open(r"Images\chandigarh-group-of-colleges-cgc-landran-mohali.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # Background image
        img3=Image.open(r"Images\wp10348233-aesthetic-anime-scenery-4k-wallpapers.jpg")
        img3=img3.resize((1535,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1535,height=710)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System", font=("Times New Roman",35,"bold"), bg="white", fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student button
        img4=Image.open(r"Images\Team_Kakashi.webp")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)        

        b1_1=Button(bg_img,text="Students Details",command=self.student_details, cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 

        # Detect Face button
        img5=Image.open(r"Images\face-600x900.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,command=self.face_data,image=self.photoimg5, cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)        

        b1_1=Button(bg_img,command=self.face_data,text="Face Detector", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)  


        # Attendance  button
        img6=Image.open(r"Images\aacb5c367ad54d04920af5e1a303a591.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,command=self.Attendance,image=self.photoimg6, cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)        

        b1_1=Button(bg_img,command=self.Attendance,text="Attendance", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)  

        # Help Desk Button
        img7=Image.open(r"Images\download.jpeg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,command=self.Help,image=self.photoimg7, cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)        

        b1_1=Button(bg_img,command=self.Help,text="Help Desk", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)  


        # Train button
        img8=Image.open(r"Images\1_6w8Iqm27n9RgHrRZOqbYKQ.jpeg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_data,image=self.photoimg8, cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)        

        b1_1=Button(bg_img,command=self.train_data,text="Train", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)  

        # Photos butto9
        img9=Image.open(r"Images\wp6934682.webp")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)        

        b1_1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img, font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)  

        # Developer Button
        img10=Image.open(r"Images\HD-wallpaper-anime-boy-aqua-hair-profile-view-headphones-computer-smiling-anime.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,command=self.Developer,image=self.photoimg10, cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)        

        b1_1=Button(bg_img,command=self.Developer,text="Developer", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)  

        # Exit Button
        img11=Image.open(r"Images\depositphotos_23855751-stock-illustration-exit-icon.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg11, cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)        

        b1_1=Button(bg_img,command=self.iExit,text="Exit", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)  

        # # Chat bot button
        # ch_1=Button(bg_img,command=self.Chat,text="Chat", cursor="hand2", font=("Times New Roman",15,"bold"), bg="purple", fg="white")
        # ch_1.place(x=1400,y=350,width=220,height=40)



    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else: 
            return
        #=======================function buttons================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    # def Chat(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Chatbot(self.new_window)

    




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()