import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs


# connecting a driver and getting HTML of the webpage
def scrape_website(webiste):
    firefox_driver_path = './geckodriver_win64.exe'     # driver allows us to control chrome
    options = webdriver.FirefoxOptions()     # specifying how browser should operate
    driver = webdriver.Firefox(service=Service(firefox_driver_path), options=options)
    
    try:
        driver.get(webiste)
        html = driver.page_source
        
        return html
    finally:
        driver.quit()
        

# html file cleaning
def extract_body_content(html_content):
    soup = bs(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = bs(body_content, 'html.parser')
    
    for style_or_script in soup(['script', 'style']):
        style_or_script.extract()
        
    cleaned_content = soup.get_text(separator='\n')
    # removing unnecessary '\n' and spaces
    cleaned_content = '\n'.join(
        line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content

# spitting content to bypass the llm's token limit (~8k)
def split_content(content, max_length=6000):
    return [
        content[i: i + max_length] for i in range(0, len(content), max_length)
    ]