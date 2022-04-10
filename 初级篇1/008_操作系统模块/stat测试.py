import os

folder_name = os.getcwd()

for file in os.listdir(folder_name):
    result = os.stat(file)
    print(result[6])
