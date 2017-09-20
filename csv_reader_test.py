import csv
filename = "TestPicFiles.csv"
spreadsheet = csv.reader(open(filename, 'rb'), delimiter = ',')
for row in spreadsheet:
	print(row)

