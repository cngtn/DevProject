from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector



class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500+0+0")
        self.root.title("Register")
        self.root.option_add("*tearOff", False)

#==========variable==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_regUser = StringVar()
        self.var_regPwd = StringVar()
        self.var_cfPwd = StringVar()
        self.var_email = StringVar()



#Bg image
        img3 = Image.open(r"assets/img/loginwd.jpg")
        img3 = img3.resize((800,500),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 800, height = 500)

#Main frame
        main_frame = Frame(bg_img, bg = "#03153B")
        main_frame.place(x = 440, y = 0, width = 445, height = 500)

        img4 = Image.open(r"assets/img/UserReg.png")
        img4 = img4.resize((80,80),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img4 = Label(self.root, image = self.photoimg4, bg = "#03153B")
        lbl_img4.place(x = 580,y = 5, width = 75, height = 75)
        
        login = Label(main_frame, text = "Đăng ký", font = ("Google Sans",20,"bold"),fg = "white", bg = "#03153B")
        login.place(x = 120, y = 50, width = 110, height = 100)

#Label and Entry

        fname = Label(main_frame, text = "Họ: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        fname.place(x = 15, y = 140, width = 30, height = 20)

        self.txtname = ttk.Entry(main_frame,textvariable = self.var_fname, font = ("Google Sans",10,"bold"), width = 17)
        self.txtname.place(x = 160, y = 135, width = 175, height = 33)

        lname = Label(main_frame, text = "Tên: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        lname.place(x = 15, y = 190, width = 35, height = 20)

        self.txtLname = ttk.Entry(main_frame, textvariable = self.var_lname, font = ("Google Sans",10,"bold"), width = 17)
        self.txtLname.place(x =160, y = 185, width = 175, height = 33)

        regUser = Label(main_frame, text = "Tên đăng nhập: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        regUser.place(x = 15, y = 240, width = 120, height = 20)

        self.txtregUser = ttk.Entry(main_frame, textvariable = self.var_regUser, font = ("Google Sans",10,"bold"), width = 17)
        self.txtregUser.place(x =160, y = 235, width = 175, height = 33)

        regPwd = Label(main_frame, text = "Mật khẩu: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        regPwd.place(x = 15, y = 290, width = 80, height = 20)

        self.txtregPwd = ttk.Entry(main_frame, textvariable = self.var_regPwd, font = ("Google Sans",10,"bold"), width = 17)
        self.txtregPwd.place(x =160, y = 285, width = 175, height = 33)

        cfPwd = Label(main_frame, text = "Nhập lại Mật khẩu: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        cfPwd.place(x = 15, y = 340, width =135, height = 20)

        self.txtregcfPwd = ttk.Entry(main_frame, textvariable = self.var_cfPwd, font = ("Google Sans",10,"bold"), width = 17)
        self.txtregcfPwd.place(x =160, y = 335, width = 175, height = 33)

        email = Label(main_frame, text = "Email: ", font = ("Google Sans",11,"bold"),fg = "#4F6998", bg = "#03153B" )
        email.place(x = 15, y = 390, width =50, height = 20)

        self.txtemail = ttk.Entry(main_frame, textvariable = self.var_email, font = ("Google Sans",10,"bold"), width = 17)
        self.txtemail.place(x =160, y = 385, width = 175, height = 33)

#======Button======
        loginbtn = ttk.Button(main_frame, text = "Đăng nhập", style="ToggleButton")
        loginbtn.place(x = 45, y = 440, width = 125, height = 33)

        regbtn = ttk.Button(main_frame, command = self.register_data, text = "Đăng ký", style="ToggleButton")
        regbtn.place(x = 200, y = 440, width = 125, height = 33)


#=====Function======
    
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get()== "" or self.var_regUser.get()== "" or self.var_regPwd.get() =="" or self.var_cfPwd.get()=="" or self.var_email.get()== "":
            messagebox.showerror("Error", "Không được để trống các trường!")
        elif self.var_regPwd.get() != self.var_cfPwd.get():
            messagebox.showerror("Error", "Mật khẩu không khớp!")
        else:
            conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition')
            print('Connect successfully')  
            cursor = conn.cursor()
            query = ("select * from user_data where user = %s")
            value =(self.var_regUser.get(),)
            cursor .execute(query, value)
            rows = cursor.fetchone()
            if rows != None:
                messagebox.showerror("Error","Tên đăng nhập đã tồn tại, vui lòng thử tên khác!")
            else:
                cursor.execute("insert into user_data values(%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_regUser.get(),
                    self.var_regPwd.get(),
                    self.var_email.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Đăng ký thành công!")



if __name__ == "__main__":
    root =Tk()
    root.option_add("*tearOff", False)

    # Make the app responsive
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)
    root.rowconfigure(index=0, weight=1)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)

    # Create a style
    style = ttk.Style(root)

    # Import the tcl file
    root.tk.call("source", "Azure-ttk-theme/azure-dark.tcl")

    # Set the theme with the theme_use method
    style.theme_use("azure-dark")
    obj = Register(root)
    root.mainloop()