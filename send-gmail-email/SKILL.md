---
name: send-gmail-email
description: Sends an email from the user's Gmail account using the gog gmail send command from the gogcli tool.
---

# Send Gmail Email Skill

## Overview
This skill allows the AI agent to send emails from the user's Gmail account by executing the `gog gmail send` command from the gogcli command-line tool. It supports specifying recipients, subject, body, attachments, and other email details.

## When to Use
- Invoke this skill when the user requests to send an email, compose a message, reply to an email, or forward content.
- Examples of user queries: "Send an email to the team about the meeting", "Reply to John Doe's email", "Send a thank you note to Alice".

## Core Capabilities
- Send emails with customizable to, cc, bcc, subject, body (plain text or HTML).
- Add attachments.
- Optionally set reply-to or in-reply-to for threads.
- Retrieve the sent message ID for confirmation.

## Instructions
1. **Parse the User Query**: Extract key email details from the user's request. Convert natural language into structured parameters. For example:
   - "Email Bob about vacation" → To: bob@example.com, Subject: "Vacation Plans", Body: "Details here".
   - For replies, may need to chain with search-email to get thread/message ID.

2. **Construct the Command**: Build the shell command using `gog gmail send [options]`. Common flags include:
   - `--to "recipient@example.com"`: Primary recipients (comma-separated).
   - `--cc "cc@example.com"`: Carbon copy.
   - `--bcc "bcc@example.com"`: Blind carbon copy.
   - `--subject "Subject Line"`: Email title.
   - `--body "Message content"`: Plain text body (or `--html-body` for HTML).
   - `--attachment "path/to/file"`: Add files (repeatable).
   - `--in-reply-to "messageId"`: For replies.
   - `--account user@gmail.com`: Specify the account if multiple.
   - Example: `gog gmail send --to "bob@example.com" --subject "Vacation" --body "Hi Bob,\nLet's plan." --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm sending and extract details like message ID.
   - Handle errors, such as invalid recipients, authentication issues, or attachment problems.
   - For follow-up, use other gog commands like `gog gmail message get [messageId]` to verify.

5. **Present Results**: Confirm to the user that the email was sent, provide a summary of details, and share any thread link or ID.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Gmail account.
- Shell access to execute commands.

## Examples
- User: "Send an email to Alice with subject 'Meeting' and body 'See you at 2pm'."
  - Command: `gog gmail send --to "alice@example.com" --subject "Meeting" --body "See you at 2pm"`
- User: "Reply to the last email from support with 'Thanks'."
  - Command: `gog gmail send --to "support@example.com" --subject "Re: Previous Subject" --body "Thanks" --in-reply-to "previousMessageId"`

## Success Criteria
- The skill should successfully send the email and confirm without errors.
- Ensure privacy: Only send from the authorized account and do not store email data beyond the current session.

## Command Help
```
gog gmail send --help
Usage: gog gmail (mail,email) send [flags]
Build: v0.11.0 (91c4c15)

Send an email

Flags:
  -h, --help                          Show context-sensitive help.
      --color="auto"                  Color output: auto|always|never
  -a, --account=STRING                Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""                     OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""            Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                          Output JSON to stdout (best for scripting)
  -p, --plain                         Output stable, parseable text to stdout (TSV; no colors)
      --results-only                  In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING                 In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run                       Do not make changes; print intended actions and exit successfully
  -y, --force                         Skip confirmations for destructive commands
      --no-input                      Never prompt; fail instead (useful for CI)
  -v, --verbose                       Enable verbose logging
      --version                       Print version and exit

      --to=STRING                     Recipients (comma-separated; required unless --reply-all is used)
      --cc=STRING                     CC recipients (comma-separated)
      --bcc=STRING                    BCC recipients (comma-separated)
      --subject=STRING                Subject (required)
      --body=STRING                   Body (plain text; required unless --body-html is set)
      --body-file=STRING              Body file path (plain text; '-' for stdin)
      --body-html=STRING              Body (HTML; optional)
      --reply-to-message-id=STRING    Reply to Gmail message ID (sets In-Reply-To/References and thread)
      --thread-id=STRING              Reply within a Gmail thread (uses latest message for headers)
      --reply-all                     Auto-populate recipients from original message (requires --reply-to-message-id or --thread-id)
      --reply-to=STRING               Reply-To header address
      --attach=ATTACH,...             Attachment file path (repeatable)
      --from=STRING                   Send from this email address (must be a verified send-as alias)
      --track                         Enable open tracking (requires tracking setup)
      --track-split                   Send tracked messages separately per recipient
      --quote                         Include quoted original message in reply (requires --reply-to-message-id or --thread-id)
```