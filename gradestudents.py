def gradeStudents(grades):

    grades_count=int(input("enter your grade count: "))

    for i in range(grades_count):
        grades_item=int(input("enter a grade: "))

        nearest_multiple=int(5 * round(float(grades_item)/5))

        if (nearest_multiple-grades_item)<3:
            grades_item=nearest_multiple

        elif(nearest_multiple-grades_item)==3:
            grades_item=grades_item

        elif(grades_item)<40:
            grades_item=grades_item
    

        grades.append(grades_item)



        print(grades)
    

    return


gradeStudents([])


