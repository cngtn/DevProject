from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x783+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)


        # =============== Variable =============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.serchTxt_var=StringVar()
        self.serch_var=StringVar()


        #Bg image
        img3 = Image.open(r"assets/img/bg_img.png")
        img3 = img3.resize((1195,790),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 790)

        main_frame = ttk.Frame(bg_img)
        main_frame.place(x = 25, y = 110, width = 1145, height = 650)

        #Left frame
        Left_frame = ttk.Labelframe(main_frame, text = "Thông tin sinh viên")
        Left_frame.place(x = 10, y = 10, width =555, height =  635)


        #Student details
        img_left = Image.open(r"assets/img/studentDetails.png")
        img_left = img_left.resize((545,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = ttk.Label(Left_frame, image = self.photoimg_left, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)

        # Current course information
        current_course_frame = ttk.Labelframe(Left_frame, text = "Thông tin môn học")
        current_course_frame.place(x = 5, y = 135, width =543, height =  120)
        
        
        #Dapartment
        dep_label = ttk.Label(current_course_frame, text = "Ngành:")
        dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        
        dep_combo = ttk.Combobox(current_course_frame, textvariable = self.var_dep, width =17, state = "readonly")
        dep_combo["values"] = ("", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx=5, pady=10, ipadx = 20, sticky = W)

        #Course
        course_label = ttk.Label(current_course_frame, text = "Khoá học:")
        course_label.grid(row = 0, column = 2, padx = 10, sticky = W)

        
        course_combo = ttk.Combobox(current_course_frame, textvariable = self.var_course, width =17, state = "readonly")
        course_combo["values"] = ("", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row = 0, column = 3, padx=5, pady=10, ipadx = 20, sticky = W)


        #year
        year_label = ttk.Label(current_course_frame, text = "Năm học:")
        year_label.grid(row = 1, column = 0, padx = 10, sticky = W)

        
        year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_year, width =17, state = "readonly")
        year_combo["values"] = ("", "2021 - 2022", "2022 - 2023", "2023 - 2024", "2024 - 2025")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx=2, pady=10, ipadx = 20, sticky = W)


        #Semester
        semester_label = ttk.Label(current_course_frame, text = "Học kì:")
        semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)

        
        semester_combo = ttk.Combobox(current_course_frame, textvariable = self.var_semester, width =17, state = "readonly")
        semester_combo["values"] = ("", "Semester - 1", "Semester - 2", "Semester - 3", "Semester - 4")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx=5, pady=10, ipadx = 20, sticky = W)


        # Class student information
        class_student_frame = ttk.Labelframe(Left_frame, text = "Thông tin Sinh viên")
        class_student_frame.place(x = 5, y = 260, width =543, height =  350)

        #Student ID
        studentId_label = ttk.Label(class_student_frame, text = "Mã Sinh viên")
        studentId_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable = self.var_std_id, width = 20)
        studentID_entry.grid(row = 0, column = 1, padx=5, ipadx = 10, sticky = W)


        #Student name
        studentName_label = ttk.Label(class_student_frame, text = "Họ tên")
        studentName_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable = self.var_std_name, width = 20)
        studentName_entry.grid(row = 0, column = 3, padx=5, pady = 5, ipadx = 10, sticky = W)


        # Class didvision
        class_div_label = ttk.Label(class_student_frame, text = "Phân lớp:")
        class_div_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

        div_combo = ttk.Combobox(class_student_frame, textvariable = self.var_div, width =17, state = "readonly")
        div_combo["values"] = (" ", "CS", "IS", "CR", "DS",)
        div_combo.current(0)
        div_combo.grid(row = 1, column = 1, padx=2, pady=10, ipadx = 20, sticky = W)


        # Roll No
        roll_no_label = ttk.Label(class_student_frame, text = "Roll No")
        roll_no_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable = self.var_roll, width = 20)
        roll_no_entry.grid(row = 1, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Gender
        gender_label = ttk.Label(class_student_frame, text = "Giới tính: ")
        gender_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        #gender_entry = ttk.Entry(class_student_frame, textvariable = self.var_gender, width = 20)
        #gender_entry.grid(row = 2, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)


        gender_combo = ttk.Combobox(class_student_frame, textvariable = self.var_gender, width =17, state = "readonly")
        gender_combo["values"] = (" ", "Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid(row = 2, column = 1, padx=2, pady=10, ipadx = 20, sticky = W)
        # DOB
        dob_label = ttk.Label(class_student_frame, text = "Ngày sinh")
        dob_label.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        dob_entry = ttk.Entry(class_student_frame, textvariable = self.var_dob, width = 20)
        dob_entry.grid(row = 2, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Email
        email_label = ttk.Label(class_student_frame, text = "Email")
        email_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        email_entry = ttk.Entry(class_student_frame, textvariable = self.var_email, width = 20)
        email_entry.grid(row = 3, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Phone
        phone_no_label = ttk.Label(class_student_frame, text = "Số điện thoại:")
        phone_no_label.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable = self.var_phone, width = 20)
        phone_no_entry.grid(row = 3, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)

        # Address
        address_label = ttk.Label(class_student_frame, text = "Địa chỉ:")
        address_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)

        address_entry = ttk.Entry(class_student_frame, textvariable = self.var_address, width = 20)
        address_entry.grid(row = 4, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)
    

        # Teacher name
        teacher_name_label = ttk.Label(class_student_frame, text = "Giảng viên:")
        teacher_name_label.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable = self.var_teacher, width = 20)
        teacher_name_entry.grid(row = 4, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        #Radio Buttom
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(class_student_frame, variable = self.var_radio1, text = "chụp ảnh mẫu", value = "yes")
        radionbtn1.grid(row = 6, column =1, sticky = W)

        
        radionbtn2 = ttk.Radiobutton(class_student_frame, variable = self.var_radio1, text = "Không có ảnh mẫu", value = "no")
        radionbtn2.grid(row = 6, column =3, sticky = W)

        #Buttom frame
        btn_frame = ttk.Frame(class_student_frame, border= 5)
        btn_frame.place(x = 0, y = 250, width =530, height =40)

        save_btn = ttk.Button(btn_frame, text ="Save", command = self.add_data, style="ToggleButton", width = 15)
        save_btn.grid(row = 0, column = 0, padx = 7)

        update_btn = ttk.Button(btn_frame, text ="Update", command = self.update_data, style="ToggleButton", width = 15)
        update_btn.grid(row = 0, column = 1, padx = 10)


        delete_btn = ttk.Button(btn_frame, text ="Delete", command = self.delete_data, style="ToggleButton", width = 15)
        delete_btn.grid(row = 0, column = 2, padx = 10)

        reset_btn = ttk.Button(btn_frame, text = "Reset", command = self.reset_data, style="ToggleButton", width = 15)
        reset_btn.grid(row = 0, column = 3, padx = 10)

        
        btn_frame1 = ttk.Frame(class_student_frame, border= 5)
        btn_frame1.place(x = 0, y = 290, width =530, height =40)
        
        take_photo_btn = ttk.Button(btn_frame1, text ="Take photo", command = self.generate_dataset, style="ToggleButton", width = 37)
        take_photo_btn.grid(row = 0, column = 0, padx = 7)

        take_photo_btn = ttk.Button(btn_frame1, text ="Upload photo",style="ToggleButton", width = 37)
        take_photo_btn.grid(row = 0, column = 1, padx = 10)




        #Right frame
        Right_frame = ttk.Labelframe(main_frame, text = "bảng thông tin sinh viên")
        Right_frame.place(x = 580, y = 10, width =555, height =  635)

        #Student details
        img_right = Image.open(r"assets/img/Search.png")
        img_right = img_right.resize((545,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = ttk.Label(Right_frame, image = self.photoimg_right, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)


        #============== Search System ====================
        search_frame = ttk.Labelframe(Right_frame, text = "Tìm kiếm thông tin")
        search_frame.place(x = 5, y = 135, width =543, height =  80)

        search_label = ttk.Label(search_frame, text = "Search by:", border = 3)
        search_label.grid(row = 0, column = 0, padx = 7, pady = 5, sticky = W)

        search_combo = ttk.Combobox(search_frame, textvariable = self.serch_var, width =15, state = "readonly")
        search_combo["values"] = ("Select ", "Roll_No", "Number_Phone", "Student_ID")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx=5, pady=10, ipadx = 10, sticky = W)


        search_entry = ttk.Entry(search_frame, textvariable = self.serchTxt_var , width = 15)
        search_entry.grid(row = 0, column = 2, padx=5,pady = 5, ipadx = 10, sticky = W)

        search_btn = ttk.Button(search_frame, text ="Search", command = self.search_data,style="ToggleButton", width = 10)
        search_btn.grid(row = 0, column = 3, padx = 7)

        showAll_btn = ttk.Button(search_frame, text ="Show all", command = self.fetch_data,style="ToggleButton", width = 10)
        showAll_btn.grid(row = 0, column = 4, padx = 7)


        #====================Table Frame====================
        table_frame = ttk.Frame(Right_frame, border = 5 )
        table_frame.place(x = 5, y = 230, width =543, height =  385)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column = ("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand= scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("dep", text = "Ngành: ")
        self.student_table.heading("course", text = "Khoá học")
        self.student_table.heading("year", text = "Năm học")
        self.student_table.heading("sem", text = "Học kì")
        self.student_table.heading("id", text = "Mã Sinh viên")
        self.student_table.heading("name", text = "Tên Sinh viên")
        self.student_table.heading("div", text = "Phân lớp")
        self.student_table.heading("roll", text = "Roll")
        self.student_table.heading("gender", text = "Giới tính")
        self.student_table.heading("dob", text = "Ngày sinh")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("phone", text = "Số điện thoại")
        self.student_table.heading("address", text = "Địa chỉ")
        self.student_table.heading("teacher", text = "Giảng viên")
        self.student_table.heading("photo", text = "Ảnh mẫu")
        self.student_table["show"] = "headings"


        self.student_table.column("dep", width = 100)
        self.student_table.column("course", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("name", width = 100)
        self.student_table.column("div", width = 100)
        self.student_table.column("roll", width = 100)
        self.student_table.column("gender", width = 100)
        self.student_table.column("dob", width = 100)
        self.student_table.column("email", width = 100)
        self.student_table.column("phone", width = 100)
        self.student_table.column("address", width = 100)
        self.student_table.column("teacher", width = 100)
        self.student_table.column("photo", width = 150)


        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
#======================= Function Decration =================================================
    def add_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition')
                print('Connect successfully')  
                cursor = conn.cursor()
                cursor .execute("INSERT INTO student() values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        
                                                                                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Sinh viên đã được thêm thành công !", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)



#============ Fetch data =================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition')
        print('Connect successfully')  
        cursor = conn.cursor()
        cursor.execute("SELECT * from student")
        data = cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values = i)
            conn.commit()
        conn.close()




#===================== Get cursor=================
    def get_cursor(self,event = ''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5])
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
        #self.serchTxt_var.set(data[15]),
        #self.serch_var.set(data[16]),

#============== Update functions =============
    def update_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Cập nhật", "Bạn có muốn cập nhật thông tin sinh viên !",parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition')
                    print('Connect successfully')  
                    cursor = conn.cursor()
                    cursor .execute("update  student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,Division=%s, Roll=%s, Gender=%s,  Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where student_id = %s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công.", "Thông tin sinh viên đã được cập nhật thành công!", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"due to:{str(es)}", parent = self.root)
#=============== Delete function ================

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Lỗi", "Không được để trống mã Sinh viên!", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Thông báo", "Bạn có muốn xoá sinh viên !", parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition')
                    print('Connect successfully')  
                    cursor = conn.cursor()
                    sql = "delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Sinh viên đã được xoá thành công !", parent = self.root)
            except Exception as es:
                messagebox.showerror("Lỗi", f"due to:{str(es)}", parent = self.root)

#============== Reset functions =============
    def reset_data(self):
        self.var_dep.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#========= Cenerate data set or Take photo samples =====
    def generate_dataset(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='250301',
                        host='localhost',
                        database='face_recognition')
                print('Connect successfully')  
                cursor = conn.cursor()
                cursor.execute("select * from student")
                my_result = cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                    cursor .execute("update  student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,Division=%s, Roll=%s, Gender=%s,  Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where student_id = %s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),                                                                                                                       
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                     ))

                conn.commit()
                self.fetch_data()
                self.update_data()
                self.reset_data()
                conn.close()
                print("dong database")
#========= Load predifiend date on face frontals from Open-CV =================================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                print("ham ...")
                cap = cv2.VideoCapture(0)
                print("mo camera")
                img_id = 0
                
                while True:
                    ret,img = cap.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #Scaling factor = 1.37
                    #Minimun Neighbor = 543
                   # cap = cv2.VideoCapture(0)
                    if img is not None:

                        img_id += 1
                    
                    face = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(face, (x,y), (x+w, y+h),(255, 0, 0), 2)
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,225,0),2)
                    cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets compled !")


            except BaseException as es:
                messagebox.showerror("Lỗi", f"due to:{str(es)}", parent = self.root)
                print(str(es))
#============= Search ===================
    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='250301',
                        host='localhost',
                        database='face_recognition')
                print('Connect successfully')  
                cursor = conn.cursor()
                cursor.execute("select * from student where " + str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
                rows=cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                print({str(es)})
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
    obj = Student(root)
    root.mainloop()