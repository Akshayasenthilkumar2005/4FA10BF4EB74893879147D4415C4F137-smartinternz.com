class student:
   def __init__(self,name,roll_number, cgpa):
     self.name=name
     self.roll_number=roll_number
     self.cgpa=cgpa
def sort_students(student_list):    
   sorted_students =sorted (student_list,key=lambda student: student.cgpa,reverse=True) 

   return sorted_students
students=[student("Akshay","A123",9.8),student("tharun","A124",9.7),student ("sam","A125",9.6),student ("dharsan","A126",9.5)]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll_Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))