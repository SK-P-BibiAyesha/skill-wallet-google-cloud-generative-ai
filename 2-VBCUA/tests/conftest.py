import os
import sys


def pytest_configure():
    # Windows terminals commonly default to cp1252, but these tests print UTF-8
    # symbols like ✅. Force the Python runtime to emit UTF-8 so the assertions
    # execute normally rather than crashing on print().
    if sys.platform.startswith("win"):
        os.environ.setdefault("PYTHONUTF8", "1")

        for stream_name in ("stdin", "stdout", "stderr"):
            stream = getattr(sys, stream_name, None)
            if stream is None or not hasattr(stream, "reconfigure"):
                continue
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass
