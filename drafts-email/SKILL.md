# Search Email Skill

## Description

The Search Email skill allows users to search and manage email drafts in Gmail using the `gog` CLI tool, which is part of the gogcli Google Suite CLI. This skill focuses on handling drafts, including listing, creating, and updating them. For searching within drafts or general emails, it leverages Gmail's search operators via the `gog gmail search` command (e.g., to find specific drafts with `is:draft`).

This skill is useful for automating email draft management from the command line, with JSON output support for scripting.

## Requirements

- Install gogcli: Clone and build from [GitHub repository](https://github.com/steipete/gogcli).
- Authenticate with Google: Run `gog auth` to set up OAuth for Gmail access.
- Environment: Go programming language for building the CLI.

## Commands

Use `gog gmail --help` for full Gmail subcommands. Key commands related to drafts and searching:

- **List drafts**: `gog gmail drafts list`  
  Retrieves a list of all drafts in your Gmail account.

- **Create a draft**: `gog gmail drafts create --to <recipient> --subject "<subject>" --body "<body>"`  
  Example: `gog gmail drafts create --to example@email.com --subject "Meeting Notes" --body "Draft content here."`

- **Update a draft**: `gog gmail drafts update <draftId> --to <recipient> --subject "<subject>" --body "<body>"`  
  Example: `gog gmail drafts update 123456789 --subject "Updated Subject" --body "New body text."`

- **Search emails (including drafts)**: `gog gmail search '<query>' --max <number> --json`  
  Use Gmail operators like `is:draft` to search drafts.  
  Example: `gog gmail search 'is:draft meeting' --max 10` (searches drafts containing "meeting").  
  Pipe to `jq` for parsing: `gog gmail search 'is:draft' --json | jq`.

## Examples

1. List all drafts:  
   ```
   gog gmail drafts list
   ```

2. Create a simple draft:  
   ```
   gog gmail drafts create --subject "Test Draft" --body "This is a test."
   ```

3. Search for drafts newer than 7 days:  
   ```
   gog gmail search 'is:draft newer_than:7d' --max 20
   ```

4. Get details of a thread (useful after searching):  
   ```
   gog gmail thread get <threadId> --download  # Downloads attachments if any
   ```

## Notes

- Output is JSON-first for easy integration into scripts.
- Supports multiple Google accounts via `GOG_ACCOUNT=<email>`.
- For full email search (not just drafts), omit `is:draft` in the query.
- No direct "search" subcommand under `drafts`; use the general `search` with operators for filtering drafts.

For more details, refer to the gogcli documentation on GitHub.

## Command Help
```
gog gmail drafts --help
Usage: gog gmail (mail,email) drafts (draft) <command>
Build: v0.11.0 (91c4c15)

Draft operations

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

Write
  list (ls) [flags]
    List drafts

  get (info,show) <draftId> [flags]
    Get draft details

  delete (rm,del,remove) <draftId>
    Delete a draft

  send (post) <draftId>
    Send a draft

  create (add,new) [flags]
    Create a draft

  update (edit,set) <draftId> [flags]
    Update a draft
```