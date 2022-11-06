# coinmarketcap-web-scraper

A simple django app built to scrape data from [CoinMarketCap](https://coinmarketcap.com) and display the data in a tabular format. The frontend is built on react, with data being refreshed every 3 seconds from the server.

Celery and rabbitmq are used to keep the scraper running in the background, where data is fetched every 5 seconds from the website to keep it up to date.
