import os
import sys


def is_running_from_batch():
    return os.environ.get("ComSpec", "").endswith("cmd.exe") and sys.stdout.isatty()
