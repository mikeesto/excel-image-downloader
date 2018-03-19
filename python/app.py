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
try:
  count = int(sys.argv[1])
except IndexError: 
  count = 1

# Get list of images from excel spreadsheet
data = pandas.read_excel('images.xlsx')
values = data['vcImagePath'].values
splitValues = values[0:count]

for index, value in enumerate(splitValues):
  urllib.urlretrieve(value, dest + "/" + str(index) + ".jpg" )

print "Images downloaded!"