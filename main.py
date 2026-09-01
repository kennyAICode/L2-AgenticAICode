from concurrent.futures import ThreadPoolExecutor

def facts(topic): return f"Facts collected about {topic}"
def examples(topic): return f"Example created for {topic}"
def risks(topic): return f"Risks reviewed for {topic}"

if __name__ == "__main__":
    topic=input("Topic: ")
    with ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(lambda f:f(topic),[facts,examples,risks]))
    print(*results,sep="\n")
