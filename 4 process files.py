
# for working dir and path for saving file
import os
import shutil

folder_path = r"xxx"

#  copy only last emails of a thread  
path_to_saved= r"your_path" 
for root, dirs, files in os.walk(folder_path):
    if len(files) > 1:
        all_file=[]
        for file in files:
            filename, file_extension = os.path.splitext(file)
            all_file.append(filename)
        all_file.sort()
        file_to_keep=all_file.pop()+".pdf"
        shutil.copy2(root+"\\"+file_to_keep, path_to_saved)
    else :
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".pdf":
                shutil.copy2(root+"\\"+file,path_to_saved )

# get path of emails with date problem (added zzz in filename)
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if "zzz" in file:
#             print(root+"\\"+file)


# delete all .eml
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         filename, file_extension = os.path.splitext(file)
#         if file_extension == ".eml":
#             print(root+"\\"+file)
#             os.remove(root+"\\"+file)


