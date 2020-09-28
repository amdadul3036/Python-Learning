tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
# ---------------------------------------------------------------------------------------
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
 
#  -------------------------------------------------------------------------------------

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, Please input numeric number")
    quit()
    
if fh>40:
    reg = fr*fh
    otp = (fh - 40)*(fr*0.5)
    xp = reg + otp
else:
    xp = fh*fr

print(xp)




# -----------------------------------------------------------------------------------------



score = float(input("Enter Score: "))


if score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
else:
    print("F")
    
    
    
    # ----------------------------------------------------------------------------------------
    
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

# --------------------------------------------------------------------------------------------
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')




# --------------------------------------------------------------------------------------------

# Coursera Assignment 5.2 ; Python for everybody. 

largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
             smallest = num
    except ValueError:
        print("Invalid input")
 
print ("Maximum is", largest)
print ("Minimum is", smallest)