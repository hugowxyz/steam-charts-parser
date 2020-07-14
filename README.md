# steam-charts-parser

This script allows you to scrape data from https://steamcharts.com/ using the command line. The script will generate a csv (.txt) file with all the data from the site. 
Please note that this web scraper only works for https://steamcharts.com/.

# How to install

1. Click the green Code button on the top right, then download as zip.
2. Unpack the zip file.
3. Open your command line and navigate to the directory where the script is.
4. run `pip3 install bs4` in case you don't have it
4. run `python3 main.py -g <game name> -u <url>` or `python3 main.py --game=<game name> --url=<url>`
5. run `python3 main.py -h` or `python3 main.py --help` if you need help

# Example usage

You can use the following command to test the script out: `python3 main.py -g Dota2 -u https://steamcharts.com/app/570` <br>
or this: `python3 main.py --game=CS:GO --url=https://steamcharts.com/app/730`
