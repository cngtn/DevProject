from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import numpy as np


class Train:
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

        img_top = Image.open(r"assets/img/TrainingFace.png")
        img_top = img_top.resize((510,100),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = ttk.Button(self.root, image = self.photoimg_top, command = self.train_classifier ,  style="ToggleButton", cursor= "hand2")
        f_lbl.place(x = 5, y = 130, width = 540, height = 130)
    

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)


#=============== Train the classifier and save ==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets completed!")


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
    obj = Train(root)
    root.mainloop()