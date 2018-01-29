import os, shutil, re

count = 0
avi = 0
mp4 = 0

for folderName, subFolders, filenames in os.walk(r'\\LINKSYS05548\New Volume\Movies'):
    print("\nThe current folder is " + folderName)

    for subFolder in subFolders:
        print("\n SUBFOLDER OF " + folderName + ': ' + subFolder)

        for filename in filenames:
            print('File Inside ' + folderName + ': ' +filename)

            x = folderName + '\\' + filename

            size = os.path.getsize(x) / 1000000000
            print("File is {:0.2f} GB".format(size))

            if filename.split(".")[-1] ==  "avi":
                avi += 1
            elif filename.split(".")[-1] == "mp4":
                mp4 += 1

print('We have number of avi films:' + str(avi))

print('We have number of mp4 films:' + str(mp4))

print(avi + mp4)
