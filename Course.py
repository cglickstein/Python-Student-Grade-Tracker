# Assignment 10 
# Purpose: student grade tracker incorporating everything we have learned including OOP and GUI. 
# Course module portion
# Developer: Chava Glickstein
# Date: 1/1/2023

from tkinter import *
from tkinter import ttk

#class: Course
#Purpose: Course object
class NewCourse(object):

 #constructor to create a new student with student name, list of student's courses, course semester, course credit hours, and GPA
    def __init__(self,courseName, courseGrade, semester, credHrs):
        self.courseName=courseName 
        self.courseGrade= courseGrade
        self.semester=semester
        self.credHrs=float(credHrs)
        self.comment="N/A"
        #based on course grade, sets course's GPA

        #version for converting letter grade
        if self.courseGrade.isalpha():
            if self.courseGrade=="A":
                self.gpa=4.0
            elif self.courseGrade=="B":
                self.gpa=3.0
            elif self.courseGrade=="C":
                self.gpa=2.0
            elif self.courseGrade=="D":
                self.gpa=1.0
            elif self.courseGrade=="B":
                self.gpa=0.0
        #version for converting number grade
        else :
            self.courseGrade=float(self.courseGrade)
            if self.courseGrade>=90:
                self.gpa=4.0
            elif self.courseGrade>=80:
                self.gpa=3.0
            elif self.courseGrade>=70:
                self.gpa=2.0
            elif self.courseGrade>=60:
                self.gpa=1.0
            elif self.courseGRade>=50:
                self.gpa=0.0
        #makes sure courseGrade is a string, so I can use it to print later on 
        self.courseGrade=str(self.courseGrade)


#__str__ method. purpose to to print course name and course grade attributes of NewCourse when you print NewCourse
    def __str__(self):
        printText=self.courseName+" "+self.courseGrade
        return printText
    
     #Function: addCommentTask
    #Purpose: assigns comment entered to attribute comment
    #Parameters: self,rootAddComments,comment,lblStudent, lblCourse,entryStudent, entryCourse, lblSemester, btnSubmit, endButton
    #Return value: none
    def addCommentTask(self,rootAddComments,comment,lblStudent, lblCourse,entryStudent, entryCourse, lblSemester, btnSubmit, endButton):
        self.comment=comment

        lblSuccess=Label(rootAddComments,text="Comment successfully added. ",font=('Helvetica bold', 14))
        lblSuccess.grid(row=13,column=0,sticky='w')


     #Function: addComment
    #Purpose: allows user to enter comment which is sent to be added as comment for course
    #Parameters: self, studentChosen,semester,rootAddComments, lblStudent, lblCourse, entryStudent, entryCourse, lblSemester, btnSubmit, endButton
    #Return value: none
    def addComment(self, studentChosen,semester,rootAddComments, lblStudent, lblCourse, entryStudent, entryCourse, lblSemester, btnSubmit, endButton):
        lblComment=Label(rootAddComments,text="Please enter "+studentChosen+"'s comment for "+self.courseName+":",font=('Helvetica bold', 14))
        lblComment.grid(row=10,column=0,sticky='w')
        
        commentText=Text(rootAddComments, width=80, height=15)
        commentText.grid(row=11,column=0)

        btnSubmit = Button(rootAddComments,text="SUBMIT COMMENT",bg="#00008B", fg="white",font=('Helvetica bold', 25),command=lambda:self.addCommentTask(rootAddComments,commentText.get("1.0",END),lblStudent, lblCourse,entryStudent, entryCourse, lblSemester, btnSubmit, endButton))
        btnSubmit.grid(row=12,column=0, pady=20,padx=40,sticky=W)






#if anyone tries to run the module, prints this 
if __name__=="__main__":
    print("This is a module meant to be imported. Please run the Glickstein_Assignment9 file")