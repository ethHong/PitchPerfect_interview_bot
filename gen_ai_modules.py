import openai
import base64
import requests

with open("api_key.txt", "r") as file:
    api_key = file.read().strip()


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def images_to_messages(image_path_list):
    messages = []
    for img in image_path_list:
        base64_image = encode_image(img)
        temp_input = {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
        }
        messages.append(temp_input)
    return messages


text_prompt = """
You are helping me with a job interview. 
For questions, conditions, and responses I provide, 

IMPORTANT: Please give me feedback on the response. SHOULD NOT be the general response, 
but mentioning input contents give tailored assistnace.

#Information
Question : {}
Role : {}
Target Company : {}

#Response
Response : {}
Images: With following input, I am providing snapshop images of the interviewee. Please based on this to provide non-verbal feedbacks - e.g, gestures, eye contact, etc.
"""


def fit_prompt_to_api_calls(text_prompt, images):
    contents = [{"type": "text"}]
    contents[0]["text"] = text_prompt

    image_inputs = images_to_messages(images)
    for i in image_inputs:
        contents.append(i)

    format = [{"role": "user"}]
    format[0]["content"] = contents
    return format

# This process refers to the documentation of OpenAI: https://platform.openai.com/docs/guides/vision
def gen_AI_call(call):

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4o-mini",
        "messages": call,
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        print("Maybe you should try again..!")
