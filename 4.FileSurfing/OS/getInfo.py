import os

os.chdir('/Users/enriqueramosmunoz/Desktop') #Go to a path
print(os.getcwd()) #Print current path
print(os.listdir()) #Print directories
os.makedirs('Folder') #Make a directory
os.removedirs('Folder') #Remove directory
print(os.environ.get('Desktop'))
# os.makedirs('newFolder')
# os.mknod("newFolder/test")

# for dirpath, dirnames, filenames in os.walk('/Users/enriqueramosmunoz/Projects/Python/Python'):
#     print('Current path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
