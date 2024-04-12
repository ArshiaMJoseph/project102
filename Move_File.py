import os
import shutil
from_dir = "C:/Users/HOME/Downloads"
to_dir = "C:/Users/HOME/Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,extension = os.path.splitext(file)
    #print(name)
   # print(extension)
    
    if extension == "":
        continue
    if extension in [".txt",".pdf",".doc",".docx"]:
        path1 = from_dir+ "/"+ file
        path2 = to_dir+"/"+ "document_files"
        path3 = to_dir+"/"+ "document_files"+"/"+ file

        if os.path.exists (path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)