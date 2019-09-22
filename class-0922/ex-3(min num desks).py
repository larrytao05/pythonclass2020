# A school decided to replace the desks in three classrooms.
# Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.


# Print number of desks needed if A class has 21 students, B class has 22 students, C class has 19 students

numStudentsA = 21
numStudentsB = 22
numStudentsC = 19
numDesksA = (numStudentsA + 1) // 2
numDesksB = (numStudentsB + 1) // 2
numDesksC = (numStudentsC + 1) // 2
totalDesks = numDesksA + numDesksB + numDesksC
print("The number of desks needed for all 3 classes is", totalDesks)