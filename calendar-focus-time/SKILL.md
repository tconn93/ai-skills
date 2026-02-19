---
name: calendar-focus-time
description: Schedules focus time blocks in the user's Google Calendar using the gog calendar focus-time command from the gogcli tool.
---

# Schedule Focus Time Skill

## Overview
This skill allows the AI agent to schedule dedicated focus time blocks in the user's Google Calendar by executing the `gog calendar focus-time` command from the gogcli command-line tool. It supports specifying durations, time ranges, and preferences to block out uninterrupted work periods.

## When to Use
- Invoke this skill when the user requests to block focus time, schedule deep work sessions, or create no-meeting periods.
- Examples of user queries: "Schedule 2 hours of focus time tomorrow morning", "Block focus time for coding next week", "Set up daily focus blocks for the next month".

## Core Capabilities
- Create focus time events with customizable duration, start times, and recurrence.
- Optionally set preferences like avoiding conflicts or specific times of day.
- Retrieve the created event IDs for further management.

## Instructions
1. **Parse the User Query**: Extract key details like duration, time range, and recurrence from the user's request. Convert natural language into structured parameters. For example:
   - "2-hour focus block tomorrow at 9am" → Duration: 120 minutes, Start: tomorrow at 09:00.
   - Use the current date (e.g., February 19, 2026) as a reference for relative times like "tomorrow" or "next week".

2. **Construct the Command**: Build the shell command using `gog calendar focus-time [options]`. Common flags include:
   - `--duration MINUTES`: Length of the focus block.
   - `--start "YYYY-MM-DDTHH:MM:SS"`: Start time in ISO format.
   - `--recurrence "RRULE:FREQ=DAILY;COUNT=5"`: Recurrence rule if needed.
   - `--avoid-conflicts`: Automatically find non-conflicting slots.
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - `--json`: Output in JSON format for parsing.
   - Example: `gog calendar focus-time --duration 120 --start "2026-02-20T09:00:00" --avoid-conflicts --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm creation and extract details like event IDs.
   - Handle errors, such as conflicts, invalid times, or authentication issues.
   - For verification, use other gog commands like `gog calendar get [eventId]` to fetch details.

5. **Present Results**: Confirm to the user that the focus time was scheduled, provide a summary of the blocks, and share any links or IDs.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Schedule 90 minutes of focus time tomorrow afternoon."
  - Command: `gog calendar focus-time --duration 90 --start "2026-02-20T14:00:00"`
- User: "Block daily focus time for the next week."
  - Command: `gog calendar focus-time --duration 60 --start "2026-02-20T10:00:00" --recurrence "RRULE:FREQ=DAILY;COUNT=7"`

## Success Criteria
- The skill should successfully schedule the focus time without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store event data beyond the current session.

## Command Help
```
gog calendar focus-time --help
Usage: gog calendar (cal) focus-time (focus) --from=STRING --to=STRING [<calendarId>] [flags]
Build: v0.11.0 (91c4c15)

Create a Focus Time block

Arguments:
  [<calendarId>]    Calendar ID (default: primary)

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

      --summary="Focus Time"          Focus time title
      --from=STRING                   Start time (RFC3339)
      --to=STRING                     End time (RFC3339)
      --auto-decline="all"            Auto-decline mode: none, all, new
      --decline-message=STRING        Message for declined invitations
      --chat-status="doNotDisturb"    Chat status: available, doNotDisturb
      --rrule=RRULE,...               Recurrence rules. Can be repeated
```