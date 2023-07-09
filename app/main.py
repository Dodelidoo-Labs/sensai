import os
import openai
from dotenv import load_dotenv
import subprocess
import re


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

def get_response(messages,result):
    if model.startswith("gpt-"):
        try:
            response = openai.ChatCompletion.create(
				model=model,
				messages=messages,
				temperature=temp,
				max_tokens=max_tokens,
				top_p=top_p,
				frequency_penalty=freq,
				presence_penalty=pres,
                stop=["###"]
			)
            last_result = response['choices'][0]['message']['content']
            result += last_result
            stop = response['choices'][0]['finish_reason']
            if (str(stop) == "stop"):
                return result
            if str(stop) == "length":
                new_messages = [
					{"role": "assistant", "content": last_result},
					{"role": "user", "content": "continue"}
				]
                messages.extend(new_messages)
                result = get_response(messages, result)
                return result
            else:
                return False

        except Exception as e:
            result, stop = f'Request failed with an exception', {e}
    else:
        try:
            response = openai.Completion.create(
				model=model,
				prompt=prompt,
				temperature=temp,
				max_tokens=max_tokens,
				top_p=top_p,
				frequency_penalty=freq,
				presence_penalty=pres,
				stop=["###"]
			)
            result, stop = response['choices'][0]['text'], response['choices'][0]['finish_reason']
        except Exception as e:
            result = f'Request failed with exception {e}'

def git_push():
    os.chdir(wdir)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", prompt])
    subprocess.run(["git", "push", "origin", "main"])

def deploy():
    messages = [
		{"role": "system", "content": "You are a full stack developer. You do not wrap your code in markup, you do not use backticks or language syntax wrappers. you do not explain your response, you do not include the question in your response, you do not write a conclusion. you write only code."},
		{"role": "user", "content": prompt + "### 1. Filename: filename ```code```"}
	]
    content = get_response(messages, result='')
    if content != False:
        files = re.findall(r'(\d+\. Filename:.*?)(?=\d+\. Filename:|$)', content, re.DOTALL)
        for file in files:
            f_r = r'Filename:\s+(.*?)\n'
            c_r = r'```(\w+)\n([\s\S]*?)\n```'
            fname = re.search(f_r, file)
            cblocks = re.findall(c_r, file, re.DOTALL)
            c = '\n'.join([block[1] for block in cblocks])
            if fname and c:
                filename = fname.group(1)
                code = c
                file_path = f"{wdir}/{filename}"
                with open(file_path, "w") as u_file:
                    u_file.write(code)
        git_push()

deploy()