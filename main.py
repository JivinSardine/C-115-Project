import os
  
source = '' ###input source of the file to be renamed
  
dest = '' ###output destination of the file to be renamed
  
os.rename(source, dest)
print("Source path renamed to destination path successfully.")