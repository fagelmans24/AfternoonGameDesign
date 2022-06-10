#Susie Fagelman
#Calculate age
#get use year and current year
import os
os.system ('cls')
#by =input ('year you were born') give us a string
by = int( input ('year you were born,')) #type
currentYear=2022 #also number
age =currentYear-by
print ('your age is ',age)
#Selection
if age >50:
    print('you are old')
if age < 51: 
    print("you are young")