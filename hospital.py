from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        self.HowtoUseMedication=StringVar()
        

        label_title=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",
        bg="white",font=("times new romman",50,"bold"))
        label_title.pack(side=TOP, fill=X)


        ## ===================================== DATA FRAME ================================================\


        data_frame=Frame(self.root,bd=20,relief=RIDGE)
        data_frame.place(x=0,y=130,width=1530,height=400)


        dataframe_left = LabelFrame(data_frame,bd=10,relief=RIDGE,padx=10,
        font=("times new romman",12,"bold"),text="Patient Information")
        dataframe_left.place(x=0,y=5,width=980,height=350)
        dataframe_right = LabelFrame(data_frame,bd=10,relief=RIDGE,padx=10,
        font=("times new romman",12,"bold"),text="Prescription")
        dataframe_right.place(x=990,y=5,width=500,height=350)


        ## ===================================== Buttons FRAME ==============================================\


        button_frame=Frame(self.root,bd=20,relief=RIDGE)
        button_frame.place(x=0,y=530,width=1530,height=70)


        ## ===================================== Details FRAME ==============================================\


        details_frame=Frame(self.root,bd=20,relief=RIDGE)
        details_frame.place(x=0,y=600,width=1530,height=190)


        ## ===================================== dataframe_left ==============================================\


        labelnametab=Label(dataframe_left,text="Name of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        labelnametab.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(dataframe_left,textvariable=self.Nameoftablet,state="readonly",font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Acitaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)


        labelref=Label(dataframe_left,font=("arial",12,"bold"),text="Reference number:",padx=2)
        labelref.grid(row=1,column=0,sticky=W)
        textref=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        textref.grid(row=1,column=1)


        labelDose=Label(dataframe_left,font=("arial",12,"bold"),text="Dose",padx=2,pady=4)
        labelDose.grid(row=2,column=0,sticky=W)
        textDose=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        textDose.grid(row=2,column=1)
        

        labelNoOfTablet=Label(dataframe_left,font=("arial",12,"bold"),text="Number of Tablets:",padx=2,pady=6)
        labelNoOfTablet.grid(row=3,column=0,sticky=W)
        textNoOfTablet=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        textNoOfTablet.grid(row=3,column=1)


        labelLot=Label(dataframe_left,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        labelLot.grid(row=4,column=0,sticky=W)
        textLot=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        textLot.grid(row=4,column=1)


        labelissuedate=Label(dataframe_left,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        labelissuedate.grid(row=5,column=0,sticky=W)
        textissuedate=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.IssueDate,width=35)
        textissuedate.grid(row=5,column=1)


        labelExpDate=Label(dataframe_left,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        labelExpDate.grid(row=6,column=0,sticky=W)
        textExpDate=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        textExpDate.grid(row=6,column=1)


        labelDailyDose=Label(dataframe_left,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        labelDailyDose.grid(row=7,column=0,sticky=W)
        textDailyDose=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        textDailyDose.grid(row=7,column=1)


        labelSideEffect=Label(dataframe_left,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        labelSideEffect.grid(row=8,column=0,sticky=W)
        textSideEffect=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
        textSideEffect.grid(row=8,column=1)


        labelFurtherinfo=Label(dataframe_left,font=("arial",12,"bold"),text="Further info:",padx=2)
        labelFurtherinfo.grid(row=0,column=2,sticky=W)
        textFurtherinfo=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        textFurtherinfo.grid(row=0,column=3)


        labelBloodPressure=Label(dataframe_left,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        labelBloodPressure.grid(row=1,column=2,sticky=W)
        textBloodPressure=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        textBloodPressure.grid(row=1,column=3)


        labelStorage=Label(dataframe_left,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        labelStorage.grid(row=2,column=2,sticky=W)
        textStorage=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        textStorage.grid(row=2,column=3)


        labelMedicine=Label(dataframe_left,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        labelMedicine.grid(row=3,column=2,sticky=W)
        textMedicine=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.HowtoUseMedication,width=35)
        textMedicine.grid(row=3,column=3,sticky=W)


        labelPatientId=Label(dataframe_left,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        labelPatientId.grid(row=4,column=2,sticky=W)
        textPatientId=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        textPatientId.grid(row=4,column=3)


        labelNhsNumber=Label(dataframe_left,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        labelNhsNumber.grid(row=5,column=2,sticky=W)
        textNhsNumber=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        textNhsNumber.grid(row=5,column=3)


        labelPatientName=Label(dataframe_left,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        labelPatientName.grid(row=6,column=2,sticky=W)
        textPatientName=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        textPatientName.grid(row=6,column=3)


        labelDateofBirth=Label(dataframe_left,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        labelDateofBirth.grid(row=7,column=2,sticky=W)
        textDateofBirth=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        textDateofBirth.grid(row=7,column=3)


        labelPatientAddress=Label(dataframe_left,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        labelPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress=Entry(dataframe_left,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        textPatientAddress.grid(row=8,column=3)


        ## ===================================== dataframe_right =============================================\


        self.txtPrescription=Text(dataframe_right,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        ## ========================================== Buttons ================================================\

        
        btnPrescription=Button(button_frame,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),
        width=24,height=1,padx=2,pady=6,command=self.iPrescription)
        btnPrescription.grid(row=0,column=0)


        btnPrescriptionData=Button(button_frame,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),
        width=24,height=1,padx=2,pady=6,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)


        btnUpdate=Button(button_frame,text="Update",bg="green",fg="white",font=("arial",12,"bold"),
        width=23,height=1,padx=2,pady=6,command=self.update_data)
        btnUpdate.grid(row=0,column=2)


        btndelete=Button(button_frame,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),
        width=23,height=1,padx=2,pady=6,command=self.idelete)
        btndelete.grid(row=0,column=3)


        btnclear=Button(button_frame,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),
        width=24,height=1,padx=2,pady=6,command=self.clear)
        btnclear.grid(row=0,column=4)


        btnexit=Button(button_frame,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),
        width=24,height=1,padx=2,pady=6,command=self.iexit)
        btnexit.grid(row=0,column=5)


        ## =============================================== Table =============================================\


        ##=======================>>>>>>>> Scroll Bar
        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)


        self.hospital_table=ttk.Treeview(details_frame,column=("nameoftablet","ref","dose","nooftablets","lot",
                                                               "issuedate","expdate","dailydose","storage",
                                                               "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,
                                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftablet",text="Name Of Tablet")
        self.hospital_table.heading("ref",text="Refference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    ## ============================= Functionality Declaration =======================================\


    def iPrescriptionData(self):
        if self.Nameoftablet.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error!!"," All fields are required... ")
        else:
            conn=mysql.connector.connect(host='localhost', username='root', password='Aman@123', database='hospital')
            my_cursor=conn.cursor()
            my_cursor.execute("insert into host values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (
                              self.Nameoftablet.get(),
                              self.ref.get(),
                              self.Dose.get(),
                              self.NumberofTablets.get(),
                              self.Lot.get(),
                              self.IssueDate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.StorageAdvice.get(),
                              self.nhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOfBirth.get(),
                              self.PatientAddress.get()
                              )
                              )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success!", "Record has been inserted.")
            



    def update_data(self):
        conn=mysql.connector.connect(host='localhost', username='root', password='Aman@123', database='hospital')
        my_cursor=conn.cursor()
        my_cursor.execute("update host set Nameoftablets=%s,Dose=%s,Numberoftablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,nhsNumber=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference_no=%s",(
            self.Nameoftablet.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get(),
            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success!", "Record has been updatesd.")
        

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root', password='Aman@123', database='hospital')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from host")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablet.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.StorageAdvice.set(row[9])
        self.nhsNumber.set(row[10])
        self.PatientName.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablet.get()+"\n")
        self.txtPrescription.insert(END,"Reference Number:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"Expiry Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Inormation:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Driving using Machine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")


    def idelete(self):
        conn=mysql.connector.connect(host='localhost', username='root', password='Aman@123', database='hospital')
        my_cursor=conn.cursor()
        query="delete from host where Reference_no=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success!", "Record has been deleted.")


    def clear(self):
        self.Nameoftablet.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowtoUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)


    def iexit(self):
        iexit=messagebox.askyesno("Hospital Management System","Do you really want to exit...?")
        if iexit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()