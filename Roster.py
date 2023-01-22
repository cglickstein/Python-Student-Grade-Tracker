# Assignment 10 
# Purpose: student grade tracker incorporating everything we have learned including OOP and GUI. 
# Roster module portion
# Developer: Chava Glickstein
# Date: 1/1/2023

import Student
import pathlib
import os
import pickle
import os.path
from tkinter import *
from tkinter import messagebox
# from tkinter import ttk
# from tkinter import simpledialog 

#class: Roster
#Purpose: Roster object
class Roster (object):
    #class variable that holds student objects with course list of course objects
    studentObjects=[] 

    #Function: addStudentTask
    #Purpose:  assists addStudent function in adding new student when submit button is pressed (using student sent from addStudent)
    #Parameters: studentName, rootAddStudent,lblStudent, entryStudent, btnSubmit,endButton) 
    #Return value: none
    def addStudentTask(studentName, rootAddStudent,lblStudent, entryStudent, btnSubmit,endButton):
            #Can be configured to display success message at bottom of page
            lblResult=Label(rootAddStudent,text="" )
            lblResult.grid(row=4,column=0,sticky='w')  

           #checks to see if attribute studentName of any of the items in the studentObjects list is equal to studentName. 
           # If it is (the student is already in the list), inList boolean is set to True.
            inList=any(obj.studentName == studentName for obj in Roster.studentObjects)
            if inList:
                messagebox.showinfo("Error","Student is already in the system", parent=rootAddStudent)
            else: 
                if studentName==" " or "":
                    messagebox.showinfo("Error","Invalid student name", parent=rootAddStudent)
                #if there are no errors when submit button is clicked, it adds student and displays message of success
                else:
                    studentCourseList=[]
                    #we send NewStudent (instance of our Student class) a name and an empty list to be filled with courses
                    newStudent=Student.NewStudent(studentName,studentCourseList)
                    #we add that student to our studentObjects list in Roster
                    Roster.studentObjects.append(newStudent)

                    lblResult.config(text=studentName+" was added successfully.",font=('Helvetica bold', 14))


    #Function: addStudent
    #Purpose: sets up environment and widgets to add a Student object to our list of studentObjects (we will add attributes later)
    #Parameters: none
    #Return value: none
    def addStudent():
            #makes an new window on top of our main window to take care of adding a student
            rootAddStudent = Tk()
            rootAddStudent.title("ADD STUDENT")
            rootAddStudent.geometry("1000x750") 
            frameAddStudent = Frame(rootAddStudent)
            frameAddStudent.grid()
     
            lblStudent=Label(rootAddStudent,text="Please enter the first and last name of the student you would like to add: ",font=('Helvetica bold', 14))
            lblStudent.grid(row=1,column=0,sticky='w')
        
            entryStudent=Entry(rootAddStudent, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=2,column=0,sticky='w', pady=10)
            
            # something I was trying to do: rootAddStudent.bind('<Return>', Roster.addStudentTask(entryStudent.get().title(),rootAddStudent,lbl,entryStudent,btnSubmit))
            
            #allows user to go back to main menu by destroying the current root at any time
            endButton=Button(rootAddStudent, text="EXIT AND GO BACK TO MENU", command=rootAddStudent.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=10, column=0)

            #allows user to submit everything they entered into text box. addStudenTask method evoked which uses information sent to it from entry boxes to make sure info is accurate and add student
            btnSubmit = Button(rootAddStudent,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.addStudentTask(entryStudent.get().title(),rootAddStudent,lblStudent,entryStudent,btnSubmit, endButton))
            btnSubmit.grid(row=5,column=0, sticky=W, pady=10, padx=25)

            rootAddStudent.mainloop()

    #Function: addGradeTask
    #Purpose:  assists addGrade function in adding new Course objects with attributes to a specific Student object (using info sent from addGrade method)
    #Parameters: studentChosen, courseName, grade, rootAddGrade,lblStudent, lblCourse, entryStudent, entryCourse, lblSemester,semester,credHrs,btnSubmit, endButton
    #Return value: none
    def addGradeTask(studentChosen, courseName, grade, rootAddGrade,lblStudent, lblCourse, entryStudent, entryCourse, lblSemester,semester,credHrs,btnSubmit, endButton):
            lblResult=Label(rootAddGrade,text="",font=('Helvetica bold', 14) )
            lblResult.grid(row=11,column=0,sticky='w',pady=5) 

            #changes user entry of one letter semester to be a full semester name
            semester=Roster.writeOutSemester(semester)
            
            #checks to see if any objects in studentObjects list have what the user entered as name to make sure grade is being added to existing student
            inList=any(obj.studentName == studentChosen for obj in Roster.studentObjects)
            if not inList:
                    messagebox.showinfo("Error","Student not in the system. ", parent=rootAddGrade)
            #once student is found, it checks that a valid semester was entered
            else:
                if semester !="Fall" and semester!="Spring" and semester!= "Summer":
                    messagebox.showinfo("Error","Invalid semester entry. ", parent=rootAddGrade)
                #once valid semester was entered checks to make sure there were no common errors for credit hour submission
                else: 
                    if credHrs=="" or credHrs==" " or credHrs.isalpha():
                        messagebox.showinfo("Error","Invalid credit hour entry. Enter 3 for default", parent=rootAddGrade)
                    #if there were no problems, call Student's addCourse method on specific Student object to add a Course object with proper attributs to Student's Course list
                    else: 
                        for student in Roster.studentObjects:
                            if student.studentName==studentChosen:
                                student.addCourse(rootAddGrade, courseName, grade,credHrs,lblResult, semester, btnSubmit )

    #Function: addGrade
    #Purpose: sets up environment and widgets to add new Course objects with attributes such as grade, semester, and course hours to Student objects
    #Parameters: none
    #Return value: none
    def addGrade():
            rootAddGrade = Tk() 
            rootAddGrade.title("ADD GRADE")
            rootAddGrade.geometry("1000x750") # dont use spaces and dont use an uppercase x
            frameAddGrade = Frame(rootAddGrade)
            frameAddGrade.grid()
           
            lblStudent=Label(rootAddGrade,text="Please enter the name of the student you would like to add a course for: ",font=('Helvetica bold', 14))
            lblStudent.grid(row=1,column=0,sticky='w')

            lblCourse=Label(rootAddGrade,text="Please enter the course you would like to add: ",font=('Helvetica bold', 14))
            lblCourse.grid(row=3,column=0,sticky='w')
        
            entryStudent=Entry(rootAddGrade, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=2,column=0,sticky='w')

            entryCourse=Entry(rootAddGrade, width=50,font=('Helvetica bold', 14))
            entryCourse.grid(row=4,column=0,sticky='w')

            lblGrade=Label(rootAddGrade,text="Please enter the grade for that course: ",font=('Helvetica bold', 14))
            lblGrade.grid(row=5,column=0,sticky='w')
        
            entryGrade=Entry(rootAddGrade, width=50,font=('Helvetica bold', 14))
            entryGrade.grid(row=6,column=0,sticky='w')

            lblSemester=Label(rootAddGrade,text="Please enter semester (f for fall, s for spring, su for summer): ",font=('Helvetica bold', 14))
            lblSemester.grid(row=7,column=0,sticky='w')
        
            entrySemester=Entry(rootAddGrade, width=50)
            entrySemester.grid(row=8,column=0,sticky='w')

            lblCredHrs=Label(rootAddGrade,text="Please enter how many credits this class is worth (if applicable)",font=('Helvetica bold', 14))
            lblCredHrs.grid(row=9,column=0,sticky='w')
        
            entryCredHrs=Entry(rootAddGrade, width=50,font=('Helvetica bold', 14))
            entryCredHrs.grid(row=10,column=0,sticky='w')

            endButton=Button(rootAddGrade, text="EXIT AND GO BACK TO MENU", command=rootAddGrade.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=13, column=0, pady=20)
            
            btnSubmit = Button(rootAddGrade,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.addGradeTask(entryStudent.get().title(),entryCourse.get().upper(),entryGrade.get().upper(),rootAddGrade,lblStudent, lblCourse,entryStudent, entryCourse, lblSemester, entrySemester.get().upper(),entryCredHrs.get(),btnSubmit, endButton))
            btnSubmit.grid(row=12,column=0, pady=20,padx=40,sticky=W)

            rootAddGrade.mainloop()
            
            
    #Function: displayStudentRecords
    #Purpose: goes through Course objects in Student Objects and prints out student name, course, and grade in a list box in first name sorted order
    #Parameters: none
    #Return value: none
    def displayStudentRecords():
        rootDisplayStudents = Tk() 
        rootDisplayStudents.title("DISPLAY STUDENTS")
        rootDisplayStudents.geometry("1000x750") 
       
        frameDisplayStudents = Frame(rootDisplayStudents)
        frameDisplayStudents.grid()

        lblTitle=Label(rootDisplayStudents,text="WITS Students (scroll if necessary): ",font=('Helvetica bold', 15))
        lblTitle.grid(row=1,column=0,sticky='w')

        listBoxStudents = Listbox(rootDisplayStudents, height = 20,width = 30,bg = "#00008B",activestyle = 'dotbox',font = "Helvetica",fg = "white")
        listBoxStudents.grid(row=3, column=2, padx=250, pady=70)

        endButton=Button(rootDisplayStudents, text="EXIT AND GO BACK TO MENU", command=rootDisplayStudents.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
        endButton.grid(row=4, column=2, sticky=NW)

        #scroll bar that wasn't working
        # scrollbar = Scrollbar(rootDisplayStudents, orient=VERTICAL)
        # scrollbar.config(command=listBoxStudents.yview)
        # listBoxStudents.config(yscrollcommand=scrollbar.set)
        # scrollbar.grid(side=RIGHT, fill=Y)

        # sorts studentObjects in order of first name alphabetical order 
        #(I chose to sort by first name because I wanted user to have option of just entering first names and would get too complicated if I had both- maybe I should change)
        Roster.studentObjects.sort(key=lambda x: x.studentName) 
        
        #For every Student object in studentObject list, print student in listbox then go through that Student's Course objects 
        # and print Course attributes such as course name, grade, and semester to list box
        #Count is increased every time I want to insert something into the next spot of the list box
        count=1
        for student in Roster.studentObjects:
            listBoxStudents.insert(count,"--------------")
            count+=1
            listBoxStudents.insert(count,student.studentName+":")
            count+=1
            print("\n"+student.studentName+":")
            for course in student.courseList:
                listBoxStudents.insert(count,course.courseName+": "+str(course.courseGrade)+" ("+course.semester+" semester)")
                count+=1
   
    #Function: getGradeTask
    #Purpose: assists getGrade method in using the information sent from getGrade to make sure information is accurate and display student grade
    #Parameters: studentName,courseName,rootGetGrade,lbl, lbl2,entryStudent, entrySem, sem, entryCourse,btnSubmit, endButton)
    #Return value: none
    def getGradeTask(studentName,courseName,rootGetGrade,lblStudent, lblCourse,entryStudent, entrySem, sem, entryCourse,btnSubmit, endButton):
            lblResult=Label(rootGetGrade,text="" )
            lblResult.grid(row=7,column=0,sticky='w') 

            #changes user entry of one letter semester to be a full semester name
            sem=Roster.writeOutSemester(sem)

            #checks to see if student entered is in studentObjects list
            inList=any(obj.studentName == studentName for obj in Roster.studentObjects)
            if not inList:
                messagebox.showinfo("Sorry that student is not in the system. ",parent=rootGetGrade)
            else:
                flag=False
                for student in Roster.studentObjects:
                    #only look at the courses for the right student user entered
                    if student.studentName==studentName:
                        for course in student.courseList:
                            #finds the right course with same name and semester. Otherwise, Error messagebox is displayed
                            if course.courseName==courseName and student.studentName==studentName and course.semester==sem:
                                grade=course.courseGrade
                                lblResult.config(text="\n"+studentName+'\''+ "s grade in "+courseName+" is a(n) "+grade+".",font=('Helvetica bold', 20)) 
                                flag=True
                if flag==False:
                    messagebox.showinfo("That course cannot be found that semester for "+studentName+".", parent=rootGetGrade)


    #Function: getGrade
    #Purpose: sets up environment and widgets to obtain information needed to display a studet's grade in a particular course 
    #Parameters: none
    #Return value: none
    def getGrade():
            rootGetGrade = Tk() 
            rootGetGrade.title("OBTAIN GRADE")
            rootGetGrade.geometry("1000x750") 
            frameAddGrade = Frame(rootGetGrade)
            frameAddGrade.grid()
  
            lblStudent=Label(rootGetGrade,text="Please enter the name of the student whose grade you would like to lookup: ",font=('Helvetica bold', 14))
            lblStudent.grid(row=1,column=0,sticky='w')

            entryStudent=Entry(rootGetGrade, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=2,column=0,sticky='w')

            lblCourse=Label(rootGetGrade,text="Please enter the course you would like to see a grade for: ",font=('Helvetica bold', 14))
            lblCourse.grid(row=3,column=0,sticky='w')

            entryCourse=Entry(rootGetGrade, width=50,font=('Helvetica bold', 14))
            entryCourse.grid(row=4,column=0,sticky='w')
    
            lblSem=Label(rootGetGrade,text="Please enter which semester the course is under (f for fall, su for summer, s for spring): ",font=('Helvetica bold', 14))
            lblSem.grid(row=5,column=0,sticky='w')
        
            entrySem=Entry(rootGetGrade, width=50,font=('Helvetica bold', 14))
            entrySem.grid(row=6,column=0,sticky='w')

            endButton=Button(rootGetGrade, text="EXIT AND GO BACK TO MENU",bg="#00008B", fg="white",font=('Helvetica bold', 18), command=rootGetGrade.destroy)
            endButton.grid(row=9, column=0, pady=20)

            btnSubmit = Button(rootGetGrade,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.getGradeTask(entryStudent.get().title(),entryCourse.get().upper(),rootGetGrade,lblStudent, lblCourse,entryStudent, entrySem, entrySem.get().upper(), entryCourse,btnSubmit,endButton))
            btnSubmit.grid(row=8,column=0, sticky=W, pady=20, padx=40)

            rootGetGrade.mainloop()

    #Function: loadFromFileTask
    #Purpose: uses information sent from loadFromFile method such as file path to read in every line (every student) of text file
    #  and create new Student object to add to list if student doesn't already exist
    #Parameters: fileName ,rootLoadFromFile,lblInstructions, lblFile,btnSubmit, endButton
    #Return value: none
    def loadFromFileTask(fileName ,rootLoadFromFile,lblInstructions, lblFile,btnSubmit, endButton):
        lblResult=Label(rootLoadFromFile,text="" )
        lblResult.grid(row=5,column=0,sticky='w')

        if os.path.exists(fileName):  
                studentNameFile=open(fileName,"r")
                lines=studentNameFile.readlines() #reads row by row and puts it into a list
                for line in lines: 
                    flag=True
                    #gets rid of the enter after each student in the list (if there's an enter)
                    # NOT USING line=line.split("\n").title()
                    if line[-1]=="\n":
                        line=line[:-1].title()
                    #if student already in student list, set flag to false
                    for student in Roster.studentObjects:
                        if line.title()==student.studentName:
                            flag=False
                    if flag==False:
                        messagebox.showinfo(line+" is already in the system", parent=rootLoadFromFile)
                    else:
                        #create a NewStudent with the name being line (the student name from the next file) and sending in an empty list for courses
                        newStudent=Student.NewStudent(line,[])
                        #add our NewStudent to list of Student objects
                        Roster.studentObjects.append(newStudent)
                        lblResult.config(text="File successfully imported",font=('Helvetica bold', 14))
                studentNameFile.close()
        else:
            messagebox.showinfo("File not found. Try again or move file", parent=rootLoadFromFile)


    #Function: loadFromFile
    #Purpose: Set up environment and widgets to allow user to enter text file to import list of students from text file into the program
    #Parameters: none
    #Return value: none
    def loadFromFile():
            rootLoadFromFile = Tk() 
            rootLoadFromFile.title("LOAD FROM FILE")
            rootLoadFromFile.geometry("1000x750") 
            frameLoadFromFile = Frame(rootLoadFromFile)
            frameLoadFromFile.grid()

            lblInstructions=Label(rootLoadFromFile,text="Text file of student names should have one student per line.",font=('Helvetica bold', 14))
            lblInstructions.grid(row=1,column=0,sticky='w')

            lblFile=Label(rootLoadFromFile,text="Enter the file path of the text file you would like to import (without quotes):  ",font=('Helvetica bold', 14))
            lblFile.grid(row=2,column=0,sticky='w')

            entryFile=Entry(rootLoadFromFile, width=50,font=('Helvetica bold', 14))
            entryFile.grid(row=3,column=0,sticky='w')

            endButton=Button(rootLoadFromFile, text="EXIT AND GO BACK TO MENU", command=rootLoadFromFile.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=7, column=0)

            
            btnSubmit = Button(rootLoadFromFile,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.loadFromFileTask(entryFile.get() ,rootLoadFromFile,lblInstructions, lblFile,btnSubmit,endButton))
            btnSubmit.grid(row=6,column=0, padx=40, pady=20, sticky=W)

    #Function: generateReportcardTask
    #Purpose: uses info sent from generateReportcard method to generate report card text file based on 
    # student name and semester that shows grades, GPA, and comments
    #Parameters: rootRC,studentName,semester,lbl, lbl2,btnSubmit, endButton
    #Return value: none
    def genReportcardTask(rootRC,studentName,semester,lbl, lbl2,btnSubmit, endButton):
        
        semester=Roster.writeOutSemester(semester)

        #creates text file in same folder as program with name of student without spaces (.replace is to replace spaces) followed by the semester name
        fileName=(studentName.replace(" ","")+semester+".txt")


        #GPA for semester calculated by multiplying grade point (4.0 for A, 3.0 for B etc) by credits for that course, adding all of that up, and diving by total credits
        semesterGPA=0
        gradePoints=0
        totalCredHrs=0
        flag= False
        flag2=False
        #while I go through and print student courses and grades for that semester, I calculate GPA for that course using Course object attributes if there are courses and semester matches up
        for student in Roster.studentObjects:
            if student.studentName==studentName:
                flag= True
                #recreates file every time run (in case there are changes made before run again)
                RCFile=open(fileName,"w")    
                #heading to report crad 
                #if student exists and no courses, still creates blank report card
                RCFile.write("~~~~~"+studentName+" "+semester+" Report Card~~~~~")
                RCFile.write("\nStudent ID: "+student.studentID)
                #if student has one or more courses
                if len(student.courseList)>0:
                    for course in student.courseList:
                        #for every course in that semester indented code will run
                            if course.semester==semester:
                                #if flag is true will later calculate overall gpa
                                flag2=True
                                #keep adding gpa * credit hours for that course to total grade points for semester
                                gradePoints+=(course.gpa*course.credHrs)
                                #keep adding credit hours for that semester so gradepoint total can be divided by total credits at the end
                                totalCredHrs+=course.credHrs
                                #while we go through courses in the chosen semester, print course and course grade
                                RCFile.write("\n"+course.courseName +"   "+course.courseGrade)
                                #print course comment which is an attribute of that Course
                                RCFile.write("\nComment: "+course.comment)

                            RCFile.write("\n-----------------")
                    #if there was at least one course so grades (otherwise, will throw error when try to do math and divide by 0 if no courses)
                    if flag2==True:
                        #calculate GPA
                        semesterGPA=gradePoints/totalCredHrs
                        RCFile.write("\n\nCumulative GPA for this semester: "+str(round(semesterGPA,2)))

                #if length of courses is not greater than 0
                if len(student.courseList)==0:
                    RCFile.write("\n\nNo courses to show currently")
                lblSuccess=Label(rootRC,text="Report card successfully created in same file as the program. ",font=('Helvetica bold', 14))
                lblSuccess.grid(row=9,column=0,sticky='w')
                RCFile.close() 
       # if flag is False because the student didn't match up to what's in the system, message box
        if flag==False:
            messagebox.showinfo("Error","Student not found", parent=rootRC)



    #Function: generateReportcardTask
    #Purpose: sets up environment and widgets to obtain student and semester to generate report card for
    #Parameters: none
    #Return value: none
    def generateReportcard():
            rootRC = Tk() 
            rootRC.title("GENERATE REPORT CARD")
            rootRC.geometry("1000x750") 
            frameRC = Frame(rootRC)
            frameRC.grid()

            lblStudent=Label(rootRC,text="Enter the student whose report card you would like to generate:  ",font=('Helvetica bold', 14))
            lblStudent.grid(row=0,column=0,sticky='w')
    

            entryStudent=Entry(rootRC, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=1,column=0,sticky='w')

            lblSem=Label(rootRC,text="Enter the semester you would like to generate a report card for (F for fall, S for spring, SU for summer):  ",font=('Helvetica bold', 14))
            lblSem.grid(row=2,column=0,sticky='w')

            entrySem=Entry(rootRC, width=50,font=('Helvetica bold', 14))
            entrySem.grid(row=3,column=0,sticky='w')

            endButton=Button(rootRC, text="EXIT AND GO BACK TO MENU", command=rootRC.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=7, column=0)

            
            btnSubmit = Button(rootRC,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.genReportcardTask(rootRC,entryStudent.get().title(),entrySem.get().upper() ,lblStudent, lblSem,btnSubmit,endButton))
            btnSubmit.grid(row=5,column=0, padx=40, pady=20, sticky=W)
    
    #Function: generateTranTask
    #Purpose: uses info sent from generateTran method to generate a text file transcript for a given student
    #Parameters: rootTran,studentName,lblStudent, btnSubmit,endButton
    #Return value: none
    def generateTranTask(rootTran,studentName,lblStudent, btnSubmit,endButton):
        #transcript text file is student name without spaces + Transcript.txt
        fileName=(studentName.replace(" ","")+"Transcript.txt")
       #flag false until student matches up to student in the system
        flag=False
        for student in Roster.studentObjects:
            
            #finds the right student
            if student.studentName==studentName:
                flag=True
                #recreates file every time so that it can be changed later on
                transcriptFile=open(fileName,"w")   
                transcriptFile.write("~~~~~"+studentName+" transcript~~~~~\n")

                lblSuccess=Label(rootTran,text="Transcript successfully created in same file as the program. ",font=('Helvetica bold', 14))
                lblSuccess.grid(row=7,column=0,sticky='w')
                
                #calls method in Student module to calculate the student's overall GPA and returns that to overallGPA variable
                overallGPA=student.calculateOverallGPA()
                transcriptFile.write("\nStudent ID: "+student.studentID)
                transcriptFile.write("\nCumulative GPA: "+str(overallGPA))

                # goes through all courses for student and under each semester heading, only prints the courses with the desired semester attribute to organize by semester

                transcriptFile.write("\n\nFall Courses:")
                for course in student.courseList:
                    if course.semester=="F":
                        transcriptFile.write("\n"+course.courseName +"   "+course.courseGrade)
                transcriptFile.write("\n-----------------")
               
                transcriptFile.write("\nSpring Courses:")
                for course in student.courseList:
                    if course.semester=="S":
                        transcriptFile.write("\n"+course.courseName +"   "+course.courseGrade)
                transcriptFile.write("\n-----------------")
               
                transcriptFile.write("\nSummer Courses:")
                for course in student.courseList:
                    if course.semester=="SU":
                        transcriptFile.write("\n"+course.courseName +"   "+course.courseGrade)
                transcriptFile.write("\n-----------------")
            #if student entered didn't match any students in the system
        if flag==False:
            messagebox.showinfo("Error","Student not found", parent=rootTran)


        transcriptFile.close()
    
    
    
    #Function: generateTran
    #Purpose: sets up widgets and environment to obtain student and generate transcript
    #Parameters: none
    #Return value: none
    def generateTran():
            rootTran = Tk() 
            rootTran.title("GENERATE TRANSCRIPT")
            rootTran.geometry("1000x750") 
            frameTran = Frame(rootTran)
            frameTran.grid()

            lblStudent=Label(rootTran,text="Enter the student whose transcript you would like to generate:  ",font=('Helvetica bold', 14))
            lblStudent.grid(row=0,column=0,sticky='w')

            entryStudent=Entry(rootTran, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=1,column=0,sticky='w')
    
            endButton=Button(rootTran, text="EXIT AND GO BACK TO MENU", command=rootTran.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=4, column=0)

            
            btnSubmit = Button(rootTran,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.generateTranTask(rootTran,entryStudent.get().title(),lblStudent, btnSubmit,endButton))
            btnSubmit.grid(row=3,column=0, padx=40, pady=20, sticky=W)

    #Function: loadBinary
    #Purpose: checks if binary file exists and loads updated studentObjects list to studentObjects (otherwise writes the binary file)
    #Parameters: none
    #Return value: none
    def loadBinary(): 
        # changes to the current directory of the computer. makes sure that it loads in from the right place where we made our text file
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        #checks to see if binary file exists
        file_exists = os.path.exists('studentRecords.dat')
        #if the file exists, allow user to read from it and load everything from it
        if file_exists:
            studentRecord=open("studentRecords.dat","rb") 
            #studentObjects list is set to the updated form that was dumped into studentRecord.dat
            Roster.studentObjects=pickle.load(studentRecord)
        #if the user is running the program for the first time, the binary file is created and can be written to
        else:
            studentRecord=open("studentRecords.dat","wb")


    #Function: saveToBinary
    #Purpose: saves updated studentObjects list to the binary file
    #Parameters: none
    #Return value: none
    def saveToBinary(root):
        #open the studentRecord.dat to write on and dump updated studentObject list into studentRecords.dat file
        studentRecord=open("studentRecords.dat","wb")
        pickle.dump(Roster.studentObjects,studentRecord) 
        studentRecord.close()
        root.destroy()

    #Function: writeOutSemesters
    #Purpose: converts user entered letter(s) to full semester name
    #Parameters: semester (letter(s) like s or su or f)
    #Return value: full semster name ("Fall","Spring","Summer")
    def writeOutSemester(semester):
        if semester=="F":
            return "Fall"
        elif semester=="S":
            return "Spring"
        elif semester=="SU":
            return "Summer"
        else:
            return "invalid"


    #Function: addCommentsTask
    #Purpose: assists addComments in checking to see that student exists and semester entered is correct then add comment for specified Course object in list for specified Student
    #Parameters: rootAddComments,studentChosen, courseName, lblStudent, lblCourse, entryStudent, entryCourse, lblSemester,semester, btnSubmit, endButton
    #Return value: none
    def addCommentsTask(rootAddComments,studentChosen, courseName, lblStudent, lblCourse, entryStudent, entryCourse, lblSemester,semester, btnSubmit, endButton):

            semester=Roster.writeOutSemester(semester)
            
            inList=any(obj.studentName == studentChosen for obj in Roster.studentObjects)
            #while the student can't be found so inList is false and user did not enter menu (if enters menu, moves on and goes back to main menu)
            if not inList:
                    messagebox.showinfo("Student not in the system. ", parent=rootAddComments)

            else:
            
            #once it finds the student that matches up to the one in the list of studentObjects, it calls the addCourse method in the Student class
                if semester !="Fall" and semester!="Spring" and semester!= "Summer":
                    print(semester)
                    messagebox.showinfo("Invalid semester entry. ", parent=rootAddComments)
                else:
                    flag=False
                    for student in Roster.studentObjects:
                        if student.studentName==studentChosen:
                            for course in student.courseList:
                                if course.courseName==courseName and student.studentName==studentChosen and course.semester==semester:
                                    flag=True
                                    course.addComment(studentChosen,semester,rootAddComments,lblStudent, lblCourse, entryStudent, entryCourse, lblSemester, btnSubmit, endButton)
                    if flag==False:               
                        messagebox.showinfo("Course cannot be found for "+studentChosen+" for that semester.", parent=rootAddComments)
              
    #Function: addComments
    #Purpose: sets up environment and widgets to allow user to enter comment for a specific course
    #Parameters: none
    #Return value: none
    def addComments():
            rootAddComments = Tk() # invokes tkinter environment
            rootAddComments.title("ADD GRADE")
            rootAddComments.geometry("1000x750") # dont use spaces and dont use an uppercase x
            frameAddGrade = Frame(rootAddComments)
            frameAddGrade.grid()
            # rootAddStudent.grid() 
            lblStudent=Label(rootAddComments,text="Please enter the name of the student you would like to add a comment for: ",font=('Helvetica bold', 14))
            lblStudent.grid(row=1,column=0,sticky='w')

            entryStudent=Entry(rootAddComments, width=50,font=('Helvetica bold', 14))
            entryStudent.grid(row=2,column=0,sticky='w')

            lblCourse=Label(rootAddComments,text="Please enter the course you would like to add a comment in: ",font=('Helvetica bold', 14))
            lblCourse.grid(row=3,column=0,sticky='w')

            entryCourse=Entry(rootAddComments, width=50,font=('Helvetica bold', 14))
            entryCourse.grid(row=4,column=0,sticky='w')

            lblSemester=Label(rootAddComments,text="Please enter the semester the comment is for (f for fall, s for spring, su for summer): ",font=('Helvetica bold', 14))
            lblSemester.grid(row=5,column=0,sticky='w')
        
            entrySemester=Entry(rootAddComments, width=50,font=('Helvetica bold', 14))
            entrySemester.grid(row=6,column=0,sticky='w')

            endButton=Button(rootAddComments, text="EXIT AND GO BACK TO MENU", command=rootAddComments.destroy,bg="#00008B", fg="white",font=('Helvetica bold', 18))
            endButton.grid(row=9, column=0, pady=20)
            
            btnSubmit = Button(rootAddComments,text="SUBMIT",bg="#00008B", fg="white",font=('Helvetica bold', 18),command=lambda:Roster.addCommentsTask(rootAddComments,entryStudent.get().title(),entryCourse.get().upper(),lblStudent, lblCourse,entryStudent, entryCourse, lblSemester, entrySemester.get().upper(),btnSubmit, endButton))
            btnSubmit.grid(row=8,column=0, pady=20,padx=40,sticky=W)

            rootAddComments.mainloop()


#if anyone tries to run the module, prints this 
if __name__=="__main__":
    print("This is a module meant to be imported. Please run the Glickstein_Assignment9 file")

