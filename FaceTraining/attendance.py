from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import csv 
from tkinter import filedialog


myData = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x783+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)


#=======vảiable=====

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        #Bg image
        img3 = Image.open(r"assets/img/bg_img.png")
        img3 = img3.resize((1195,790),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 790)

        main_frame = ttk.Frame(bg_img)
        main_frame.place(x = 25, y = 110, width = 1145, height = 650)

        #Left frame
        Left_frame = ttk.Labelframe(main_frame, text = "Thông tin điểm danh sinh viên")
        Left_frame.place(x = 10, y = 10, width =555, height =  635)


        #Student attendance details
        img_left = Image.open(r"assets/img/studentDetails.png")
        img_left = img_left.resize((545,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = ttk.Label(Left_frame, image = self.photoimg_left, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)

        left_insider_frame = ttk.Labelframe(Left_frame, text = "Thông tin điểm danh sinh viên")
        left_insider_frame.place(x = 5, y = 135, width =543, height =  450)


        #Labeland entry
        #Student ID
        attendanceId_label = ttk.Label(left_insider_frame, text = "Mã sinh viên")
        attendanceId_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        attendanceID_entry = ttk.Entry(left_insider_frame, width = 20, textvariable = self.var_atten_id)
        attendanceID_entry.grid(row = 0, column = 1, padx=5, ipadx = 10, sticky = W)

        
        #Student name
        studentName_label = ttk.Label(left_insider_frame, text = "Họ tên")
        studentName_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        studentName_entry = ttk.Entry(left_insider_frame,  width = 20, textvariable = self.var_atten_name)
        studentName_entry.grid(row = 0, column = 3, padx=5, pady = 5, ipadx = 10, sticky = W)

        #Department
        department_label = ttk.Label(left_insider_frame, text = "Chuyên Ngành:")
        department_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

        department_entry = ttk.Entry(left_insider_frame,  width = 20, textvariable = self.var_atten_dep)
        department_entry.grid(row = 1, column = 1, padx=5, pady = 5, ipadx = 10, sticky = W)

        #Roll
        roll_label = ttk.Label(left_insider_frame, text = "Roll no:")
        roll_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

        roll_entry = ttk.Entry(left_insider_frame,  width = 20, textvariable = self.var_atten_roll)
        roll_entry.grid(row = 1, column = 3, padx=5, pady = 5, ipadx = 10, sticky = W)


        #Attendance time
        time_label = ttk.Label(left_insider_frame, text = "Giờ: ")
        time_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        time_entry = ttk.Entry(left_insider_frame, width = 20, textvariable = self.var_atten_time)
        time_entry.grid(row = 2, column = 1, padx=5, pady = 5, ipadx = 10, sticky = W)
        #Attendance date
        date_label = ttk.Label(left_insider_frame, text = "Ngày: ")
        date_label.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        date_entry = ttk.Entry(left_insider_frame, width = 20, textvariable = self.var_atten_date)
        date_entry.grid(row = 2, column = 3, padx=5, pady = 5, ipadx = 10, sticky = W)

        #Attendance status
        attendance_label = ttk.Label(left_insider_frame, text = "Trạng thái điểm danh:")
        attendance_label.grid(row = 3, column = 0, padx = 10, sticky = W)

        
        self.attendance_status = ttk.Combobox(left_insider_frame,  width =17, state = "readonly", textvariable = self.var_atten_attendance)
        self.attendance_status["values"] = ("", "Present", "Absent")
        self.attendance_status.current(0)
        self.attendance_status.grid(row = 3, column = 1, padx=5, pady=10, ipadx = 20, sticky = W)
        

#Buttom frame
        btn_frame = ttk.Frame(left_insider_frame, border= 5)
        btn_frame.place(x = 0, y = 250, width =530, height =40)

        import_btn = ttk.Button(btn_frame, text ="Nhập CSV", command = self.importCsv,  style="ToggleButton", width = 15)
        import_btn.grid(row = 0, column = 0, padx = 7)

        export_btn = ttk.Button(btn_frame, text ="Xuất CSV", command = self.exportCsv,  style="ToggleButton", width = 15)
        export_btn.grid(row = 0, column = 1, padx = 10)

        update_btn = ttk.Button(btn_frame, text ="Cập nhật", command = self.action,  style="ToggleButton", width = 15)
        update_btn.grid(row = 0, column = 2, padx = 10)

        reset_btn = ttk.Button(btn_frame, text = "Reset", command = self.reset_data,  style="ToggleButton", width = 15)
        reset_btn.grid(row = 0, column = 3, padx = 10)

        #Right frame
        Right_frame = ttk.Labelframe(main_frame, text = "TThông tin điểm danh: ")
        Right_frame.place(x = 580, y = 10, width =555, height =  635)

        #Attendance details
        img_right = Image.open(r"assets/img/attendancedetails.png")
        img_right = img_right.resize((545,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = ttk.Label(Right_frame, image = self.photoimg_right, cursor= "hand2")
        f_lbl.place(x = 3, y = 0, width = 545, height = 130)

        #============== Search System ====================
        search_frame = ttk.Labelframe(Right_frame, text = "Tìm kiếm thông tin")
        search_frame.place(x = 5, y = 135, width =543, height =  80)

        search_label = ttk.Label(search_frame, text = "Search by:", border = 3)
        search_label.grid(row = 0, column = 0, padx = 7, pady = 5, sticky = W)

        search_combo = ttk.Combobox(search_frame, width =13, state = "readonly")
        search_combo["values"] = (" ", "Roll No", "Số điện thoại", "Mã sinh viên")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx=5, pady=10, ipadx = 2, sticky = W)


        search_entry = ttk.Entry(search_frame, width = 15)
        search_entry.grid(row = 0, column = 2, padx=5,pady = 5, ipadx = 10, sticky = W)

        search_btn = ttk.Button(search_frame, text ="Tìm kiếm",style="ToggleButton", width = 10)
        search_btn.grid(row = 0, column = 3, padx = 7)

        showAll_btn = ttk.Button(search_frame, text ="Hiển thị tất cả",style="ToggleButton", width = 13)
        showAll_btn.grid(row = 0, column = 4, padx = 10)


        #====================Table Frame====================
        table_frame = ttk.Frame(Right_frame, border = 5 )
        table_frame.place(x = 5, y = 230, width =543, height =  385)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns = ("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand= scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text = "Mã Sinh viên")
        self.AttendanceReportTable.heading("roll", text = "Roll")
        self.AttendanceReportTable.heading("name", text = "Tên sinh viên")
        self.AttendanceReportTable.heading("department", text = "Ngành")
        self.AttendanceReportTable.heading("time", text = "Giờ vào lớp")
        self.AttendanceReportTable.heading("date", text = "Ngày")
        self.AttendanceReportTable.heading("attendance", text = "Trạng thái")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width = 100)
        self.AttendanceReportTable.column("roll", width = 100)
        self.AttendanceReportTable.column("name", width = 100)
        self.AttendanceReportTable.column("department", width = 100)
        self.AttendanceReportTable.column("time", width = 100)
        self.AttendanceReportTable.column("date", width = 100)
        self.AttendanceReportTable.column("attendance", width = 100)

        self.AttendanceReportTable.pack(fill = BOTH, expand = 1)


        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor )
        #===============Fetch data============
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values = i)



     #====Import CSV====   
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Mở CSV", filetypes = (("CSV File", "*.csv"), ("All Files","*.*")), parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter = ",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)   

#=====exxport csv=====
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("Error", "Không có dữ liệu nhập vào!", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Mở CSV", filetypes = (("CSV File", "*.csv"), ("All Files","*.*")), parent = self.root)
            with open(fln, mode = "w", newline =  "") as myfile:
                epx_write = csv.writer(myfile,delimiter = ",")
                for i in myData:
                    epx_write.writerow(i)
                messagebox.showinfo("Success","Dữ liệu được lưu vào : "+ os.path.basename(fln) + " thành công!")
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)
                print(str(es))


    def get_cursor(self, event = ""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    # export upadte
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                #dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
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
    obj = Attendance(root)
    root.mainloop()