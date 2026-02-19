---
name: calendar-delete-event
description: Deletes an existing event in the user's Google Calendar using the gog calendar delete command from the gogcli tool.
---

# Delete Calendar Event Skill

## Overview
This skill allows the AI agent to delete existing events in the user's Google Calendar by executing the `gog calendar delete` command from the gogcli command-line tool. It supports deleting events by their ID, with options for confirmation or handling recurrences.

## When to Use
- Invoke this skill when the user requests to remove, cancel, or delete a calendar event, meeting, or appointment.
- Examples of user queries: "Delete my team meeting tomorrow", "Remove the doctor's appointment on March 1st", "Cancel the birthday party event next Saturday".

## Core Capabilities
- Delete single events or instances of recurring events.
- Requires the event ID, which may be obtained from prior searches using other skills like search-calendar-event.
- Optionally handle recurrences (e.g., delete this instance, all future, or entire series).

## Instructions
1. **Parse the User Query**: Identify the target event from the user's request. If the event ID is not provided, chain with a search skill to find it first. For example:
   - "Cancel meeting with John tomorrow" → Search for the event to get ID, then delete.
   - Confirm user intent to avoid accidental deletions.

2. **Construct the Command**: Build the shell command using `gog calendar delete [eventId] [options]`. Common flags include:
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - `--send-notifications`: Notify attendees of cancellation (true/false).
   - For recurrences: `--recurrence-mode` (this, future, all).
   - Example: `gog calendar delete abc123 --send-notifications true --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - Confirm deletion from the output.
   - Handle errors, such as invalid event ID, authentication issues, or if the event doesn't exist.
   - No detailed output typically, but verify with a follow-up search if needed.

5. **Present Results**: Confirm to the user that the event was deleted, provide a summary of what was removed, and note if notifications were sent.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Delete the meeting with Alice on February 25th."
  - Command: `gog calendar delete def456 --send-notifications true`
- User: "Remove my birthday reminder for next year."
  - Command: `gog calendar delete ghi789`

## Success Criteria
- The skill should successfully delete the event and confirm without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store event data beyond the current session.


## Command Help
```
gog calendar delete --help
Usage: gog calendar (cal) delete (rm,del,remove) <calendarId> <eventId> [flags]
Build: v0.11.0 (91c4c15)

Delete an event

Arguments:
  <calendarId>    Calendar ID
  <eventId>       Event ID

Flags:
  -h, --help                     Show context-sensitive help.
      --color="auto"             Color output: auto|always|never
  -a, --account=STRING           Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""                OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""       Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                     Output JSON to stdout (best for scripting)
  -p, --plain                    Output stable, parseable text to stdout (TSV; no colors)
      --results-only             In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING            In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run                  Do not make changes; print intended actions and exit successfully
  -y, --force                    Skip confirmations for destructive commands
      --no-input                 Never prompt; fail instead (useful for CI)
  -v, --verbose                  Enable verbose logging
      --version                  Print version and exit

      --scope="all"              For recurring events: single, future, all
      --original-start=STRING    Original start time of instance (required for scope=single,future)
      --send-updates=STRING      Notification mode: all, externalOnly, none (default: none)
```