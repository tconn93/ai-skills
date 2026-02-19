---
name: create-new-skill
description: A skill for creating new skill with the agent
---
# Creating New Skill

## Description

The Creating New Skill allows users to define and implement new skills within a skill management system or framework, such as AI assistants, CLI tools, or automation platforms. This skill focuses on the process of conceptualizing, documenting, and deploying custom skills, often using templates like SKILL.md files. It includes steps for identifying requirements, listing commands or actions, providing examples, and noting best practices.

This skill is useful for developers, AI trainers, or users extending systems like gog CLI or similar tools with new functionalities, ensuring consistency in documentation and implementation.

## Requirements

- Access to a skill framework or platform (e.g., gog CLI, AI agent systems, or Markdown-based documentation).
- Basic knowledge of Markdown formatting for SKILL.md files.
- Optional: Programming environment for implementing skill logic (e.g., Go for gogcli extensions).
- Authentication or setup for the target system (e.g., OAuth for Google services if extending gog).

## Commands

Since this is a meta-skill for creation, it doesn't have specific CLI commands but follows a process. Use analogous commands from tools like git or text editors:

- **Conceptualize**: Define the skill's purpose and scope.  
  Example: Brainstorm features and map to existing APIs.

- **Template Setup**: Create a SKILL.md file using a standard structure.  
  Example: `echo "# New Skill" > SKILL.md` (in bash).

- **Document Commands**: List actions or subcommands with flags and examples.  
  Example: Add sections for each command in Markdown.

- **Implement Logic**: Code the skill if applicable (e.g., add to gogcli source).  
  Example: `go build` for compiling extensions.

- **Test and Deploy**: Validate the skill and integrate it.  
  Example: Run unit tests or simulate usage.

- **Version Control**: Use git for tracking changes.  
  Example: `git add SKILL.md && git commit -m "Add new skill documentation"`.

## Examples

1. Create a basic SKILL.md template:  
   ```
   cat <<EOF > SKILL.md
   # My New Skill

   ## Description
   Brief overview.

   ## Requirements
   List prerequisites.

   ## Commands
   - Command 1 [flags]

   ## Examples
   1. Example usage.

   ## Notes
   Additional info.
   EOF
   ```

2. Extend gog CLI with a new command:  
   Assume adding a "hello" skill. Edit source code, then:  
   ```
   go build gogcli
   ./gog hello --name "World"
   ```

3. Document a new AI skill:  
   For an AI system, define in YAML or JSON, then generate MD:  
   ```
   # In a script or manually
   Skill: creating-new-skill
   Actions: conceptualize, document, implement
   ```

## Notes

- Follow consistent formatting: Use # for title, ## for sections, - for lists, ``` for code blocks.
- Ensure skills are modular and reusable; avoid overlapping with existing ones.
- For gog-like tools, refer to GitHub repos for extension guidelines.
- Test documentation for clarity; include real-world examples.
- If integrating with AI, consider tools like code_execution for validation.
- No JSON output by default; focus on readable Markdown.

For more details, adapt from existing SKILL.md files or consult framework documentation.