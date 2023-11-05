# OP_scraper
Scrape one piece images off of TCBscans and store them into a folder.

## Prequisite Libraries
 - requests
 - Beautifulsoup4
 - urllib.parse
 - if any package is not on your machine, can be installed with pip or pip3

## Usage
`python3 scraper.py -i URL -o OUTPUT_FOLDER`
 - Input the url of the TCB scans page containing the manga images
 - Declare an output folder to place all the photos in for later viewing

## Changing the Content Filter
 - by default this script parses for all images beginning with the source url of URL. If a change is needed the src url can be modified in the code
