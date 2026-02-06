import json
from pathlib import Path

def to_json(soup):
    #downloads_path = Path.home() / "Downloads"
    #file_name = "output.txt"
    #file_path = downloads_path / file_name
    data = {}
    sections = soup.find_all(['section'])

    for sec in sections:
        # Use id or class as the section name if available, else auto-number
        section_name = sec.get('id') or sec.get('class', ['section'])[0]
    
        # Get the text content of the section
        content = sec.get_text(separator="\n", strip=True)
    
        data[section_name] = content
    
    #with open(file_path, "w", encoding="utf-8") as f:
        #json.dump(data, f, indent=4, ensure_ascii=False)

    print("Soup Converted to json")
    return data

def to_txt(json_data):
    # Save raw JSON string
    downloads_path = Path.home() / "Downloads"
    file_name = "output.txt"
    file_path = downloads_path / file_name

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f)

    print(f"JSON saved as raw TXT successfully to {file_path} !")
