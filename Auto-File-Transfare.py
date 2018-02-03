import os, shutil, re, pprint

count = 0
avi, mp4 = 0, 0

fileLocations = []
newfilelocation= []

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
                # Copy and add the new location
                fileLocations.append(folderName + "\\" + filename)
                newfilelocation.append(folderName + "\\" + filename + " - " + 'C:\\Users\\Thor\\Videos\\' + filename)# TODO change the location of the file destination

            elif filename.split(".")[-1] == "mp4":
                mp4 += 1

# Print the statistics
print('We have number of avi films:' + str(avi))
print('We have number of mp4 films:' + str(mp4))
print(avi + mp4)
input("Press Enter to Copy the Films into the File location Specified")

for f in fileLocations:
    shutil.copy(fileLocations[f], 'C:\\Users\\Thor\\Videos') # TODO change the location of the file destination

file = open("Location.txt", "w")
for l in newfilelocation:
    file.write(l + '\n')
