import os
folder_name = input("Enter folder path: ")
file_extension = input("Enter file extension: ")
count = 1
for filename in os.listdir(folder_name):
    if filename.endswith(file_extension):
        new_name = str(count) + '.' + file_extension
        os.rename(os.path.join(folder_name, filename),
                  os.path.join(folder_name, new_name))
        count += 1
