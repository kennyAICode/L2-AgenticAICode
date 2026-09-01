import json, re, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1])); from ollama_client import generate

def infer(text):
    raw=generate(f'Text: {text}\nReturn JSON only: {{"intent":"learn|test|unknown","difficulty":"beginner|advanced"}}',temperature=0)
    match=re.search(r"\{.*\}",raw,re.S)
    try: data=json.loads(match.group()) if match else {}
    except json.JSONDecodeError: data={}
    return {"intent":data.get("intent","unknown"),"difficulty":data.get("difficulty","beginner")}
if __name__ == "__main__": print(infer(input("Learner request: ")))
