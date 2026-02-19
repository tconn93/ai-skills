---
name: google-docs-management
description: A skill to manage google docs using the gogcli app.
---
# Docs Management Skill

## Description

The Docs Management skill enables users to interact with Google Docs using the `gog` CLI tool, part of the gogcli Google Suite CLI. This skill covers operations such as exporting, creating, copying, reading, writing, inserting, deleting, finding and replacing text, updating content, managing comments, and listing tabs in Google Docs. It supports JSON output for scripting and automation where applicable.

This skill is ideal for command-line management of Google Docs, including content manipulation and metadata retrieval.

## Requirements

- Install gogcli: Clone and build from [GitHub repository](https://github.com/steipete/gogcli).
- Authenticate with Google: Run `gog auth` to set up OAuth for Docs access.
- Environment: Go programming language for building the CLI.
- Optional: Use `--json` flag on supported commands for structured output.

## Commands

Use `gog docs --help` for full Docs subcommands. Below is a detailed list of supported commands:

- **export (download,dl) <docId> [flags]**: Export a Google Doc (pdf|docx|txt).  
  Flags: `--format <pdf|docx|txt>`, `--output <path>`.  
  Example: `gog docs export 1aBcDeFgHiJkLmNoPqRsTuVwXyZ --format pdf --output local_doc.pdf`.

- **info (get,show) <docId>**: Get Google Doc metadata.  
  Outputs details like title, revision ID, and last modified time.  
  Example: `gog docs info 1aBcDeFgHiJkLmNoPqRsTuVwXyZ`.

- **create (add,new) {title} [flags]**: Create a Google Doc.  
  Flags: `--folder <folderId>`, `--json`.  
  Example: `gog docs create "New Document" --folder 0aBcDeFgHiJk`.

- **copy (cp,duplicate) <docId> {title} [flags]**: Copy a Google Doc.  
  Flags: `--folder <folderId>`.  
  Example: `gog docs copy 1aBcDeFgHiJkLmNoPqRsTuVwXyZ "Copy of Doc" --folder 0newFolderId`.

- **cat (text,read) <docId> [flags]**: Print a Google Doc as plain text.  
  Flags: `--json`.  
  Example: `gog docs cat 1aBcDeFgHiJkLmNoPqRsTuVwXyZ`.

- **comments <command>**: Manage comments on a Google Doc.  
  Subcommands: `list <docId>`, `create <docId> --text "<comment>"`, `delete <docId> <commentId>`.  
  Example: `gog docs comments list 1aBcDeFgHiJkLmNoPqRsTuVwXyZ`.

- **list-tabs <docId>**: List all tabs in a Google Doc.  
  Example: `gog docs list-tabs 1aBcDeFgHiJkLmNoPqRsTuVwXyZ`.

- **write <docId> [<content>] [flags]**: Write content to a Google Doc.  
  Flags: `--append`, `--json`.  
  Example: `gog docs write 1aBcDeFgHiJkLmNoPqRsTuVwXyZ "New content to add." --append`.

- **insert <docId> [<content>] [flags]**: Insert text at a specific position.  
  Flags: `--index <position>`, `--json`.  
  Example: `gog docs insert 1aBcDeFgHiJkLmNoPqRsTuVwXyZ "Inserted text." --index 0`.

- **delete --start=INT-64 --end=INT-64 <docId>**: Delete text range from document.  
  Example: `gog docs delete --start=10 --end=20 1aBcDeFgHiJkLmNoPqRsTuVwXyZ`.

- **find-replace <docId> <find> <replace> [flags]**: Find and replace text in document.  
  Flags: `--match-case`, `--json`.  
  Example: `gog docs find-replace 1aBcDeFgHiJkLmNoPqRsTuVwXyZ "old text" "new text" --match-case`.

- **update <docId> [flags]**: Update content in a Google Doc.  
  Flags: `--content "<newContent>"`, `--json`.  
  Example: `gog docs update 1aBcDeFgHiJkLmNoPqRsTuVwXyZ --content "Updated full content."`.

## Examples

1. Create and export a doc:  
   ```
   gog docs create "Test Doc"
   gog docs export $(gog docs info "Test Doc" | jq -r '.documentId') --format txt
   ```

2. Read and modify content:  
   ```
   gog docs cat 1docId
   gog docs insert 1docId "New intro." --index 0
   gog docs find-replace 1docId "typo" "correction"
   ```

3. Manage comments:  
   ```
   gog docs comments create 1docId --text "Check this paragraph."
   gog docs comments list 1docId
   gog docs comments delete 1docId 123commentId
   ```

4. Delete and update range:  
   ```
   gog docs delete --start=5 --end=15 1docId
   gog docs update 1docId --content "Revised document text."
   ```

5. Copy and list tabs:  
   ```
   gog docs copy 1originalId "Copied Doc"
   gog docs list-tabs 1copiedId
   ```

## Notes

- Most commands support `--json` for parseable output; pipe to `jq` for processing (e.g., `gog docs info 1docId --json | jq '.title'`).
- Doc IDs can be obtained from Google Drive URLs or via `gog drive search`.
- The `comments` command has subcommands; use `gog docs comments --help` for details.
- Content manipulation commands like `write`, `insert`, `delete`, and `update` use the Docs API for precise edits.
- Supports multiple Google accounts via `GOG_ACCOUNT=<email>`.
- Be cautious with destructive operations like `delete` to avoid data loss.
- For advanced features like batch updates or styling, consider integrating with the full Google Docs API.

For more details, refer to the gogcli documentation on GitHub.