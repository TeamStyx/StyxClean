import os
#initialization of file count.
Number_Of_Files=0
#path name variablle .
path="C:/Users/xitzf/AppData/Local/Temp"
#os.walk () method is used for travel throught the fle .
for files in os.walk(path):
    for files in path:
        Number_Of_Files=Number_Of_Files+1
print("Total files  = ",Number_Of_Files)