---
name: calendar-search
description: Searches the user's Google Calendar using the gog calendar search command from the gogcli tool.
---

# Search Calendar Skill

## Overview
This skill allows the AI agent to search for calendars or events in the user's Google Calendar account by executing the `gog calendar search` command from the gogcli command-line tool. It supports querying based on various criteria like calendar names, IDs, or event-related searches.

## When to Use
- Invoke this skill when the user requests to search their calendars, find specific calendars, or retrieve calendar details based on criteria like names, owners, or types.
- Examples of user queries: "Search my calendars for work-related ones", "Find the team calendar", "List calendars shared with me".

## Core Capabilities
- Search for calendars using queries or filters.
- Retrieve calendar IDs, summaries, or full details.
- Optionally get JSON output for further processing.

## Instructions
1. **Parse the User Query**: Extract the search criteria from the user's request. Convert natural language into command parameters. For example:
   - "Calendars with 'project' in name" → Query: "project".
   
2. **Construct the Command**: Build the shell command using `gog calendar search [query]`. Add flags if needed:
   - `--query "search term"`: The search query.
   - `--max N`: Limit results to N items.
   - `--json`: Output in JSON format for parsing.
   - `--account user@gmail.com`: Specify the account if multiple are configured.
   - Example: `gog calendar search --query "project" --max 10 --json`

3. **Execute the Command**: Run the command in the shell. Ensure gogcli is installed and authenticated with the user's Google account.

4. **Process the Output**: 
   - If JSON output is used, parse it to extract relevant information like calendar IDs, names, descriptions.
   - For further actions, use other gog commands like `gog calendar get [calendarId]` to fetch full details.
   - Handle errors, such as authentication issues or no results found.

5. **Present Results**: Summarize and display the search results to the user in a clear, readable format.

## Requirements
- gogcli installed (available at https://github.com/steipete/gogcli).
- Google OAuth authentication set up for the Calendar account.
- Shell access to execute commands.

## Examples
- User: "Search for shared calendars."
  - Command: `gog calendar search --query "shared" --max 5`
- User: "Find calendars created last year."
  - Command: `gog calendar search --query "created:>2025-01-01"`

## Success Criteria
- The skill should return accurate calendar search results without exposing sensitive information unnecessarily.
- Ensure privacy: Only search the authorized account and do not store calendar data beyond the current session.

## Command Help
```
gog calendar search --help
Usage: gog calendar (cal) search (find,query) <query> [flags]
Build: v0.11.0 (91c4c15)

Search events

Arguments:
  <query>    Search query

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

      --from=STRING           Start time (RFC3339, date, or relative: today, tomorrow, monday)
      --to=STRING             End time (RFC3339, date, or relative)
      --today                 Today only
      --tomorrow              Tomorrow only
      --week                  This week (uses --week-start, default Mon)
      --days=0                Next N days
      --week-start=""         Week start day for --week (sun, mon, ...)
      --calendar="primary"    Calendar ID
      --max=25                Max results
```
