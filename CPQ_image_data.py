import os, string

school = raw_input("School abbreviation? ")
season = str(raw_input('Season (e.g., "2017 Fall")? '))
date = raw_input("Shoot date? ")
num_img = int(raw_input("How many images of each child?"))

file_to_write = "/Users/eddieatkinson/Desktop/%s/%s.csv" % (season, school)

group = 1
groups = [] # numbers to group images
list_from_file = os.listdir("/Users/eddieatkinson/Desktop/%s/%s/%s Exports" % (season, school, school))
file_names = [] # names of the jpgs
new_file_names = [] # the final list
just_first_names = []
for item in list_from_file:
	if ".jpg" in item: # make sure we only have jpgs
		file_names.append(item)
for item in file_names:
	new_item = item.replace(".jpg", "") # remove the extension
	newer_item = new_item.replace(" ", ",", 1) # remove first space (class prefix)
	newest_item = newer_item.rstrip("-0123456789") # remove numbers and dash from end
	new_file_names.append(newest_item)
for j in range (0, len(new_file_names)):
	just_first_names.append(new_file_names[j].split(',', 1)[-1])
for k in range (0, len(just_first_names)):
	if k == 0:
		groups.append(group)
	elif just_first_names[k] != just_first_names[k - 1]:
		group += 1
		groups.append(group)
	else:
		groups.append(group)
for i in set(new_file_names):
	if (4 * num_img + 1) > new_file_names.count(i) >= (3 * num_img + 1): # if there are more than 6, for multiple proofs
		i += "_II" # add a _II to the name, so it won't get erased
		new_file_names.append(i)
		i += "I" 
		new_file_names.append(i)
		i += "I" 
		new_file_names.append(i)
	if (3 * num_img + 1) > new_file_names.count(i) >= (2 * num_img + 1):
		i += "_II" 
		new_file_names.append(i)
		i += "I" 
		new_file_names.append(i)
	if new_file_names.count(i) >= (num_img + 1):
		i += "_II"
		new_file_names.append(i)
new_list = list(set(new_file_names)) # change it back to a list
new_list_sorted = sorted(new_list) # put it in alphabetical order
the_file = open(file_to_write, "w")
for item in new_list_sorted:
	the_file.write("%s\n" % item)
image_data_file = open("/Users/eddieatkinson/Desktop/%s/%s.txt" % (season, school), "w")
image_data_file.write("Filename,FirstName,LastName,FullName,GroupTest,Class,Packages,ShootDate,SchoolName\n")
for i in range (0, len(file_names)):
	image_data_file.write("%s,%s,,%s ,%d,,,%s,%s\n" % (file_names[i], just_first_names[i], just_first_names[i], groups[i], date, school))