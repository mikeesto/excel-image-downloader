import os
import sys
import pandas
import xlrd
import urllib

# Path to download images to
dest = "./images"

# Create img directory if it does not exist
try: 
  os.makedirs(dest)
except OSError:
  if not os.path.isdir(dest):
    raise

# Store number of images to download
if (len(sys.argv) > 2):
  startIndex = int(sys.argv[1])
  endIndex = int(sys.argv[2])
else:
  startIndex = 0
  try:
    endIndex = int(sys.argv[1])
  except IndexError: 
    endIndex = 0

# Get data from excel spreadsheet
data = pandas.read_excel('images.xlsx')

# Store URL values
values = data['vcImagePath'].values

# Store IDs
ids = data['biOcrImageId'].values

splitValues = values[startIndex:endIndex + 1]
splitIds = ids[startIndex:endIndex + 1]

for index, value in enumerate(splitValues):
  try: 
    urllib.urlretrieve(value, dest + "/" + str(splitIds[index]) + ".jpg" )
  except:
    print "I could not download image " + str(splitIds[index])

print "Images downloaded!"