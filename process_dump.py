import os
import re

def extract_posts(problem_path):
    with open(os.path.join(problem_path, "decoded.txt"), 'r', encoding='utf-8') as f:
        content = f.read()
    
    post_canonical_indices = [match.end() for match in re.finditer(r'\"post_canonical\":', content)]
    #print(len(post_canonical_indices))

    username_indices = [match.end() for match in re.finditer(r'\"username\":', content)]
    #print(len(username_indices))
    print(f"number of usernames = {len(username_indices)}")

    for i,j in zip(post_canonical_indices, username_indices[:len(post_canonical_indices)]):
        solution = content[i+1:j-10]
        username = content[j+1:content.find(',', j)-1]
        print(username)
        print("-----------")
        #print(solution)


extract_posts("problems/ISL-2018-A1")