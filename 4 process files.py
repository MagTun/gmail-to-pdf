
# for working dir and path for saving file
import os
import shutil

abspath = os.path.abspath(__file__)
working_folder_path = os.path.dirname(abspath)
os.chdir(working_folder_path)
print("working dir set to ", working_folder_path)
folder_path = os.path.join(working_folder_path, "Lenny's Newsletter")

##  copy only last emails of a thread  
# path_to_saved= r"your_path" 
# for root, dirs, files in os.walk(folder_path):
#     if len(files) > 1:
#         all_file=[]
#         for file in files:
#             filename, file_extension = os.path.splitext(file)
#             all_file.append(filename)
#         all_file.sort()
#         file_to_keep=all_file.pop()+".pdf"
#         shutil.copy2(root+"\\"+file_to_keep, path_to_saved)
#     else :
#         for file in files:
#             filename, file_extension = os.path.splitext(file)
#             if file_extension == ".pdf":
#                 shutil.copy2(root+"\\"+file,path_to_saved )

## get path of emails with date problem (added zzz in filename)
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if "zzz" in file:
#             print(root+"\\"+file)


## delete all .eml
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         filename, file_extension = os.path.splitext(file)
#         if file_extension == ".eml":
#             print(root+"\\"+file)
#             os.remove(root+"\\"+file)

# Move all pdfs into their own folder, and emls into their own folder
eml_folder_name = "EML files"
eml_folder_path = os.path.join(folder_path, eml_folder_name)
os.makedirs(eml_folder_path, exist_ok=True)
pdf_folder_name = "PDF files"
pdf_folder_path = os.path.join(folder_path, pdf_folder_name)
os.makedirs(pdf_folder_path, exist_ok=True)

files = os.listdir(folder_path)
for f in files:
    filename, file_extension = os.path.splitext(f)
    print(f'Working on {filename}')
    absolute_file_path = os.path.join(folder_path, f)
    if file_extension == ".eml":
        shutil.move(absolute_file_path, eml_folder_path)
    elif file_extension == ".pdf":
        shutil.move(absolute_file_path, pdf_folder_path)