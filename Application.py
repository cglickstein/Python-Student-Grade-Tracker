# Assignment 10 
# Purpose: student grade tracker incorporating everything we have learned including OOP and GUI. 
# Application module to run everything else (main part of program)
# Developer: Chava Glickstein
# Date: 1/1/2023

from tkinter import *
from Roster import Roster

#class: Application
#Purpose: Application object which is a Frame we add things to 
class Application(Frame):
    #master is the root
    def __init__(self,master):
        #calling the constructor for the parent
        super(Application,self).__init__(master)
        self.grid()
        self.configure(bg="white")
        self.menuWidgets()


    #Function: menuWidgets
    #Purpose:  creates all of the widgets on the main window which have buttons that on command, link to all of the other functions in the other modules
    #Parameters: self
    #Return value: none
    def menuWidgets(self):

        self.lblIntro=Label(self, text="Welcome to the WITS student grade tracker! \nPress a button below to continue.",font=('Helvetica bold', 16),bg="white")
        self.lblIntro.grid(row=0,column=0, sticky=N, pady=8)
        
        self.btn1 = Button(self,text="ADD STUDENT", command=Roster.addStudent, width=40, height=3, bg="#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=2,column=0, padx=50, pady=8)

        self.btn1 = Button(self,text="ADD STUDENT COURSE AND COURSE GRADE", command=Roster.addGrade, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=4,column=0, padx=100,pady=8, sticky='w')
       
        self.btn1 = Button(self,text="DISPLAY ALL STUDENT RECORDS", command=Roster.displayStudentRecords, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=6,column=0,padx=100, pady=8,sticky=W)

        self.btn1 = Button(self,text="OBTAIN STUDENT GRADE", command=Roster.getGrade, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=8,column=0, padx=100,pady=8, sticky=W)

        self.btn1 = Button(self,text="LOAD IN TEXT FILE OF STUDENTS", command=Roster.loadFromFile, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=2,column=1, padx=0, pady=8,sticky=W)

        self.btn1 = Button(self,text="GENERATE REPORT CARD FOR STUDENT", command=Roster.generateReportcard, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=4,column=1, padx=0, pady=8,sticky=W)

        self.btn1 = Button(self,text="GENERATE TRANSCRIPT FOR STUDENT", command=Roster.generateTran, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=6,column=1, padx=0, pady=8,sticky=W)

        self.btn1 = Button(self,text="ADD COMMENT TO STUDENT COURSE", command=Roster.addComments, width=40, height=3, bg=	"#00008B", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=8,column=1, padx=0, pady=8,sticky=W)

        self.btn1 = Button(self,text="EXIT AND SAVE ALL CHANGES", command=lambda:Roster.saveToBinary(root), height=3, width=40, bg=	"orange", fg="white",font=('Helvetica bold', 11))
        self.btn1.grid(row=10,column=1, sticky=W)


    #not using:
    # def clearWidgets():
    #         for widgets in root.winfo_children():
    #             widgets.destroy()




root = Tk() 
root.title("WITS STUDENT GRADE TRACKER")

#sizing
root.geometry("1000x750")
root.configure(bg="white")

#imports the wits logo to use on the screen.
#  Logo should be in the same folder as the program and have the name witsLogo.png. If not working, comment this part out.
logo = PhotoImage(file = "witsLogo.png")
logoLabel = Label(root, image = logo)
PhotoImage(file = "witsLogo.png")
logoLabel.grid(row=0, column=0, rowspan=1, columnspan=1, padx=230, sticky=NW)

#creating our application and sending it the root created
app=Application(root)

#load everything from before before we run the main program
Roster.loadBinary()

root.mainloop()

#user should press exit and save button to save everythings
# Roster.saveToBinary()