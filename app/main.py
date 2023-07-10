import os
from dotenv import load_dotenv
import subprocess
import json
import openai

# Ask for a prompt
prompt = input("Enter prompt:" )

# Load the environment variables from the .env file
load_dotenv(".env")

base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")
max_tokens = int(os.getenv("MAX_TOKENS"))
temp = float(os.getenv("TEMPERATURE"))
top_p = float(os.getenv("TOP_P"))
freq = float(os.getenv("FREQ_PENALTY"))
pres = float(os.getenv("PRES_PENALTY"))
openai.api_key = os.getenv("TOKEN")
wdir = os.getenv("WORKING_DIR")

system_message = "You are a full stack developer. You write complete code. You always include all necessary styles and scripts. You write safe, validated and performant code. You do not return a description or an explanation. You do not include any formatting or backticks. Your response must be valid JSON array. Example Response: [{\"filename\":\"filename.extension\",\"content\":\"code\"},{\"filename\":\"another-file.extension\",\"content\":\"code\"}]."
messages = [
	{"role": "system", "content": system_message},
	{"role": "user", "content": prompt}
]

def get_gpt_response(messages, result):
    try:
        response = openai.ChatCompletion.create(
			model=model,
			messages=messages,
			temperature=temp,
			max_tokens=max_tokens,
			top_p=top_p,
			frequency_penalty=freq,
			presence_penalty=pres,
		)
        last_result = response['choices'][0]['message']['content']
        result += last_result
        stop = response['choices'][0]['finish_reason']
        if (str(stop) == "stop"):
            return result
        if str(stop) == "length":
            new_messages = [
				{"role": "assistant", "content": last_result},
				{"role": "user", "content": "Continue." + system_message}
			]
            messages.extend(new_messages)
            result = get_gpt_response(messages, result)
            return result
        else:
            return False

    except Exception as e:
        result, stop = "Request failed with an exception", {e}
        print( result, stop)
        return False

def get_legacy_response(prompt, result):
    try:
        response = openai.Completion.create(
			model=model,
			prompt=prompt,
			temperature=temp,
			max_tokens=max_tokens,
			top_p=top_p,
			frequency_penalty=freq,
			presence_penalty=pres,
		)
        last_result = response['choices'][0]['text']
        result += last_result
        stop = response['choices'][0]['finish_reason']
        if (str(stop) == "stop"):
            return result
        if str(stop) == "length":
            result = get_legacy_response(last_result, result)
            return result
        else:
            return False
    except Exception as e:
        result = f'Request failed with exception {e}'
        print( result, stop)
        return False

def git_push():
    os.chdir(wdir)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", prompt])
    subprocess.run(["git", "push", "origin", "main"])

def deploy():
    if model.startswith("gpt-"):
        content = get_gpt_response(messages, result='')
    else:
        prompt = system_message + " " + prompt
        content = get_legacy_response(prompt, result='') 
    data = json.loads(content)
    if content != False:
        
        for item in data:
            filename = item["filename"]
            content = item["content"]
            if filename and content:
                file_path = f"{wdir}/{filename}"
                with open(file_path, "w") as u_file:
                    u_file.write(content)
        git_push()

deploy()