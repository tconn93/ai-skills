---
name: get-email-labels
description: A custom skill for OpenClaw to retrieve all email labels and store the result in the `/assistant/emails/labels.json` file.
---

# Instructions
When the user or skill ask to get unread emails:  
1. Locate the script at `~/.openclaw/skills/get-email-labels/skill.py`
2. Execute it using: `python3 ~/.openclaw/skills/get-email-labels/skill.py`
3. Read the file `/assistant/emails/labels.json` to the user.