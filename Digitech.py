from tkinter import *
from tkinter import messagebox
import os




def MainMenu():

        
    MainMenuWin=Tk()
    MainMenuWin.title("Main Menu")
    MainMenuWin.geometry("200x200")
    
    frame1=Frame(MainMenuWin)
    frame1.pack()
                           
    btn1=Button(frame1,text="Add Jobs",command=AddJob)
    btn2=Button(frame1,text="Payroll",command= Payroll)
    
    frame2=Frame(MainMenuWin)
    frame2.pack()

    btn3=Button(frame2,text="Add User",command=AddUser)
    
    frame3=Frame(MainMenuWin)
    frame3.pack()

    btn4=Button(frame3,text="Logout",command=LoginScreen)
    btn5=Button(frame3,text="Exit",command=MainMenuWin.destroy)
            
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)
            
def Payroll():
    
    os.system('python Payroll.py')
    
def AddJob():

    def SaveJob() :

        JobIDSave = JobIDVar.get()
        JobIDSave = JobIDSave.ljust(50)
    
        ItemnameSave = ItemnameVar.get()
        ItemnameSave = ItemnameSave.ljust(50)
    
        ManufacturerSave = ManufacturerVar.get()
        ManufacturerSave = ManufacturerSave.ljust(50)
    
        DescriptionSave = DescriptionVar.get()
        DescriptionSave = DescriptionSave.ljust(50)
    
        CustomerIDSave = CustomerIDVar.get()
        CustomerIDSave = CustomerIDSave.ljust(50)

      
    
        fileObject = open("JobDetails.txt","a")
        
        fileObject.write(JobIDSave + ItemnameSave + ManufacturerSave + DescriptionSave + CustomerIDSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Job details successfully saved")
    
    AddJobWin=Tk()
    AddJobWin.title("Add Job")
    AddJobWin.geometry("300x300")
    
    frame1=Frame(AddJobWin)
    frame1.pack()

       
    Label(frame1, text="JobID").grid(row=3, column=0, sticky=W)
    JobIDVar=StringVar()
    JobIDVar= Entry(frame1, textvariable=JobIDVar)
    JobIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Itemname").grid(row=4, column=0, sticky=W)
    ItemnameVar=StringVar()
    ItemnameVar= Entry(frame1, textvariable=ItemnameVar)
    ItemnameVar.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Manufacturer").grid(row=5, column=0, sticky=W)
    ManufacturerVar=StringVar()
    ManufacturerVar= Entry(frame1, textvariable=ManufacturerVar)
    ManufacturerVar.grid(row=5,column=1,sticky=W)
    
    Label(frame1, text="Description").grid(row=6, column=0, sticky=W)
    DescriptionVar=StringVar()
    DescriptionVar= Entry(frame1, textvariable=DescriptionVar)
    DescriptionVar.grid(row=6,column=1,sticky=W)
    
    Label(frame1, text="CustomerID").grid(row=7, column=0, sticky=W)
    CustomerIDVar=StringVar()
    CustomerIDVar= Entry(frame1, textvariable=CustomerIDVar)
    CustomerIDVar.grid(row=7,column=1,sticky=W)

  

    frame2 = Frame(AddJobWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddJobWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveJob)
    b1.pack(side=LEFT); b2.pack(side=LEFT)



    
    

    
def AddUser():
    
    def SaveUser() :

        UserIDSave = UserIDVar.get()
        UserIDSave = UserIDSave.strip()
    
        PasswordSave = PasswordVar.get()
        PasswordSave = PasswordSave.strip()
    
       
        fileObject = open("data.dat","a")
        
        fileObject.write(UserIDSave + " " + PasswordSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Password successfully saved")
    
    AddUserWin=Tk()
    AddUserWin.title("Add User")
    AddUserWin.geometry("300x300")
    
    frame1=Frame(AddUserWin)
    frame1.pack()

       
    Label(frame1, text="UserID").grid(row=3, column=0, sticky=W)
    UserIDVar=StringVar()
    UserIDVar= Entry(frame1, textvariable=UserIDVar)
    UserIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Password").grid(row=4, column=0, sticky=W)
    PasswordVar=StringVar()
    PasswordVar= Entry(frame1, textvariable=PasswordVar)
    PasswordVar.grid(row=4,column=1,sticky=W)
    
     

    frame2 = Frame(AddUserWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddUserWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveUser)
    b1.pack(side=LEFT); b2.pack(side=LEFT)

    
    
def LoginScreen():
    
    def login():
        username=usname.get()
        passwd=password.get()
        flag=TRUE

        if username.strip() == "" and passwd.strip() == "":
            messagebox.showinfo("Error","Blank username and password")
        elif passwd.strip() == "":
            messagebox.showinfo("Error","Blank password")
        elif username.strip()== "":
            messagebox.showinfo("Error","Blank username")
        else:
            
            passwordfile = open("data.dat","r")
            passvar = passwordfile.readline()
                            
            while flag and passvar !="":
                                      
                if passvar.find(username.strip()) >=0 and passvar.find(passwd.strip())>=0:
                    messagebox.showinfo("Authenticated","Correct username and password")
                    flag = FALSE
                                    
                passvar = passwordfile.readline()
                                
                passwordfile.close()
                if flag:
                 messagebox.showinfo("Error","Incorrect username and / or password")
                else:
                    loginwindow.destroy()
                    MainMenu()
                                

        
    loginwindow=Tk()
    loginwindow.title("DigiTech Log In Screen")
    loginwindow.geometry("200x200")
    lbluname=Label(loginwindow, text="Username")
    usname=Entry(loginwindow)
    lblpass=Label(loginwindow, text="Password")
    password=Entry(loginwindow)

    lbluname.pack()
    usname.pack()
    lblpass.pack()
    password.pack()

    btn=Button(loginwindow,text="Log In",command=login).pack()


LoginScreen()     

