---
name: calendar-create-event
description: Creates a new event in the user's Google Calendar using the gog calendar create command from the gogcli tool.
---

# Create Calendar Event Skill

## Overview
This skill allows the AI agent to create new events in the user's Google Calendar by executing the `gog calendar create` command from the gogcli command-line tool. It supports specifying event details such as title, start and end times, location, attendees, and descriptions.

## When to Use
- Invoke this skill when the user requests to add a calendar event, schedule a meeting, set a reminder, or create any timed entry.
- Examples of user queries: "Add a meeting with the team tomorrow at 2pm", "Create an event for my birthday party next Saturday", "Schedule a reminder for doctor's appointment on March 1st".

## Core Capabilities
- Create events with customizable parameters like title, start/end dates, duration, location, attendees, and recurrence.
- Optionally set reminders or add descriptions.
- Retrieve the created event ID for further actions like updates or deletions.

## Instructions
1. **Parse the User Query**: Extract key event details from the user's request. Convert natural language into structured parameters. For example:
   - "Meeting with John at 3pm tomorrow for 1 hour" → Title: "Meeting with John", Start: tomorrow at 15:00, Duration: 60 minutes.
   - Use the current date (e.g., February 19, 2026) as a reference for relative times like "tomorrow" or "next week".

2. **Construct the Command**: Build the shell command using `gog calendar create [options]`. Common flags include:
   - `--title "Event Title"`: Required event name.
   - `--start "YYYY-MM-DDTHH:MM:SS"`: Start time in ISO format.
   - `--end "YYYY-MM-DDTHH:MM:SS"`: End time (alternative: `--duration MINUTES`).
   - `--description "Details here"`: Event body.
   - `--location "Place"`: Venue.
   - `--attendee email@example.com`: Add guests (repeatable).
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - Example: `gog calendar create --title "Team Meeting" --start "2026-02-20T14:00:00" --end "2026-02-20T15:00:00" --attendee john@example.com --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm creation and extract details like event ID or link.
   - Handle errors, such as invalid dates, authentication issues, or conflicts.
   - For follow-up, use other gog commands like `gog calendar get [eventId]` to verify.

5. **Present Results**: Confirm to the user that the event was created, provide a summary of details, and share any shareable link or ID.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Create a meeting with Alice on February 25th at 10am for 30 minutes."
  - Command: `gog calendar create --title "Meeting with Alice" --start "2026-02-25T10:00:00" --duration 30`
- User: "Add a birthday reminder for next year with description."
  - Command: `gog calendar create --title "Birthday Reminder" --start "2027-02-19T00:00:00" --all-day --description "Don't forget gifts!"`

## Success Criteria
- The skill should successfully create the event and confirm without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store event data beyond the current session.

## Command Help
```
gog calendar create --help
Usage: gog calendar (cal) create (add,new) <calendarId> [flags]
Build: v0.11.0 (91c4c15)

Create an event

Arguments:
  <calendarId>    Calendar ID

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

      --summary=STRING                   Event summary/title
      --from=STRING                      Start time (RFC3339)
      --to=STRING                        End time (RFC3339)
      --description=STRING               Description
      --location=STRING                  Location
      --attendees=STRING                 Comma-separated attendee emails
      --all-day                          All-day event (use date-only in --from/--to)
      --rrule=RRULE,...                  Recurrence rules (e.g., 'RRULE:FREQ=MONTHLY;BYMONTHDAY=11'). Can be repeated.
      --reminder=REMINDER,...            Custom reminders as method:duration (e.g., popup:30m, email:1d). Can be repeated (max 5).
      --event-color=STRING               Event color ID (1-11). Use 'gog calendar colors' to see available colors.
      --visibility=STRING                Event visibility: default, public, private, confidential
      --transparency=STRING              Show as busy (opaque) or free (transparent). Aliases: busy, free
      --send-updates=STRING              Notification mode: all, externalOnly, none (default: none)
      --guests-can-invite                Allow guests to invite others
      --guests-can-modify                Allow guests to modify event
      --guests-can-see-others            Allow guests to see other guests
      --with-meet                        Create a Google Meet video conference for this event
      --source-url=STRING                URL where event was created/imported from
      --source-title=STRING              Title of the source
      --attachment=ATTACHMENT,...        File attachment URL (can be repeated)
      --private-prop=PRIVATE-PROP,...    Private extended property (key=value, can be repeated)
      --shared-prop=SHARED-PROP,...      Shared extended property (key=value, can be repeated)
      --event-type=STRING                Event type: default, focus-time, out-of-office, working-location
      --focus-auto-decline=STRING        Focus Time auto-decline mode: none, all, new
      --focus-decline-message=STRING     Focus Time decline message
      --focus-chat-status=STRING         Focus Time chat status: available, doNotDisturb
      --ooo-auto-decline=STRING          Out of Office auto-decline mode: none, all, new
      --ooo-decline-message=STRING       Out of Office decline message
      --working-location-type=STRING     Working location type: home, office, custom
      --working-office-label=STRING      Working location office name/label
      --working-building-id=STRING       Working location building ID
      --working-floor-id=STRING          Working location floor ID
      --working-desk-id=STRING           Working location desk ID
      --working-custom-label=STRING      Working location custom label
```