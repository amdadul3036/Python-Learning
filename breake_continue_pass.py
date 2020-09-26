for i in range(5):
    if i == 3:
        continue
    print("Hello - $" , i)

'''
OUTPUT
Hello - $ 0
Hello - $ 1
Hello - $ 2
Hello - $ 4
'''

# So continue just skip the section in scilence . Look as we continue i == 3 so it does not print Hello - $ 3 anymore. It prints rest of the other. 

# -----------------------------------------------------------------------------------------------

for k in range(6):
    if k == 4:
        break
    print("Hello Break", k)

'''
OUTPUT 
Hello Break 0
Hello Break 1
Hello Break 2
Hello Break 3


So break will stop at the break condition. The program will not run after that. 
'''