import requests
import os
from decode_unicode import decode_unicode_file

def extract_html(url):
    response = requests.get(url)
    html = response.text
    return html

def dump_text(text, path):
    with open(path, "w") as file:
        file.write(text)

def create_files(url, dir, problem_name):
    raw = extract_html(url)
    path = os.path.join(dir, problem_name)
    os.makedirs(path)
    dump_text(raw, os.path.join(path, "raw.txt"))
    decode_unicode_file(os.path.join(path, "raw.txt"), os.path.join(path, "decoded.txt"))

# url = "https://ssi.inc"
url = "https://artofproblemsolving.com/community/c6h1876757p12752810"
# url = "https://artofproblemsolving.com/community/c6h1876757p12752810" # direct link to post
# html = extract_html(url)
# dump_text(html, "3.txt")

create_files(url, "problems", "ISL-2018-A1")