#Susie Fagelman
#Files
#we can add delete read write and append files
#r read is the most important file
#w write
#a append
#open files and make sure to close files

import os,datetime
os.system('cls')
name="Susie"
score=120
date=datetime.datetime.now() #todays date and time
print(date.strftime("%m/%d/%Y")) #month day year #stringfortime=strftime
print(date.strftime("%Y/%m/%d"))
scoreLine=str(score)+ "\t"+name+"\t" +date.strftime("%m/%d/%Y")
print(scoreLine)
#to open a file we must create an object
myFile=open("scre.txt", 'w') #open a file twrite
myFile.write(scoreLine)
myFile.close()
myFile=open("scre.txt", 'a') #open a file twrite
myFile.write(scoreLine)
myFile.close()
myFile=open("scre.txt", 'r') #opens a file to read
# lines=myFile.readlines() #need to read entire file
print()
for line in myFile.readlines():
    print(line)
myFile.close()

