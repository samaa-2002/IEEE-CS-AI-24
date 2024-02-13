if __name__ == '__main__':
    students=[]
    second_lowest_students=[]
    students_no=int(input())
    for x in range( students_no):
        name = input()
        score = float(input())
        students.append((name,score))
    students.sort(key=lambda x:x[1])
    scores = [student[1] for student in students]
    second_lowest_grade=sorted(set(scores))[1]
    for name,score in students:
      if score==second_lowest_grade:
         second_lowest_students.append(name)
    second_lowest_students.sort ()
    for x in second_lowest_students:
        print(x)