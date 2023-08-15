import openai

openai.api_key = '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'

def review_request(content, model="gpt-3.5-turbo"):

    prompt = f"Review the following life task: {content}\n\nFeedback:"
    messages = [
        {"role": "user", "content": prompt},
    ]

    review = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=200
        )["choices"][0]["message"]["content"]
    
    return review 

def ai_merge(merge_request, current_content, model="gpt-3.5-turbo"):

    # prompt = f"Merge the following task: \"{merge_request}\" into the Life Document: \"{current_content}\".\n\nComplete merged Life Document:"

    system_prompt = """
You are a merge manager assistant. Your task is to take a Life Document, which is a markdown document, and merge in 'commits' to it. 
These could be new project ideas, new habits that the user wants to build, new life goals. You shouldn't delete anything in the Life Document, but you could merge a new goal 
with an existing one, if that makes sense. Use your own expertise, as an expert in life coaching and Life Document management.
"""

    user_prompt = f"""
The current Life Document is as follows:
---
{current_content}
---

The new merge is as follows:
---
{merge_request}
---

Merged Life Document:
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    merged = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=1000  # Adjust as needed
    )["choices"][0]["message"]["content"]
    
    return merged
