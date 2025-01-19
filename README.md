# AI Web Scraper

This is a python AI web scraper built using Streamlit framework. This scraper can scrape the content of a website and then use Ollama LLM to parse the scraped content based on user provided description.

# Requirements

This script requires the following libraries to be installed:
- streamlit
- langchain
- langchain_ollama
- selenium
- beautifulsoup4
- lxml
- html5lib
- python-dotenv

# Overview

The script consists of three main files:

- main.py - This file contains the Streamlit application code. It defines the user interface and interacts with the other two python files (parse.py and scrape.py) to achieve the web scraping and parsing functionality.

- parse.py - This file contains functions to parse the scraped content using Ollama LLM. It utilizes langchain library to chain the user provided description prompt with Ollama LLM for achieving the desired parsing logic.

- scrape.py - This file contains functions to scrape the content from a website. It uses Selenium webdriver to control a Firefox browser to get the HTML content of the provided website URL. Then it uses BeautifulSoup to parse the HTML content and extract the body content. Finally, it cleans the body content by removing unnecessary tags and whitespaces.

# Usage

1) Make sure you have all the required libraries installed.
2) Run the script using streamlit run main.py.
3) Enter the website URL in the text input box and click on the "Scrape" button.
4) The script will scrape the website content and display it in an expandable text box.
5) Enter a description of what information you want to parse from the scraped content in the text area.
6) Click on the "Parse content" button.
7) The script will use Ollama LLM to parse the scraped content based on your description and display the parsed results.

# Important notes

- This scraper uses Ollama LLM which has a token limit of around 8k tokens. To bypass this limitation, the script splits the scraped content into smaller chunks before feeding it to the LLM for parsing.
- The current implementation uses Firefox webdriver for scraping. You can modify the script to use a different webdriver if needed.
