import os

# specify the directory you want to list
directory_path = '/'

# list all files and directories in the specified path : it is a solution of question 4
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)


