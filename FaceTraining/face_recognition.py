from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("550x350+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)

#Bg image
        img3 = Image.open(r"assets/img/bg_train.png")
        img3 = img3.resize((550,550),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 550, height = 550)


#Buttom

        img_top = Image.open(r"assets/img/face_recog.png")
        img_top = img_top.resize((120,120),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = ttk.Button(self.root, image = self.photoimg_top, command = self.face_recogn,  style="ToggleButton", cursor= "hand2")
        f_lbl.place(x = 5, y = 130, width = 540, height = 130)



#============= Attendance==========================
    def mark_attendance(self, i, r, n, d):
        with open("DiemDanh.csv", "r+", newline = "\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((", "))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

#============ Face Recognition ----------------

    def face_recogn(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='250301',
                              host='localhost',
                              database='face_recognition') 
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_id = " + str(id))
                n = cursor.fetchone()
                n = "+".join(n)


                cursor.execute("select Roll from student where Student_id = " + str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute("select Dep from student where Student_id = " + str(id))
                d = cursor.fetchone()
                d = "+".join(d) 

                cursor.execute("select Student_id from student where Student_id = " + str(id))
                i = cursor.fetchone()
                i = "+".join(i) 

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Namel:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, f"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                coord = [x, y, w, h]
                print("debug")
            return coord
        def recongize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,10,(255,255,255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recongize(img, clf, faceCascade)
            cv2.imshow("Wellcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



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
    obj = Face_Recognition(root)
    root.mainloop()