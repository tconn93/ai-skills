---
name: track-gmail
description: Tracks mailbox changes or email status in the user's Gmail using the gog gmail track command from the gogcli tool.
---

# Track Gmail Skill

## Overview
This skill allows the AI agent to track changes in the user's Gmail mailbox or specific email status by executing the `gog gmail track` command from the gogcli command-line tool. It supports setting up watches for new emails, label changes, or monitoring sent email status like delivery or opens (if applicable).

## When to Use
- Invoke this skill when the user requests to track email changes, monitor for new messages, set up notifications, or check the status of emails.
- Examples of user queries: "Track new emails in my inbox", "Monitor changes to starred emails", "Track the email I sent last week".

## Core Capabilities
- Set up tracking for mailbox changes using queries or labels.
- Retrieve current tracking status or history.
- Optionally integrate with push notifications or topics.

## Instructions
1. **Parse the User Query**: Extract the tracking criteria from the user's request. Convert natural language into parameters. For example:
   - "Track unread emails from Alice" → Query: "from:alice is:unread".
   
2. **Construct the Command**: Build the shell command using `gog gmail track [options]`. Common flags include:
   - `--query "search query"`: Filter for tracking.
   - `--label "LABEL_ID"`: Specific label to track.
   - `--topic "pubsub/topic"`: For push notifications.
   - `--message-id "MESSAGE_ID"`: Track specific email status.
   - `--json`: Output in JSON format for parsing.
   - `--account user@gmail.com`: Specify the account if multiple.
   - Example: `gog gmail track --query 'from:alice is:unread' --label INBOX --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm tracking setup or extract status details.
   - Handle errors, such as invalid queries, authentication issues, or no changes found.
   - For ongoing tracking, note that it may require webhooks or further integration.

5. **Present Results**: Confirm to the user that tracking is set up or provide the current status, with details on monitored changes.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Gmail account.
- Shell access to execute commands.

## Examples
- User: "Track changes in spam folder."
  - Command: `gog gmail track --label SPAM`
- User: "Set up tracking for new emails older than a day."
  - Command: `gog gmail track --query 'newer_than:1d'`

## Success Criteria
- The skill should successfully set up or retrieve tracking information without errors.
- Ensure privacy: Only track the authorized account and do not store data beyond the current session.

## Command Help
```
gog gmail track --help
Usage: gog gmail (mail,email) track <command>
Build: v0.11.0 (91c4c15)

Email open tracking

Flags:
  -h, --help                  Show context-sensitive help.
      --color="auto"          Color output: auto|always|never
  -a, --account=STRING        Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""             OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""    Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                  Output JSON to stdout (best for scripting)
  -p, --plain                 Output stable, parseable text to stdout (TSV; no colors)
      --results-only          In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING         In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run               Do not make changes; print intended actions and exit successfully
  -y, --force                 Skip confirmations for destructive commands
      --no-input              Never prompt; fail instead (useful for CI)
  -v, --verbose               Enable verbose logging
      --version               Print version and exit

Write
  setup [flags]
    Set up email tracking (deploy Cloudflare Worker)

  opens [<tracking-id>] [flags]
    Query email opens

  status
    Show tracking configuration status
```