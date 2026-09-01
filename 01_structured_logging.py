import json
import logging
import time
import uuid
from config import settings


logging.basicConfig(level=settings.log_level, format="%(message)s")
logger = logging.getLogger("agent")


def log_event(event: str, **fields) -> None:
    logger.info(json.dumps({"event": event, **fields}))


if __name__ == "__main__":
    run_id, started = str(uuid.uuid4()), time.perf_counter()
    log_event("agent_started", run_id=run_id, model=settings.model)
    time.sleep(0.05)
    log_event("agent_completed", run_id=run_id,
              latency_ms=round((time.perf_counter() - started) * 1000, 2), status="success")

