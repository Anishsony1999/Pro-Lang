import os
import shutil

# os.mkdir("python_class") # if the folder is exists rasie a error
# os.makedirs("path/of /our/folders")


task =1

string = f"task{task}"
path = "python_class/"+string

if os.path.exists(path) :
    # os.rmdir(path)  if the foler is empty only this will happend
    # os.remove(path)
    shutil.rmtree(path)
else:
    os.makedirs(path)

    with open(path+'/new.py','w') as file:
        file.write("# This is new folder")

# from pathlib import Path

# Path.mkdir("")
# Path.rmdir("")

# 1,users.txt - file
# username , email , pass , balance , creat by

# 2,folder(transaction) -> anish.txt(with or depos )

# Create user -> anish,anish@gmail.com,pass

