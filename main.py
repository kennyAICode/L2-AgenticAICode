import json, time, uuid
from contextlib import contextmanager

@contextmanager
def span(name, trace_id):
    started = time.perf_counter(); print(json.dumps({"event":"start","span":name,"trace_id":trace_id}))
    try: yield
    finally: print(json.dumps({"event":"end","span":name,"trace_id":trace_id,"ms":round((time.perf_counter()-started)*1000,2)}))

if __name__ == "__main__":
    trace = str(uuid.uuid4())
    with span("agent", trace):
        with span("tool", trace): time.sleep(.05)
