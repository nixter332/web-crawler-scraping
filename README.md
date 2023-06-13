# Web-Crawler-Scraping
Creating a web crawler and scraper using Scrapy to extract various detail like title, price and rating from books.toscrape.com into an external file format like csv/json.

# Webpage

![webpage](https://github.com/nixter332/web-crawler-scraping/assets/97787214/e7a4e41a-1829-4d0a-9704-f7b68e00f4cb)

# Installation
1. Create a virtual environment in the directory you want to store the project in.
2. Activate the environment.
3. Install scrapy.
4. Open your IDE of your choice and cd the directory the project is in. (Have used VSC but pycharm etc should work too)
5. Run this command in the terminal - scrapy startproject <project_name> (Scrapy will automatically create the required files for the project)
6. Create a new file in the spiders folder created or just copy in the code which has been uploaded in the code section (tutorial.py)
7. Now run the following command to crawl the spider over the website - scrapy crawl <spider_name>
8. To output the data extracted into a json/csv file just add the following command after - scrapy crawl <spider_name> -o <file_name>.csv or .json
9. The desired output should have been created in the respective file format.

# Working
1. Input the starting url of the homepage to the spider.
2. Now to scrape the website, a parse function has been defined which is used to extract the data into the variable response.
3. To extract the necessary details, the required css selectors have been extracted from the webpage and we have scraped the necessary details into 3 variables, namely title, price and rating.
4. To output the details, yield has been used which returns us a dictionary of key-value pairs.
5. Now to crawl onto other pages, the next page functionality on the webpage has been used. Therefore, we extract the <a> href attribute and pass it onto the next_page variable.
6. We use response.follow which is a functionality of scrapy and we pass it again to the parse function to scrape the details.
7. This will keep running till we run out of pages.
  
# Sample Output
  
  Json File-
  
  ![sample_json](https://github.com/nixter332/web-crawler-scraping/assets/97787214/f1c2882e-589e-4f3b-a107-5520ea4b473d)
