import os, csv

# f=open("/Users/eddieatkinson/Documents/jpg_name_writer/TestPicFiles.csv",'r+')
# w=csv.writer(f)
# for path, dirs, files in os.walk("/Users/eddieatkinson/Documents/jpg_name_writer/TestPicFiles"):
#     for filename in files:
#         w.writerow([filename])

filelist = os.listdir("/Users/eddieatkinson/Documents/jpg_name_writer/TestPicFiles")
f = csv.writer(open("test2.csv", 'ab'), delimiter = ".", quotechar = " ", quoting = csv.QUOTE_MINIMAL)
for file_name in filelist:
	f.writerow([file_name])