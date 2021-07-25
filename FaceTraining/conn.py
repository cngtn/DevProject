#importing module  
import pyodbc  
#creating connection Object which will contain SQL Server Connection  
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=MSI\SQLEXPRESS;database=face_recognition;uid=sa;pwd=250301')  
  
print("Connection Successfully Established")  
  
#closing connection  
conn.close()  