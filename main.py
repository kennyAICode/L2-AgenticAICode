from dataclasses import dataclass

@dataclass
class Snapshot: error_rate: float; p95_ms: float; empty_rate: float
def alerts(s):
    result=[]
    if s.error_rate > .05: result.append("High error rate")
    if s.p95_ms > 2000: result.append("High latency")
    if s.empty_rate > .02: result.append("Too many empty answers")
    return result or ["Healthy"]

if __name__ == "__main__":
    s=Snapshot(float(input("Error rate: ")), float(input("p95 ms: ")), float(input("Empty rate: ")))
    print(*alerts(s), sep="\n")
