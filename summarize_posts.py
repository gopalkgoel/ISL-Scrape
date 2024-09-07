import extract_posts
import llm_processing

problem_path = "problems/ISL-2018-A1"
raw = extract_posts.read_posts(problem_path)

problem_statement = raw[0]['post_canonical']
print(problem_statement)

for post in raw[1:]:
    print(post['username'])
    print('---------')
    system_prompt = f"You are a math grader trying to grade the following problem: {problem_statement}"
    summary = llm_processing.LLM(
        system_prompt=system_prompt,
        user_prompt=f"Is the following post a solution to the problem. I generally expect it to be a solution, but it might just not be. Reply with a single Yes/No: {post['post_canonical']}"
    )
    print(summary)