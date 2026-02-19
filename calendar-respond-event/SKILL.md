---
name: calendar-respond-event
description: Responds to a calendar event invitation in the user's Google Calendar using the gog calendar respond command from the gogcli tool.
---

# Respond to Calendar Event Skill

## Overview
This skill allows the AI agent to respond to event invitations in the user's Google Calendar by executing the `gog calendar respond` command from the gogcli command-line tool. It supports setting RSVP status such as accepted, declined, or tentative, with options for comments and notifications.

## When to Use
- Invoke this skill when the user requests to accept, decline, or tentatively respond to a calendar invitation, meeting request, or event.
- Examples of user queries: "Accept the team meeting invite for tomorrow", "Decline the doctor's appointment on March 1st", "Tentatively accept the birthday party invitation".

## Core Capabilities
- Update attendee status for the user on a specific event.
- Add optional comments to the response.
- Control notification sending to organizers or attendees.
- Requires the event ID, which may be obtained from prior searches using other skills like search-calendar-event.

## Instructions
1. **Parse the User Query**: Extract the response type (accept, decline, tentative) and identify the target event from the user's request. For example:
   - "Accept invite from John tomorrow" → Status: accepted, identify event ID via search if needed.
   - Confirm user intent to avoid unintended actions.

2. **Construct the Command**: Build the shell command using `gog calendar respond [eventId] [status] [options]`. Common flags include:
   - `--status accepted|declined|tentative|needsAction`: The response status.
   - `--comment "Message here"`: Optional comment for the organizer.
   - `--send-notifications all|externalOnly|none`: Control email notifications.
   - `--account user@gmail.com`: Specify the calendar account if multiple.
   - Example: `gog calendar respond abc123 --status accepted --comment "Looking forward to it!" --send-notifications all --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to confirm the response update.
   - Handle errors, such as invalid event ID, authentication issues, or if no invitation exists.
   - For verification, use other gog commands like `gog calendar get [eventId]` to fetch updated event details.

5. **Present Results**: Confirm to the user that the response was sent, provide a summary of the action, and note if notifications were dispatched.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Accept the meeting with Alice on February 25th."
  - Command: `gog calendar respond def456 --status accepted --send-notifications externalOnly`
- User: "Decline the birthday reminder invite with a note."
  - Command: `gog calendar respond ghi789 --status declined --comment "Sorry, can't make it."`

## Success Criteria
- The skill should successfully update the event response and confirm without errors.
- Ensure privacy: Only interact with the authorized calendar and do not store event data beyond the current session.



## Command Help
```
gog calendar respond --help
Usage: gog calendar (cal) respond (rsvp,reply) <calendarId> <eventId> [flags]
Build: v0.11.0 (91c4c15)

Respond to an event invitation

Arguments:
  <calendarId>    Calendar ID
  <eventId>       Event ID

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

      --status=STRING         Response status (accepted, declined, tentative, needsAction)
      --comment=STRING        Optional comment/note to include with response
```