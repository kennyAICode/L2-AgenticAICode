from dataclasses import dataclass

@dataclass
class Evaluation: simple:int; relevant:int; safe:int
def score(answer, required_word):
    words=answer.split(); return Evaluation(int(len(words)<=60),int(required_word.lower() in answer.lower()),int("password" not in answer.lower()))
def passed(e): return sum((e.simple,e.relevant,e.safe))==3
if __name__ == "__main__":
    answer=input("Persona answer: "); expected=input("Required word: "); result=score(answer,expected); print(result,"PASS" if passed(result) else "REVISE")
