# Excel Image Downloader

A Node.js script for downloading image files from a spreadsheet containing URLs.

## Usage

1. Clone the repository
2. Install required dependencies
    ```
    npm install
    ```
3. Move your excel spreadsheet to the cloned directory and rename it to `images.xlsx`
4. On line 20 of `app.js`, change `data[i].ImagePath` to the column heading in your spreadsheet that contains the image URLs.
5. Run the script with
    ```
    node app.js 5
    ```
    
    Where 5 indicates the number of images to be downloaded. If no argument is provided, the default is 1.

6. Look for the newly created `images` directory!

## License

MIT.

## :heart: Credits 

[Excel as JSON](https://github.com/stevetarver/excel-as-json)

[Images downloader](https://www.npmjs.com/package/images-downloader)