#File Modes 
#When you open a file you give Python 2 things 
#The filename
#THe mode 

#Common Modes 
# "w"=write 
#Creates the file if it doesn't exist 
#Overwrites the file if it does exist (Deletes all the content that was in the file)

#"r"=read only 
#You can read the file, but we cannot change it 
#Error if the file doesn't exist 

#"a"=append(adding to)
#Create the file if it doesn't exist 
#Adds new text to the end without deleting existing content 

#with open("FolderName/FileName, "Mode" ")
#
# with open("Week9/stuff.txt","r") as file: 
#     contents=file.read()
#     print(contents)


# with open("Week9/stuff.txt","w") as file:
#     file.write("This is going to be line 1 \n")
#     file.write("This is going to be on line 2 \n")
#     file.write("This is going to be on line 3 ")
    #\n means "new line"
    #If you forget \n, everything will run together on one line

# with open("Week9/newfile.txt","w")as file:
#     file.write("This is a new document")


#Reading from a File 
#Method A: Read the whole file at once 
with open("Week9/stuff.txt","r") as file:
    contents=file.read()
    print(contents)

#Method B: Read line-by-line using a for loop 
with open("Week9/stuff.txt","r") as file:
    for line in file:
        print(line)

# with open("Week9/stuff.txt", "a") as file:
#     file.write("I am adding to this file \n")
#     file.write("Stuff is going on this page \n")

password=input("Enter your password: ")
 #len is used to count how many characters an obj is
if len(password)>=8:
    print("Password is the right length")
else:
    print("Password is too short")

