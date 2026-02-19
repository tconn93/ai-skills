import subprocess
import json
import os

def run_command(cmd_list):
    result = subprocess.run(cmd_list, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr}")
    return json.loads(result.stdout)

cmd = ["gog", "gmail", "labels", "list", "--json"]
data = run_command(cmd)

# Write to file
os.makedirs("/assistant/emails", exist_ok=True)
with open("/assistant/emails/labels.json", "w") as f:
    json.dump(data, f, indent=4)