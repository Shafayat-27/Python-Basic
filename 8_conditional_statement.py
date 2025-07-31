mark = 100

if(mark >= 90):
    grade = "A+"
elif(mark >= 80 and mark<90):
    grade = "B"
elif(mark >= 70 and mark<80):
    grade = "C"
else:
    grade = "F"
    
print("Grade of the student is:",grade)