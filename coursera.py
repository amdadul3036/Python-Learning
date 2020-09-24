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