import os
from dotenv import load_dotenv
import requests
import json
import html
import subprocess

# Ask for a prompt
prompt = input("Enter prompt:" )

# Load the environment variables from the .env file
load_dotenv(".env")

base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")
max_tokens = int(os.getenv("MAX_TOKENS"))
temp = float(os.getenv("TEMPERATURE"))
token = os.getenv("TOKEN")
wdir = os.getenv("WORKING_DIR")

def route_endpoint_data():
    if model == "text-davinci-003":
        endpoint = "completions"
        payload = json.dumps({
            "model": model,
			"prompt": prompt,
			"max_tokens": max_tokens,
			"temperature": temp
		})
    else:
        endpoint = "chat/completions"
        payload = json.dumps({
            "model": model,
			"messages": [
                {
                    "role": "system", 
                    "content": "You are a Professional Full Stack Developer. Provide clean, safe, secure and performant code. Do not add the question, or explanations, to your answer. Provide only pure code answers. Do not wrap the code in any backtics, or else code formatting wrappers. Provide raw, secure source codee only."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
        	],
            "temperature": temp,
    		"max_tokens": max_tokens
		})
    return endpoint, payload

def make_post_request():
    endpoint, payload = route_endpoint_data()
    url = f"{base_url}/{endpoint}"
    headers = {
		'Content-Type': 'application/json',
		'Authorization': f"Bearer {token}"
	}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def get_response():
    response_data = make_post_request()
    if response_data.status_code == 200:
        data = response_data.json()
        choices = data.get("choices", [])
        for choice in choices:
                finish_reason = choice.get("finish_reason", "")
                if model == 'text-davinci-003':
                    answer = html.unescape(choice.get("text", "")).strip()
                else:
                    answer = html.unescape(choice.get("message", "")['content']).strip()
                return answer
    else:
       print(f"Bad response code: {response_data.status_code}")
       return False

def git_push():
    os.chdir(wdir)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", prompt])
    subprocess.run(["git", "push", "origin", "main"])

def deploy(file):
    file_path = f"{wdir}/{file}"
    content = get_response()
    if content != False:
        with open(file_path, "w") as file:
            file.write(content)
        git_push()

deploy("index.php")