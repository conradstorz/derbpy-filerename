
import os

directory = '/media/conrad/PENDRIVE/LRH_BE_normalized_Chapterized'

print 'Beginning scan of filenames for missing leading zero'

for file in os.listdir(directory):
    new_file_name = file
    try:
    	digit = int(file[1])
    except ValueError, e:
    	print 'Fixing... ', file
    	new_file_name = '0' + file
        print 'Renaming', file, 'to',  new_file_name
        new_file_name = os.path.join(directory, new_file_name)
        old_file_name = os.path.join(directory, file)
        os.rename(old_file_name, new_file_name)

print 'Beginning scan of filenames for wrong file name'

for file in os.listdir(directory):
    new_file_name = file
    if file[6] != 'B':
    	new_file_name = file[:6] + 'Battlefield Earth.mp3'
        print 'Renaming', file, 'to',  new_file_name
        new_file_name = os.path.join(directory, new_file_name)
        old_file_name = os.path.join(directory, file)
        os.rename(old_file_name, new_file_name)

print 'All issues fixed.'