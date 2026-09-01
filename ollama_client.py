import json
from urllib import request

def generate(prompt, model="tinyllama", temperature=0.2):
    data=json.dumps({"model":model,"prompt":prompt,"stream":False,"options":{"temperature":temperature}}).encode()
    req=request.Request("http://localhost:11434/api/generate",data=data,headers={"Content-Type":"application/json"})
    with request.urlopen(req,timeout=120) as response:
        return json.loads(response.read())["response"].strip()
