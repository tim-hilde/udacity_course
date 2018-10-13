import os
def rename_files():
    # 1) get file name from folder
    file_list = os.listdir(r"/Users/timhildebrandt/Downloads/prank")
    path_original = os.getcwd()
    os.chdir(r"/Users/timhildebrandt/Downloads/prank")

    # 2) for each file, rename filename
    for file_name in file_list:
        print("Old name: "+ file_name)
        print("New name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(path_original)
rename_files()
