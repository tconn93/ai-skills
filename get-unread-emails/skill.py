import subprocess
import json
import os

def run_command(cmd_list):
    result = subprocess.run(cmd_list, capture_output=True, text=True)
    # print("result",result)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr}")
    return json.loads(result.stdout)

threads = []
next_token = None

base_cmd = ["gog", "gmail", "search", "is:unread label:inbox", "--json"]

while True:
    cmd = base_cmd.copy()
    if next_token:
        cmd.extend(["--page", next_token])
    data = run_command(cmd)
    threads.extend(data.get("threads", []))
    next_token = data.get("nextPageToken")
    if not next_token:
        break

# Write to file
os.makedirs("/assistant/emails", exist_ok=True)
with open("/assistant/emails/unread.json", "w") as f:
    json.dump(threads, f, indent=4)