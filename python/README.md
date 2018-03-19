# Excel Image Downloader

A Python script for downloading image files from a spreadsheet containing URLs.

## Usage

1. Clone the repository
2. Install required dependencies
    ```
    pip install pandas
    pip install xlrd
    ```
3. Move your excel spreadsheet into the same folder as `app.py` and rename it to `images.xlsx`
4. On line 25 of `app.py`, change `data[i].vcImagePath` to the column heading in your spreadsheet that contains the image URLs.
5. Run the script with
    ```
    python app.py 5
    ```
    
    Where 5 indicates the number of images to be downloaded. If no argument is provided, the default is 1.

6. Look for the newly created `images` directory!

## License

MIT.