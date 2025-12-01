gpa = float(input("Please enter your GPA: "))

# if else condition
# if else ladder

if 3.6 <= gpa <= 4.0:
    print("You got A+")
elif gpa>=3.2 and gpa<3.6:
    print("You got A")
elif gpa>=2.8 and gpa<3.2:
    print("You got B+")
elif gpa>=2.4 and gpa<2.8:
    print("You got B")
elif gpa>=2.0 and gpa <2.4:
    print("You just passed")
else:
    print("You failed your exam")