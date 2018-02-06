const convertExcel = require('excel-as-json').processFile;
const download = require('images-downloader').images;
const fs = require('fs');

// Path to download images to
const dest = "./images";

// Create img directory if it doesn't exist
if (!fs.existsSync(dest)) {
  fs.mkdirSync(dest);
}

// Store number of images to download
const count = process.argv[2] || 1;

convertExcel ('images.xlsx', undefined, undefined, (err, data) => {
  const images = [];

  for (let i = 0; i < count; i++) {
    images.push(data[i].vcImagePath);
  }
  
  // Download images from urls
  download (images, dest)
  .then(function(result) {
    console.log('All images downloaded');
  })
  .catch(error => console.log('Error downloading images!', error));
});