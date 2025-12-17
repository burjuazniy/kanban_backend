import os
import subprocess
import sys
import time

import httpx


def before_all(context):
    context.base_url = 'http://127.0.0.1:8001'

    # 'fastapi dev' as subprocess
    context.server_proc = subprocess.Popen(
        [
            sys.executable, "-m", "fastapi",
            "dev",
            "./src/kanban_backend",
            "--port", "8001",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    # wait until server is up
    deadline = time.time() + 10
    last_err = None
    while time.time() < deadline:
        try:
            r = httpx.get(f"{context.base_url}/tasks/", timeout=1.0)
            if r.status_code < 500:
                return
        except Exception as e:
            last_err = e
        time.sleep(0.3)

    # if the server did not start - terminate and raise an error
    context.server_proc.terminate()
    raise RuntimeError(f"Server did not start in time. Last error: {last_err}")


def after_all(context):
    if getattr(context, "server_proc", None):
        context.server_proc.terminate()
        try:
            context.server_proc.wait(timeout=5)
        except Exception:
            context.server_proc.kill()
