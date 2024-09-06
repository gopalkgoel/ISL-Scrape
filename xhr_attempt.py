import requests

url = "https://artofproblemsolving.com/m/community/ajax.php"

headers_with_cookie = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # Add your full cookie header here
}

data = {
    "topic_id": 1876757,
    "direction": "forwards",
    "start_post_id": -1,
    "start_post_num": 25,
    "show_from_time": -1,
    "num_to_fetch": 1,
    "a": "fetch_posts_for_topic",
    "aops_logged_in": "false",
    "aops_user_id": 1,
    "aops_session_id": "21d6f40cfb511982e4424e0e250a9557"
}

response = requests.post(url, headers=headers_with_cookie, data=data)
print(response.json())