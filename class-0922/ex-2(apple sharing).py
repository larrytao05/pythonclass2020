# Create two variables: numStudents and numApples
# Students take apples from a basket and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
# Test with 20 apples, 6 students

print("If there are 20 apples and 6 students:")
numStudents = 6
numApples = 20
perStudent = numApples // numStudents
notEaten = numApples % numStudents
print("The students will each get", perStudent, "apples.")
print("There will be", notEaten, "apples left in the basket.")

# Test with 25 apples, 10 students

print(" ")
print("If there are 25 apples and 10 students:")
numStudents = 10
numApples = 25
perStudent = numApples // numStudents
notEaten = numApples % numStudents
print("The students will each get", perStudent, "apples.")
print("There will be", notEaten, "apples left in the basket.")