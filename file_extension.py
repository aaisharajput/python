#6.WAP to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
file_split = filename.split(".")
print ("The extension of the file is : " + file_split[-1])
