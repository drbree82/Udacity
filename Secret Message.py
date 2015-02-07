import os
def rename_files():
    # Get File Names
    file_list = os.listdir(r"C:\Python27\Udacity\prank\prank")
    saved_path = os.getcwd()
    print("current working directory is " +saved_path)
    os.chdir(r"C:\Python27\Udacity\prank\prank")
    # For each file, Rename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
