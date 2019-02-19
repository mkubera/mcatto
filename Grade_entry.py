import statistics
import json
import logging
from pprint import pprint

admins = {'Mark':'raith', 't':'t'} # I added an admin for easier debugging

# load json file
with open('students.json') as f:
    studentDict = json.load(f)

pprint(studentDict) # print var to console (you can remove it,
                    # it's just for debugging :))

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exsist')

    print(studentDict)

def removeStudent():
    nameToRemove = input('What student do you want to remove?: ')
    if nameToRemove in studentDict:
        print('Removing student.....')
        del studentDict[nameToRemove]

    print(studentDict)



def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = statistics.mean(gradeList)

        print(eachStudent,'Has an average of:',avgGrade)




def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print ('No valid choice was given, try again')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,',login)
        while True:
            main()
        else:
            print('Invalid Password')


else:
    print('Invalid Username, please try again')
