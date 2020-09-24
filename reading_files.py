# r = read()
# w = write()
# a = append()
# r+ = read() and write()
# These above are called "Mode"

student_file = open("student.txt","r")


# Check If the file readable or not 
print(student_file.readable())
# .readable() will give a boolean value. 
# OUTPUT 
# True 


# As it is readable let's read now. 
# print(student_file.read())
# It will read the whole file. 


# We can read single line one by one  by using readline()
# print(student_file.readline())
# print(student_file.readline())
# print(student_file.readline())
# print(student_file.readline())
# It will read first to 4th line one by one. 



# We can read all lines in a list using readlines()
print(student_file.readlines())
# As I open the file now I need to close the file.  
student_file.close()