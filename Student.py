# Assignment 10 
# Purpose: student grade tracker incorporating everything we have learned including OOP and GUI. 
# Student module portion
# Developer: Chava Glickstein
# Date: 1/1/2023

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog 
import Course
import Roster
#for generating random ID
import random
import string

studentIDList=[]
#class: NewStudent
#Purpose: Student object
class NewStudent(object):

    #constructor to create a new student with student name, list of student's courses, and unique student ID
    def __init__(self,studentName, courseList):
        self.studentName=studentName 
        self.courseList= courseList
        #generates a string of 10 random numbers
        studentID = ''.join([random.choice(string.digits) for n in range(10)])
        #only sets studentID if the studentID does not already exist (it's not in list of studentIDs which gets added to every time an ID is created)
        if studentID not in studentIDList:
            studentIDList.append(studentID)
            self.studentID=studentID

        #not using because want to allow user to also enter first name for new students
        # obtaining last name to sort student objects by name to display students in alphabetical order for display student method
        # lastNameStart=studentName.rfind(" ")
        # if lastNameStart==-1:
        #     self.studentLastName=studentName
        # else:
        #     self.studentLastName=studentName[lastNameStart+1:]
        # print(self.studentLastName)

    #__str__ method. purpose to to print studentName attribute of student when NewStudent is printed
    def __str__(self):
        printText=self.studentName
        return printText
    

    #Function: addCourse
    #Purpose: Checks to see if the entered course is already a course for that particular student in particular semester otherwise creates the course and adds it to the student's course list
    #Parameters: self, rootAddGrade, courseName, grade, credHrs, lbl3, semester,btnSubmit
    #Return value: none
    def addCourse(self, rootAddGrade, courseName, grade, credHrs, lbl3, semester,btnSubmit):
        flag= True
        #for each course in that particular student's course list, check if the course already exists in semester entered or displays error messagebox
        for course in self.courseList:
                if course.courseName==courseName  and course.semester==semester:
                    # while course.courseName==courseName and courseName !="MENU":
                    # courseName=input("\nSorry that course already exists for that student. Enter new course name or \"menu\" to go back to the main menu: ").upper()
                    messagebox.showinfo("Error","Sorry that course already exists for that student. Please try again and make sure to enter a correct course")
                    flag=False
        if flag==True:
            newCourse=Course.NewCourse(courseName, grade, semester,credHrs)
            #append that course object to the student object's list of courses 
            self.courseList.append(newCourse)
            lbl3.configure(text="Student record was successfully updated")
    
    #Function: calculateOverallGPA
    #Purpose: goes through course grades in each course object and calculates total gpa
    #Parameters: self
    #Return value: actual GPA or "no current gpa" string
    def calculateOverallGPA(self):
        gradePoints=0
        totalCredHrs=0
            # transcriptFile.write("\nStudent: "+student.studentName+"\n\n\n")
        if len(self.courseList)>0:
            for course in self.courseList:
                gradePoints+=(course.gpa*course.credHrs)
                totalCredHrs+=course.credHrs
            self.cumulativeGPA=gradePoints/totalCredHrs
            return self.cumulativeGPA
        else:
            return "No current GPA"
    
    #doing in the Roster's generateRC method because already going through all of the courses there
    # def calculateSemesterGPA(self):

        

#if anyone tries to run the module, prints this 
if __name__=="__main__":
    print("This is a module meant to be imported. Please run the Glickstein_Assignment9 file")