---
name: calendar-get-event
description: Searches the user's Google Calendar for events using the gog calendar list command from the gogcli tool.
---

# Search Calendar Event Skill

## Overview
This skill allows the AI agent to search for events in the user's Google Calendar by executing the `gog calendar list` command from the gogcli command-line tool. It supports querying events based on time ranges, search terms, calendars, and other filters.

## When to Use
- Invoke this skill when the user requests to search their calendar, find specific events, check for upcoming appointments, or retrieve event details based on criteria like date, keywords, attendees, etc.
- Examples of user queries: "Search my calendar for meetings next week", "Find events with John Doe", "Show events from last month containing 'project'".

## Core Capabilities
- List calendar events using filters like time ranges (timeMin/timeMax), search query (q), singleEvents for recurring, etc.
- Retrieve event IDs, summaries, or full details.
- Optionally get JSON output for further processing.

## Instructions
1. **Parse the User Query**: Extract the search criteria from the user's request. Convert natural language into command flags. For example:
   - "Events about project X next week" → `--q "project X" --time-min "2026-02-23T00:00:00" --time-max "2026-03-02T00:00:00"`
   
2. **Construct the Command**: Build the shell command using `gog calendar list [options]`. Add flags if needed:
   - `--q "search term"`: Free-text search.
   - `--time-min "YYYY-MM-DDTHH:MM:SS"`: Start of time range.
   - `--time-max "YYYY-MM-DDTHH:MM:SS"`: End of time range.
   - `--max-results N`: Limit results to N items.
   - `--json`: Output in JSON format for parsing.
   - `--calendar-id calendar@example.com`: Specify the calendar if not primary.
   - Example: `gog calendar list --q "project X" --time-min "2026-02-23T00:00:00" --time-max "2026-03-02T00:00:00" --max-results 10 --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to extract relevant information like event IDs, summaries, start/end times.
   - For further actions, use other gog commands like `gog calendar get [eventId]` to fetch full event details.
   - Handle errors, such as authentication issues or no results found.

5. **Present Results**: Summarize and display the search results to the user in a clear, readable format. If needed, offer to update or delete events.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Search for meetings with support team next month."
  - Command: `gog calendar list --q "support team meeting" --time-min "2026-03-01T00:00:00" --time-max "2026-04-01T00:00:00" --max-results 5`
- User: "Find events older than a year."
  - Command: `gog calendar list --time-max "2025-02-19T00:00:00"`

## Success Criteria
- The skill should return accurate calendar event search results without exposing sensitive information unnecessarily.
- Ensure privacy: Only search the authorized calendar and do not store event data beyond the current session.


## Command Help
```
gog calendar event --help
Usage: gog calendar (cal) event (get,info,show) <calendarId> <eventId>
Build: v0.11.0 (91c4c15)

Get event

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
```