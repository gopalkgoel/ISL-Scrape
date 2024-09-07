import requests
import os
import json

def dump_posts_json(url, problem_path):
    """
    Assumes that url is an aops url of the desired form, something like
    "https://artofproblemsolving.com/community/c6h1876757p12752810"
    problem_path is just the directory to store the file in
    """

    topic_id = url[len("https://artofproblemsolving.com/community/c6h"):]
    topic_id = int(topic_id[:topic_id.find('p')])
        
    url_for_request = "https://artofproblemsolving.com/m/community/ajax.php"
    headers_with_cookie = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # Add your full cookie header here
    }
    data = {
        "topic_id": topic_id,
        #"direction": "forwards",
        "start_post_id": -1,
        "start_post_num": 1,
        "show_from_time": -1,
        "num_to_fetch": 10000000,
        "a": "fetch_posts_for_topic",
        "aops_logged_in": "false",
        "aops_user_id": 1,
        "aops_session_id": "21d6f40cfb511982e4424e0e250a9557" # MD5 hash of the string "session" lmao
    }
    response = requests.post(url_for_request, headers=headers_with_cookie, data=data)

    os.makedirs(problem_path, exist_ok=True)
    with open(os.path.join(problem_path, "raw_posts.json"), "w") as json_file:
        json.dump(response.json(), json_file, indent=4)

def read_posts(problem_path):
    """
    Assumes raw_posts.json exists in the directory of interest
    """
    with open(os.path.join(problem_path, "raw_posts.json"), "r") as json_file:
        posts_raw = json.load(json_file)
    return posts_raw['response']['posts']

url = "https://artofproblemsolving.com/community/c6h1876757p12752810"
dump_posts_json(url, "problems/ISL-2018-A1")