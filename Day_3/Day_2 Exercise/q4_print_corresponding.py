"""4) A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade"""

from day2_exercise_functionality import takeFloatValueFromUserPassMsg,printCorrespondingGrade

mark=takeFloatValueFromUserPassMsg("Enter Your Mark to Print correspoinding GRADE : ")
print("Your grade for mark ",mark," is ",printCorrespondingGrade(mark))