---
name: calendar-out-of-office
description: Sets out-of-office status in the user's Google Calendar using the gog calendar out-of-office command from the gogcli tool.
---

# Set Out-of-Office Skill

## Overview
This skill allows the AI agent to set or manage out-of-office (OOO) status in the user's Google Calendar by executing the `gog calendar out-of-office` command from the gogcli command-line tool. It supports specifying time periods, custom messages, and options for auto-declining invitations during the OOO period.

## When to Use
- Invoke this skill when the user requests to set out-of-office status, mark vacation time, or enable auto-replies for unavailability.
- Examples of user queries: "Set out of office from tomorrow to Friday", "Enable OOO for my vacation next month with a message", "Mark me as out of office for the afternoon".

## Core Capabilities
- Create OOO events with start/end times, custom messages, and decline preferences.
- Optionally set visibility or recurrence.
- Retrieve confirmation of the OOO setup for verification.

## Instructions
1. **Parse the User Query**: Extract key details like start/end times, message, and preferences from the user's request. Convert natural language into structured parameters. For example:
   - "OOO from February 20th to 25th with message 'On vacation'" → Start: 2026-02-20, End: 2026-02-25, Message: "On vacation".
   - Use the current date (e.g., February 19, 2026) as a reference for relative times like "tomorrow" or "next week".

2. **Construct the Command**: Build the shell command using `gog calendar out-of-office [options]`. Common flags include:
   - `--start "YYYY-MM-DDTHH:MM:SS"`: Start time in ISO format.
   - `--end "YYYY-MM-DDTHH:MM:SS"`: End time.
   - `--message "Custom message"`: Out-of-office reply message.
   - `--decline all|new|none`: Auto-decline meeting invites (default: all).
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - `--json`: Output in JSON format for parsing.
   - Example: `gog calendar out-of-office --start "2026-02-20T00:00:00" --end "2026-02-25T23:59:59" --message "On vacation" --decline all --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm the OOO setup and extract details.
   - Handle errors, such as overlapping OOO periods, invalid dates, or authentication issues.
   - For verification, use other gog commands like `gog calendar get [eventId]` if an event is created.

5. **Present Results**: Confirm to the user that the out-of-office status was set, provide a summary of the period and message, and note any auto-decline settings.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Set out of office tomorrow for the whole day."
  - Command: `gog calendar out-of-office --start "2026-02-20T00:00:00" --end "2026-02-20T23:59:59" --message "Out of office"`
- User: "Enable OOO next week with auto-decline."
  - Command: `gog calendar out-of-office --start "2026-02-23T00:00:00" --end "2026-02-27T23:59:59" --decline all --message "Unavailable"`

## Success Criteria
- The skill should successfully set the out-of-office status and confirm without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store data beyond the current session.


## Command Help
```
gog calendar out-of-office --help
Usage: gog calendar (cal) out-of-office (ooo) --from=STRING --to=STRING [<calendarId>] [flags]
Build: v0.11.0 (91c4c15)

Create an Out of Office event

Arguments:
  [<calendarId>]    Calendar ID (default: primary)

Flags:
  -h, --help                       Show context-sensitive help.
      --color="auto"               Color output: auto|always|never
  -a, --account=STRING             Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""                  OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""         Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                       Output JSON to stdout (best for scripting)
  -p, --plain                      Output stable, parseable text to stdout (TSV; no colors)
      --results-only               In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING              In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run                    Do not make changes; print intended actions and exit successfully
  -y, --force                      Skip confirmations for destructive commands
      --no-input                   Never prompt; fail instead (useful for CI)
  -v, --verbose                    Enable verbose logging
      --version                    Print version and exit

      --summary="Out of office"    Out of office title
      --from=STRING                Start date or datetime (RFC3339 or YYYY-MM-DD)
      --to=STRING                  End date or datetime (RFC3339 or YYYY-MM-DD)
      --auto-decline="all"         Auto-decline mode: none, all, new
      --decline-message="I am out of office and will respond when I return."
                                   Message for declined invitations
      --all-day                    Create as all-day event
```