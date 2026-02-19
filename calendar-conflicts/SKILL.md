---
name: calendar-conflicts
description: Checks for scheduling conflicts in the user's Google Calendar using the gog calendar conflicts command from the gogcli tool.
---

# Check Calendar Conflicts Skill

## Overview
This skill allows the AI agent to check for scheduling conflicts in the user's Google Calendar by executing the `gog calendar conflicts` command from the gogcli command-line tool. It supports specifying a proposed time range and optionally attendees or calendars to identify overlapping events.

## When to Use
- Invoke this skill when the user requests to check for conflicts, verify availability for a new event, or detect overlaps before scheduling.
- Examples of user queries: "Check for conflicts tomorrow at 2pm for a 1-hour meeting", "Are there any overlaps next week for a team call?", "Verify if March 1st is free for an appointment".

## Core Capabilities
- Detect conflicting events within a specified time range for primary or multiple calendars.
- Consider attendee availability if specified.
- Retrieve details of conflicting events, such as IDs, summaries, and times.
- Optionally get JSON output for further processing.

## Instructions
1. **Parse the User Query**: Extract the proposed time range, duration, and any attendees from the user's request. Convert natural language into structured parameters. For example:
   - "Conflicts for a meeting next Tuesday from 9am to 10am" → Start: next Tuesday 09:00, End: next Tuesday 10:00.
   - Use the current date (e.g., February 19, 2026) as a reference for relative times like "tomorrow" or "next week".
   
2. **Construct the Command**: Build the shell command using `gog calendar conflicts [options]`. Common flags include:
   - `--start "YYYY-MM-DDTHH:MM:SS"`: Start time of the proposed event in ISO format.
   - `--end "YYYY-MM-DDTHH:MM:SS"`: End time (alternative: `--duration MINUTES`).
   - `--attendee email@example.com`: Attendees to check (repeatable).
   - `--calendar-id calendar@example.com`: Calendars to query (repeatable; default primary).
   - `--json`: Output in JSON format for parsing.
   - `--account user@gmail.com`: Specify the account if multiple are configured.
   - Example: `gog calendar conflicts --start "2026-02-24T09:00:00" --end "2026-02-24T10:00:00" --attendee john@example.com --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to extract conflicting events with details like summaries and times.
   - Handle cases with no conflicts.
   - Handle errors, such as invalid time ranges or authentication issues.

5. **Present Results**: Inform the user of any conflicts found, listing overlapping events, or confirm the slot is free.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Check conflicts for a 30-minute slot tomorrow morning."
  - Command: `gog calendar conflicts --start "2026-02-20T09:00:00" --duration 30`
- User: "Verify overlaps next week with Alice."
  - Command: `gog calendar conflicts --start "2026-02-23T00:00:00" --end "2026-03-02T00:00:00" --attendee alice@example.com --json`

## Success Criteria
- The skill should accurately identify conflicts or confirm availability without errors.
- Ensure privacy: Only query authorized calendars and do not store data beyond the current session.

## Command Help
```
gog calendar conflicts --help
Usage: gog calendar (cal) conflicts [flags]
Build: v0.11.0 (91c4c15)

Find conflicts

Flags:
  -h, --help                   Show context-sensitive help.
      --color="auto"           Color output: auto|always|never
  -a, --account=STRING         Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""              OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""     Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                   Output JSON to stdout (best for scripting)
  -p, --plain                  Output stable, parseable text to stdout (TSV; no colors)
      --results-only           In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING          In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run                Do not make changes; print intended actions and exit successfully
  -y, --force                  Skip confirmations for destructive commands
      --no-input               Never prompt; fail instead (useful for CI)
  -v, --verbose                Enable verbose logging
      --version                Print version and exit

      --from=STRING            Start time (RFC3339, date, or relative: today, tomorrow, monday)
      --to=STRING              End time (RFC3339, date, or relative)
      --today                  Today only (timezone-aware)
      --week                   This week (uses --week-start, default Mon)
      --days=0                 Next N days (timezone-aware)
      --week-start=""          Week start day for --week (sun, mon, ...)
      --calendars="primary"    Comma-separated calendar IDs
```