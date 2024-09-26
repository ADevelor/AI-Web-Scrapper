import streamlit as sl
from scrape import (
    scrape_website, 
    extract_body_content, 
    clean_body_content, 
    split_content,
    )
from parse import parse_with_ollama

# simple UI
sl.title('AI Web Scraper')    # website title
url = sl.text_input("Enter a Website URL: ")    # text input box

if sl.button('Scrape'):     # if created button pressed
    sl.write('Scraping website...')
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    # store clean content to be able to access it later
    sl.session_state.content = cleaned_content
    # button that opens and closes text field
    with sl.expander('View scrapped content'):
        sl.text_area('Scrapped content', cleaned_content, height=300)    # expandable text box
        
# asking user for a prompt
if 'content' in sl.session_state:
    parse_description = sl.text_area('What do you want to parse?')
    
    if sl.button('Parse content'):
        if parse_description:
            sl.write('Parsing...')
            
            content_pieces = split_content(sl.session_state.content)
            result = parse_with_ollama(content_pieces, parse_description)
            sl.write(result)