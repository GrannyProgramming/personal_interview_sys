# Conventional Commit Instructions

**Version**: 1.0 | **Framework**: Version Control-Focused | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

Follow conventional commit format for clear, consistent commit messages that enable automated changelog generation and semantic versioning.

## Conventional Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types

### Primary Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semi-colons, etc.)
- **refactor**: Code refactoring without functionality changes
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Build system or dependency changes
- **ci**: CI/CD configuration changes
- **chore**: Maintenance tasks

### Project-Specific Types
- **content**: Flashcard content updates
- **study**: Study session or spaced repetition logic
- **backup**: Backup/restore functionality
- **config**: Configuration changes

## Scopes

### Technical Scopes
- **database**: Database operations, schema changes
- **gui**: GUI interface changes
- **wsl**: WSL compatibility fixes
- **deps**: Dependency updates

### Content Scopes
- **stage1**: Data manipulation content
- **stage2**: Culture fit content
- **stage3**: MLOps engineering content
- **stage4**: Work history content

## Examples

### Good Examples
```
feat(study): implement spaced repetition algorithm

fix(wsl): resolve X11 display issues

content(stage3): add MLOps engineering flashcards

docs: update README with installation instructions
```

### Bad Examples
```
update stuff
fix bug
wip
various changes
```

## Breaking Changes

For breaking changes, add `!` after type/scope:
```
feat(database)!: migrate to new schema

BREAKING CHANGE: Database schema updated from v1 to v2
```

## Footer References

Link to issues:
```
Closes #123
Fixes #456
Relates to #789
```
