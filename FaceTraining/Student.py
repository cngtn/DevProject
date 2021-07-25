from tkinter import * 
from tkinter import font
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x765+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)

        #Bg image
        img3 = Image.open(r"assets/img/bg_img.png")
        img3 = img3.resize((1195,765),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 765)

        main_frame = ttk.Frame(bg_img)
        main_frame.place(x = 25, y = 110, width = 1145, height = 635)

        #Left frame
        Left_frame = ttk.Labelframe(main_frame, text = "Student Details")
        Left_frame.place(x = 10, y = 10, width =555, height =  615)


        #Student details
        img_left = Image.open(r"assets/img/studentDetails.png")
        img_left = img_left.resize((545,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = ttk.Label(Left_frame, image = self.photoimg_left, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)

        # Current course information
        current_course_frame = ttk.Labelframe(Left_frame, text = "Current Course information")
        current_course_frame.place(x = 5, y = 135, width =543, height =  120)
        
        
        #Dapartment
        dep_label = ttk.Label(current_course_frame, text = "Department")
        dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        
        dep_combo = ttk.Combobox(current_course_frame, width =17, state = "readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx=5, pady=10, ipadx = 10, sticky = W)

        #Course
        course_label = ttk.Label(current_course_frame, text = "Course")
        course_label.grid(row = 0, column = 2, padx = 10, sticky = W)

        
        course_combo = ttk.Combobox(current_course_frame, width =17, state = "readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row = 0, column = 3, padx=5, pady=10, ipadx = 10, sticky = W)


        #year
        year_label = ttk.Label(current_course_frame, text = "Year")
        year_label.grid(row = 1, column = 0, padx = 10, sticky = W)

        
        year_combo = ttk.Combobox(current_course_frame, width =17, state = "readonly")
        year_combo["values"] = ("Select Year", "2021 - 2022", "2022 - 2023", "2023 - 2024", "2024 - 2025")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx=2, pady=10, ipadx = 10, sticky = W)


        #Semester
        semester_label = ttk.Label(current_course_frame, text = "Semester")
        semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)

        
        semester_combo = ttk.Combobox(current_course_frame, width =17, state = "readonly")
        semester_combo["values"] = ("Select Course", "Semester - 1", "Semester - 2", "Semester - 3", "Semester - 4")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx=5, pady=10, ipadx = 10, sticky = W)


        # Class student information
        class_student_frame = ttk.Labelframe(Left_frame, text = "Class student information")
        class_student_frame.place(x = 5, y = 260, width =543, height =  335)

        #Student ID
        studentId_label = ttk.Label(class_student_frame, text = "Student ID")
        studentId_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        studentID_entry = ttk.Entry(class_student_frame, width = 20)
        studentID_entry.grid(row = 0, column = 1, padx=5, ipadx = 10, sticky = W)


        #Student name
        studentName_label = ttk.Label(class_student_frame, text = "Student Name")
        studentName_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        studentName_entry = ttk.Entry(class_student_frame, width = 20)
        studentName_entry.grid(row = 0, column = 3, padx=5, pady = 5, ipadx = 10, sticky = W)


        # Class didvision
        class_div_label = ttk.Label(class_student_frame, text = "Class Didvision")
        class_div_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

        class_div_entry = ttk.Entry(class_student_frame, width = 20)
        class_div_entry.grid(row = 1, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Roll No
        roll_no_label = ttk.Label(class_student_frame, text = "Roll No")
        roll_no_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

        roll_no_entry = ttk.Entry(class_student_frame, width = 20)
        roll_no_entry.grid(row = 1, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Gender
        gender_label = ttk.Label(class_student_frame, text = "Gender: ")
        gender_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        gender_entry = ttk.Entry(class_student_frame, width = 20)
        gender_entry.grid(row = 2, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)

        # Roll No
        dob_label = ttk.Label(class_student_frame, text = "DOB:")
        dob_label.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        dob_entry = ttk.Entry(class_student_frame, width = 20)
        dob_entry.grid(row = 2, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Email
        email_label = ttk.Label(class_student_frame, text = "Email")
        email_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        email_entry = ttk.Entry(class_student_frame, width = 20)
        email_entry.grid(row = 3, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)


        # Phone
        phone_no_label = ttk.Label(class_student_frame, text = "Number phone")
        phone_no_label.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)

        phone_no_entry = ttk.Entry(class_student_frame, width = 20)
        phone_no_entry.grid(row = 3, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)

        # Address
        address_label = ttk.Label(class_student_frame, text = "Address")
        address_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)

        address_entry = ttk.Entry(class_student_frame, width = 20)
        address_entry.grid(row = 4, column = 1, padx=5,pady = 5, ipadx = 10, sticky = W)
    

        # Teacher name
        teacher_name_label = ttk.Label(class_student_frame, text = "Teacher name")
        teacher_name_label.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)

        teacher_name_entry = ttk.Entry(class_student_frame, width = 20)
        teacher_name_entry.grid(row = 4, column = 3, padx=5,pady = 5, ipadx = 10, sticky = W)


        #Radio Buttom
        radionbtn1 = ttk.Radiobutton(class_student_frame, text = "Take photo Sample", value = "yes")
        radionbtn1.grid(row = 6, column =1, sticky = W)
        radionbtn2 = ttk.Radiobutton(class_student_frame, text = "No photo Sample", value = "no")
        radionbtn2.grid(row = 6, column =3, sticky = W)

        #Buttom frame
        btn_frame = ttk.Frame(class_student_frame, border= 5)
        btn_frame.place(x = 0, y = 230, width =530, height =40)

        save_btn = ttk.Button(btn_frame, text ="Save",style="ToggleButton", width = 15)
        save_btn.grid(row = 0, column = 0, padx = 7)

        update_btn = ttk.Button(btn_frame, text ="Update",style="ToggleButton", width = 15)
        update_btn.grid(row = 0, column = 1, padx = 10)


        delete_btn = ttk.Button(btn_frame, text ="Delete",style="ToggleButton", width = 15)
        delete_btn.grid(row = 0, column = 2, padx = 10)

        reset_btn = ttk.Button(btn_frame, text ="Reset",style="ToggleButton", width = 15)
        reset_btn.grid(row = 0, column = 3, padx = 10)

        
        btn_frame1 = ttk.Frame(class_student_frame, border= 5)
        btn_frame1.place(x = 0, y = 275, width =530, height =40)
        
        take_photo_btn = ttk.Button(btn_frame1, text ="Take photo",style="ToggleButton", width = 37)
        take_photo_btn.grid(row = 0, column = 0, padx = 7)

        take_photo_btn = ttk.Button(btn_frame1, text ="Upload photo",style="ToggleButton", width = 37)
        take_photo_btn.grid(row = 0, column = 1, padx = 10)
















        #Right frame
        Right_frame = ttk.Labelframe(main_frame, text = "Student Details")
        Right_frame.place(x = 580, y = 10, width =555, height =  615)

        #Student details
        img_right = Image.open(r"assets/img/Search.png")
        img_right = img_right.resize((545,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = ttk.Label(Right_frame, image = self.photoimg_right, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)


        #============== Search System ====================
        search_frame = ttk.Labelframe(Right_frame, text = "Search information")
        search_frame.place(x = 5, y = 135, width =543, height =  80)

        search_label = ttk.Label(search_frame, text = "Search by:", border = 3)
        search_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

        search_combo = ttk.Combobox(search_frame, width =15, state = "readonly")
        search_combo["values"] = ("Select ", "Roll No", "Number Phone", "Student ID")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx=5, pady=10, ipadx = 10, sticky = W)


        search_btn = ttk.Button(search_frame, text ="Search",style="ToggleButton", width = 10)
        search_btn.grid(row = 0, column = 2, padx = 10)

        showAll_btn = ttk.Button(search_frame, text ="Show all",style="ToggleButton", width = 10)
        showAll_btn.grid(row = 0, column = 3, padx = 10)











if __name__ == "__main__":
        obj = Student(root)
        root.mainloop()