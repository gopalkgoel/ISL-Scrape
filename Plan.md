The idea here is to scrape ISL solutions from AoPS (and later from the official packet, though this is much harder given its a pdf and not HTML), and potentially do some interesting analysis by feeding them into an LLM.

At a basic level, in order to tell if a post constitutes a solution, we probably have to feed it into an LLM anyway.

First iteration:
Write code that takes a thread link, and scrapes it, and stores the content of each post into a file system.
Step 1: Given a URL corresponding to an AoPS thread, extract the post content somehow.