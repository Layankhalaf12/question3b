#b)	Use version management with git and make the following changes to the program in part a: The loop breaks if the user
#  types your student number print the message “ cutoff point”. The loop should skip #the statements in current iteration and does not
#  increment count whenever the user types a multiple of 11.
#Flowchart is required for this program
num = 0
count = 0  
studentN = "991274007" 
while True:
    num = input("please Enter your student number: ")
    if num == studentN:
        print("cutoff point")
        break

    num = int(num) 
    if num % 11 == 0:
        continue
    
    count += 1  
    print("you entered a number", count, "times")
