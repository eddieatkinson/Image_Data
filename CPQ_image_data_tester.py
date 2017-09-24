import string

# school = raw_input("School abbreviation? ")
# season = str(raw_input('Season (e.g., "2017 Fall")? '))
# date = raw_input("Shoot date? ")
# print "%s" % season

# file_to_write = "/Users/eddieatkinson/Desktop/%s/DataFolder/%s.csv" % (season, school)
# file_to_test = raw_input("What is the path for the files you would like to name? ")
# file_to_write = raw_input("To which file would you like to write? ")

group = 1
groups = [] # numbers to group images
# list_from_file = os.listdir("/Users/eddieatkinson/Desktop/%s/%s/%s Exports" % (season, school, school))
list_from_file = ['EPS1 Frank-9938.jpg', 'EPS1 Johnny-3462.jpg', 'EPS1 Johnny-3461.jpg', 'PS1 Nathan-109.jpg', 'PS1 Nathan-108.jpg', 'PS1 Nathan-107.jpg', 'PS1 Nathan-106.jpg', 'PS1 Nathan-105.jpg', 'PS1 Nathan-104.jpg', 'PS1 Nathan-103.jpg', 'PS1 Nathan-102.jpg', 'PS1 Nathan-101.jpg']
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
	if 25 > new_file_names.count(i) >= 19: # if there are more than 6, for multiple proofs
		i += "_4" # add a _2 to the name, so it won't get erased
		new_file_names.append(i)
	if 19 > new_file_names.count(i) >= 13:
		i += "_3" # add a _3 to the name, so it won't get erased
		# print i - 1
		new_file_names.append(i)
	if new_file_names.count(i) >= 7:
		i += "_2" # add a _3 to the name, so it won't get erased
		new_file_names.append(i)
new_list = list(set(new_file_names)) # change it back to a list
new_list_sorted = sorted(new_list) # put it in alphabetical order
# the_file = open(file_to_write, "w")
# for item in new_list_sorted:
# 	the_file.write("%s\n" % item)
# image_data_file = open("/Users/eddieatkinson/Desktop/2017 Fall/DataFolder/%s.txt" % school, "w")
# image_data_file.write("Filename,FirstName,LastName,FullName,GroupTest,Class,Packages,ShootDate,SchoolName\n")
# for i in range (0, len(file_names)):
# 	image_data_file.write("%s,%s,,%s ,%d,,,%s,%s\n" % (file_names[i], just_first_names[i], just_first_names[i], groups[i], date, school))