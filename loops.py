#whenever we want to repeat a set of statement in our program .
#for example: print 10 to 1000000000
'''loops make it easy for the programers to tell the system (laptop),
 which set of instructions to repeat and how !! 
 '''

 #types of loop 
 # 1) while loop
 # while condition:
 # body of the loop
 #In while loops, the condition is checked first. if it evaluates to true the body
 # of the loop is exectuted otherwise not 


 # 2)  For loop :
''' A for loop is used iterate through a sequence like list, tuple or string'''
'''a = [1,2,3]
for item in a:
    print(item)

'''

#3) Range function in python:
'''the range function in python is used to generate a sequence of numbers. we can
specify the start, stop and step -size as range(start,stop, step-size)

for example : 
    for i in range(0,7):
        print(i)

'''

#4) break statement
'''
Break statement we use when we have to come out of the loop when encountered. 
it instructs the program to exit the loop now

example:
for i in range(0,80):
    print(i)   #it will print 1, 2 and as soon as it try to print 3 it will break and exit
    if i ==3:
        break

'''