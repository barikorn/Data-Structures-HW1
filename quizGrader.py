"""
    File: quizGrader.py
    Author: Leziga Barikor
    Description: A program to run from inside the hw1 directory
    to generare a gradeReport.txt file.
"""

from os.path import exists
import os

def main():
    """This function calls other functions to produce graded quizes"""
    gradeBook, nameBook = readStudents()

    readQuizes(gradeBook, nameBook)

    gradingBook = open('gradeReport.txt','w')

    gradingBook.write("Student Quiz Report".center(48) + "\n\n\n")

    gradingBook.write('%-15s %9s %8s\n' % ('Student', 'Total Quiz Points', 'Overall Quiz %'))
    gradingBook.write('-'*48+'\n')

    for student in gradeBook:
        totalpts = gradeBook.get(student)
        overallpts = gradeBook.get(student)/42*100
        gradingBook.write('%-15s %7d %11.2f\n' % (student, totalpts, overallpts))

    gradingBook.write('\n')
    
    gradingBook.write('%-15s %7s\n' % ('Points Possible',42))

    gradingBook.close()
    

def checkFiles():
    directoryList = os.listdir('.')
    for dirItem in directoryList:
        print(dirItem)
    print()

    while True:
        fileName = input("Enter file name to search if it exist: ")
        if fileName == '':
            break
        elif exists(fileName):
            print(fileName, "exists!")
        else:
            print(fileName, "does NOT exist!")

def readStudents():
    """Opens and reads the name of students"""

    gradeDict = {}
    nameDict = {}
    myFile = open('students.txt', 'r')
    lineNumber = 1
    for line in myFile:
        line = line.rstrip()
        gradeDict[line] = 0
        nameDict[line]= line.lower()
        nameDict[line] = line.replace(', ','_')+ '.txt'

    myFile.close()
    return gradeDict, nameDict


def readQuizes(gradeBook, nameBook):
    """Opens quizes and creates set of scores."""
    quizDirectory = os.listdir('.')

    for dirItem in quizDirectory:
        if os.path.isdir(dirItem):
            os.chdir(dirItem)
            #gradeQuiz
            gradeQuiz(gradeBook,nameBook)
            os.chdir('..')


def gradeQuiz(gradeBook, nameBook):
    """Get answers and compare students grade."""
    answerKey = open('answers.txt','r')
    answerList = answerKey.readlines()
    #loop through students

    for name in gradeBook:
        studentFile = open(nameBook[name],'r')
        
        studentAns = studentFile.readlines()
        count = 0
        for index in range(len(studentAns)):
            if studentAns[index] == answerList[index]:
                count += 1
        #update dictionary with count
        gradeBook[name] += count
        studentFile.close()
    answerKey.close()
    
    
main()
