import shutil

shutil.copy("70_Shutil_module.py" , "shutil_copies_files.py")
shutil.copy2("70_Shutil_module.py" , "shutil_copies_files.py")
shutil.copytree(src , dst) # to copy folder
shutil.move(src , dst) # to move file
shutil.rmtree(src , dst) # to delete directory
