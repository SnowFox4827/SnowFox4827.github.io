import json
from bs4 import BeautifulSoup

def to_json(soup):
    data = {}
    sections = soup.find_all(['section'])

    for sec in sections:
        # Use id or class as the section name if available, else auto-number
        section_name = sec.get('id') or sec.get('class', ['section'])[0]
    
        # Get the text content of the section
        content = sec.get_text(separator="\n", strip=True)
    
        data[section_name] = content
    
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    #print("Soup Converted to json")
    return data

def to_txt(json_data):
    # Save raw JSON string
    with open("output.txt", "w", encoding="utf-8") as f:
        json.dump(json_data, f)
    print("JSON saved as raw TXT successfully!")
