import requests
import os

def extract_html(url):
    response = requests.get(url)
    html = response.text
    return html

def dump_text(text, path):
    with open(path, "w") as file:
        file.write(text)

def decode_unicode_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Decode the unicode escape sequences
    decoded_content = content.encode().decode('unicode_escape')

    # Write the decoded content to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_content)
    
    print(f"Decoded content has been written to {output_file}")

def create_dump(url, problem_path):
    raw = extract_html(url)
    os.makedirs(problem_path)
    dump_text(raw, os.path.join(problem_path, "raw.txt"))
    decode_unicode_file(os.path.join(problem_path, "raw.txt"), os.path.join(problem_path, "decoded.txt"))

url = "https://artofproblemsolving.com/community/c6h1876757p12752810"
create_dump(url, "problems/ISL-2018-A1")