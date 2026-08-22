import os, shutil

# getting input from user
path = input("Enter the path where files are located: ")

# print(path)
# print(os.listdir(path))

# required folders names as list
folder_names = ["csv_files", "code_files", "png_files", "jpg_files", "text_files"]

# creating folders if not created
for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# storing file names as a list
file_name = os.listdir(path)

# moving the files into their relative folder based on their extentions
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv_files/" + file):
        shutil.move(path + file, path + "csv_files/" + file)
    elif ".ipynb" in file and not os.path.exists(path + "code_files/" + file):
        shutil.move(path + file, path + "code_files/" + file)
    elif ".jpeg" in file and not os.path.exists(path + "jpg_files/" + file):
        shutil.move(path + file, path + "jpg_files/" + file)
    elif ".png" in file and not os.path.exists(path + "png_files/" + file):
        shutil.move(path + file, path + "png_files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text_files/" + file):
        shutil.move(path + file, path + "text_files/" + file)
