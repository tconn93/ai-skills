---
name: calendar-update-event
description: Updates an existing event in the user's Google Calendar using the gog calendar update command from the gogcli tool.
---

# Update Calendar Event Skill

## Overview
This skill allows the AI agent to update existing events in the user's Google Calendar by executing the `gog calendar update` command from the gogcli command-line tool. It supports modifying event details such as title, start and end times, location, attendees, and descriptions.

## When to Use
- Invoke this skill when the user requests to modify a calendar event, reschedule a meeting, update details, or change any aspect of an existing event.
- Examples of user queries: "Change my team meeting to 3pm tomorrow", "Update the location for my doctor's appointment on March 1st", "Add Alice to the birthday party event next Saturday".

## Core Capabilities
- Update events with new parameters like title, start/end dates, duration, location, attendees, and recurrence.
- Optionally modify reminders or descriptions.
- Requires the event ID, which may be obtained from prior searches using other skills like search-calendar-event.

## Instructions
1. **Parse the User Query**: Extract the update criteria and identify the target event from the user's request. Convert natural language into structured parameters. For example:
   - "Reschedule meeting with John to 4pm tomorrow" → Identify event (may require prior search), then update Start: tomorrow at 16:00.
   - Use the current date (e.g., February 19, 2026) as a reference for relative times like "tomorrow" or "next week".
   - If event ID is not known, suggest or chain with a search skill first.

2. **Construct the Command**: Build the shell command using `gog calendar update [eventId] [options]`. Common flags include:
   - `--title "New Event Title"`: Update event name.
   - `--start "YYYY-MM-DDTHH:MM:SS"`: New start time in ISO format.
   - `--end "YYYY-MM-DDTHH:MM:SS"`: New end time (alternative: `--duration MINUTES`).
   - `--description "Updated Details"`: Update event body.
   - `--location "New Place"`: Update venue.
   - `--attendee email@example.com`: Add or update guests (repeatable).
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - Example: `gog calendar update abc123 --title "Updated Team Meeting" --start "2026-02-20T15:00:00" --end "2026-02-20T16:00:00" --attendee alice@example.com --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm the update and extract updated details.
   - Handle errors, such as invalid event ID, authentication issues, or conflicts.
   - For verification, use other gog commands like `gog calendar get [eventId]` to fetch updated event details.

5. **Present Results**: Confirm to the user that the event was updated, provide a summary of the new details, and share any updated link or ID.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Update the meeting with Alice to 11am on February 25th."
  - Command: `gog calendar update def456 --start "2026-02-25T11:00:00" --duration 30`
- User: "Change the description of my birthday reminder."
  - Command: `gog calendar update ghi789 --description "Updated: Bring cake!"`

## Success Criteria
- The skill should successfully update the event and confirm without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store event data beyond the current session.

## Command Help
```
gog calendar update --help
Usage: gog calendar (cal) update (edit,set) <calendarId> <eventId> [flags]
Build: v0.11.0 (91c4c15)

Update an event

Arguments:
  <calendarId>    Calendar ID
  <eventId>       Event ID

Flags:
  -h, --help                             Show context-sensitive help.
      --color="auto"                     Color output: auto|always|never
  -a, --account=STRING                   Account email for API commands (gmail/calendar/chat/classroom/drive/docs/slides/contacts/tasks/people/sheets/forms/appscript)
      --client=""                        OAuth client name (selects stored credentials + token bucket)
      --enable-commands=""               Comma-separated list of enabled top-level commands (restricts CLI)
  -j, --json                             Output JSON to stdout (best for scripting)
  -p, --plain                            Output stable, parseable text to stdout (TSV; no colors)
      --results-only                     In JSON mode, emit only the primary result (drops envelope fields like nextPageToken)
      --select=STRING                    In JSON mode, select comma-separated fields (best-effort; supports dot paths). Desire path: use --fields for most commands.
  -n, --dry-run                          Do not make changes; print intended actions and exit successfully
  -y, --force                            Skip confirmations for destructive commands
      --no-input                         Never prompt; fail instead (useful for CI)
  -v, --verbose                          Enable verbose logging
      --version                          Print version and exit

      --summary=STRING                   New summary/title (set empty to clear)
      --from=STRING                      New start time (RFC3339; set empty to clear)
      --to=STRING                        New end time (RFC3339; set empty to clear)
      --description=STRING               New description (set empty to clear)
      --location=STRING                  New location (set empty to clear)
      --attendees=STRING                 Comma-separated attendee emails (replaces all; set empty to clear)
      --add-attendee=STRING              Comma-separated attendee emails to add (preserves existing attendees)
      --all-day                          All-day event (use date-only in --from/--to)
      --rrule=RRULE,...                  Recurrence rules (e.g., 'RRULE:FREQ=MONTHLY;BYMONTHDAY=11'). Can be repeated. Set empty to clear.
      --reminder=REMINDER,...            Custom reminders as method:duration (e.g., popup:30m, email:1d). Can be repeated (max 5). Set empty to clear.
      --event-color=STRING               Event color ID (1-11, or empty to clear)
      --visibility=STRING                Event visibility: default, public, private, confidential
      --transparency=STRING              Show as busy (opaque) or free (transparent). Aliases: busy, free
      --guests-can-invite                Allow guests to invite others
      --guests-can-modify                Allow guests to modify event
      --guests-can-see-others            Allow guests to see other guests
      --scope="all"                      For recurring events: single, future, all
      --original-start=STRING            Original start time of instance (required for scope=single,future)
      --private-prop=PRIVATE-PROP,...    Private extended property (key=value, can be repeated)
      --shared-prop=SHARED-PROP,...      Shared extended property (key=value, can be repeated)
      --event-type=STRING                Event type: default, focus-time, out-of-office, working-location
      --focus-auto-decline=STRING        Focus Time auto-decline mode: none, all, new
      --focus-decline-message=STRING     Focus Time decline message (set empty to clear)
      --focus-chat-status=STRING         Focus Time chat status: available, doNotDisturb
      --ooo-auto-decline=STRING          Out of Office auto-decline mode: none, all, new
      --ooo-decline-message=STRING       Out of Office decline message (set empty to clear)
      --working-location-type=STRING     Working location type: home, office, custom
      --working-office-label=STRING      Working location office name/label
      --working-building-id=STRING       Working location building ID
      --working-floor-id=STRING          Working location floor ID
      --working-desk-id=STRING           Working location desk ID
      --working-custom-label=STRING      Working location custom label
      --send-updates=STRING              Notification mode: all, externalOnly, none (default: none)
```