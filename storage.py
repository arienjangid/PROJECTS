from student import student #Import the student class (or object) from the file student.py into your current program.
# s1 = student("Ram",20)
# s1.display()
import os  # we trach ,create , check the file
import pickle # in pickle we write and read the object 
# we use rb==>> read binary
# wb ==> write binary
# os.path.exists(file name)  it check the file and return true , false

file_name = 'student.txt'

def save_student(s):  
    students = []
    if os.path.exists(file_name) :   # ✅ check file not empty
        with open(file_name, "rb") as f:
            students = pickle.load(f)  # load existing list
    students.append(s)
    with open(file_name, "wb") as f:
        pickle.dump(students, f)  # save back list

s1 = student("Alice", 20)
s2 = student("Bob", 22)
save_student(s1)
save_student(s2)

def load_student():
    if os.path.exists(file_name) :   # ✅ avoid empty file error
        with open(file_name, "rb") as f:
            data = pickle.load(f)
            return [s.display() for s in data]   # ✅ call display() on each object
    else:
        return []

print("Students in Storage : ")
print(load_student())
