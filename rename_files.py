import os
import string

def rename_files():
    file_names = os.listdir("prank")
    original_dir = os.getcwd()
    os.chdir("prank")
    for name in file_names:
        print("Old name: " + name)
        print("New name: " + name.translate(None, "0123456789"))
        os.rename(name, name.translate(None, "0123456789"))

    os.chdir(original_dir)

rename_files()
