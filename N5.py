import re
from datetime import datetime

LINE_RE = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARN|INFO)(?:\s+.*)?$"
)



def analyze_log(text):
    counts = {"ERROR": 0, "WARN": 0, "INFO": 0}
    first = None
    last = None

    for line in (text or "").splitlines():
        m = LINE_RE.match(line.strip())
        if not m:
            continue  # другой формат или уровень

        ts, level = m.groups()
        try:
            datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")  # проверка реальной даты/времени
        except ValueError:
            continue  # например 2026-02-30 или 25:61:00

        counts[level] += 1
        if first is None:
            first = ts
        last = ts

    return {**counts, "first": first, "last": last}


log = """2026-10-13 14:23:05 INFO Service started
not a log line
2026-10-13 14:23:15 ERROR Connection refused
2026-10-13 14:23:20 WARN Retry attempt 1
2026-10-13 25:61:00 ERROR Bad time
2026-10-13 14:23:30 ERROR Giving up"""

log2 = """2026-10-13 14:23:05 info Service started
not a log line
2026-30-13 14:23:15 ERROR аывдаыдвпывп Connection refused
2026-10-13 14:23:20 WaRn Retry attempt 1
2026-10-13 25:61:00 ERRORbad time
2026-10-13 14:23:30 ERROR Giving up"""

print(analyze_log(log))
# {'ERROR': 2, 'WARN': 1, 'INFO': 1, 'first': '2026-10-13 14:23:05', 'last': '2026-10-13 14:23:30'}

print(analyze_log(log2))
# {'ERROR': 1, 'WARN': 0, 'INFO': 0, 'first': '2026-10-13 14:23:30', 'last': '2026-10-13 14:23:30'}
