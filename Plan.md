The idea here is to scrape ISL solutions from AoPS (and later from the official packet, though this is much harder given its a pdf and not HTML), and potentially do some interesting analysis by feeding them into an LLM.

At a basic level, in order to tell if a post constitutes a solution, we probably have to feed it into an LLM anyway.

First iteration:
Write code that takes a thread link, and scrapes it, and stores the content of each post into a file system.
Step 1: Given a URL corresponding to an AoPS thread, extract the post content somehow.

Bro it turns out doing the http request only gives you the top part and the bottom part of the thread, and skips all the posts in the middle. That's so bad. Not tryna debug that rn, so lets see if I can pivot to webscraping a simpler webpage?

### 9/6/24
Hell nah, we will just debug this. Using ChatGPTs help, I found that each time I scroll, it's an XHR request. Will try to follow this down using ChatGPT and figure out what's going on.
LMAO HOLY SHIT the aops_session_id is just the MD5 hash of the string "session"

### 9/7/24
Reduced to hard LLM problem. It's having trouble figuring out what's a solution or not, as expected. I think that's good enough for this project. Time to move on to some more hardcore API practice.