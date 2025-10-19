import json
from datetime import datetime

def log_result(result):
    log = {
        "timestamp": datetime.now().isoformat(),
        "result": result
    }
    with open("log.txt", "a") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")
