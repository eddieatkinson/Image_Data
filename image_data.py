import os, string

school = raw_input("School Name? ")
date = raw_input("Shoot date? ")
file_to_test = raw_input("What is the path for the files you would like to name? ")
file_to_write = raw_input("To which file would you like to write? ")

list_from_file = os.listdir(file_to_test)
file_names = [] # names of the jpgs
new_file_names = [] # the final list
for item in list_from_file:
	if ".jpg" in item: # make sure we only have jpgs
		file_names.append(item)
for item in file_names:
	new_item = item.replace(".jpg", "") # remove the extension
	newer_item = new_item.replace(" ", ",", 1) # remove first space (class prefix)
	newest_item = newer_item.rstrip("-0123456789") # remove numbers and dash from end
	new_file_names.append(newest_item)
for i in set(new_file_names):
	if new_file_names.count(i) >= 7: # if there are more than 6, for multiple proofs
		i += "_2" # add a _2 to the name, so it won't get erased
		new_file_names.append(i)
new_list = list(set(new_file_names)) # change it back to a list
new_list_sorted = sorted(new_list) # put it in alphabetical order
the_file = open(file_to_write, "w")
for item in new_list_sorted:
	the_file.write("%s\n" % item)
image_data_file = open("%s.txt" % school, "w")
image_data_file.write("Filename,FirstName,LastName,FullName,GroupTest,Class,Packages,ShootDate,SchoolName")
for i in range (0, len(file_names)):
	image_data_file.write("%s,%s,,%s ,%d,,,%s,%s\n" % (file_names[i], new_file_names[i], new_file_names[i], i + 1, date, school))
