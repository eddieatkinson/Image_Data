## Image Data
This application was created specifically for my photography business. It takes jpg files and creates CSV spreadsheets for record-keeping and image-data text files for submission to my company's requisite photo lab. 

## Github Link:
[Image data GitHub](https://github.com/eddieatkinson/image_data)

## Technologies used:
**Languages:**
* Python

## Code snippets:
Turn jpg files into spreadsheet of class names and child names:
``` python
for item in list_from_file:
  if ".jpg" or ".JPG" in item: # make sure we only have jpgs
    file_names.append(item)
for item in file_names:
  new_item = item.replace(".JPG", ".jpg") # in case caps are used in extension
  new_item = item.replace(".jpg", "") # remove the extension
  newer_item = new_item.replace(" ", ",", 1) # remove first space (class prefix)
  newest_item = new_item.rstrip("-0123456789") # remove numbers and dash from end
  new_file_names.append(newest_item)
for j in range (0, len(new_file_names)):
  just_first_names.append(new_file_names[j].split(',', 1)[-1])
```
Duplicate names if child receives multiple sittings:
``` python
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
```