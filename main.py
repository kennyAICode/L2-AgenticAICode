from dataclasses import dataclass, field

@dataclass
class Metrics:
    requests: int=0; successes: int=0; latency_ms: list[float]=field(default_factory=list)
    def record(self, ok, latency): self.requests+=1; self.successes+=int(ok); self.latency_ms.append(latency)
    def report(self):
        return {"success_rate": self.successes/self.requests if self.requests else 0, "average_ms": sum(self.latency_ms)/len(self.latency_ms) if self.latency_ms else 0}

if __name__ == "__main__":
    m=Metrics(); [m.record(ok,ms) for ok,ms in [(True,120),(True,90),(False,300)]]; print(m.report())
