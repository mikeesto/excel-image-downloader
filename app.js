const convertExcel = require('excel-as-json').processFile;
const download = require('images-downloader').images;
const fs = require('fs');

// Path to download images to
const dest = "./images";

// Create img directory if it doesn't exist
if (!fs.existsSync(dest)) {
  fs.mkdirSync(dest);
}

convertExcel ('photos.xlsx', undefined, undefined, (err, data) => {
  const images = [];

  data.map(row => {
    if (images.length < 10) {
      images.push(row.vcImagePath);
    }
  });
  
  // Download images from urls
  download (images, dest)
  .then(function(result) {
    console.log('All images downloaded');
  })
  .catch(error => console.log('Error downloading images!', error));
});