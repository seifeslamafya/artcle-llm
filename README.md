# SET_project LLM APP

# This microservice uses a Large Language Model (LLM) to automatically review student answers to article-based questions. It receives an answer and related context (e.g., article text) via API, processes the input through the LLM, and returns structured feedback such as relevance, clarity, and overall quality.

# Setting the Model

## 1) you have to download Ollama from this link
https://ollama.com/
## 2) you have to install LLAMA3 on you machine (I prefare using the CMD)
- open CMD and type 
```bash
ollama run llama3
```
(NOTE: its about 4GB so it might take time)
### Now you have LLAMA3 model running on you machine and you can chat with it anytime throug the cmd

# install packages and libraries 
## 1) create virtual env (something like node modules but for pthon projects)
```bash
python3 -m venv setvenv
```
## 2) activate the venv
```bash
.\setvenv\scripts\activate
```
to make sure that the venv is working you will see the venv name (setvenv) at the begining of any line of the terminal
## 3) install the required libraries from the reqs.text using pip (smth like npm)
```bash
pip install -r reqs.txt
```
### Run the fast api server (dev mode)
```bash
uvicorn app.main:app --reload 
```

to check the if the project is working call this api in the browser
http://127.0.0.1:8000/api/v1/