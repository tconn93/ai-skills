---
name: get-unread-emails
description: A custom skill for OpenClaw to retrieve all unread Emails from your Google Workspace.This skill creates a `unread.json` file in `/assistant/emails` directory with all the unread emails' data. 
---

# Instructions
When the user or skill ask to get unread emails:  
1. Locate the script at `~/.openclaw/skills/get-unread-emails/skill.py`
2. Execute it using: `python3 ~/.openclaw/skills/get-unread-emails/skill.py`
3. Read the file `/assistant/emails/unread.json` to the user.


