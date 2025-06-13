# GitHub Copilot Instruction Files (VS Code)

Quick reference for GitHub Copilot instruction file commands, syntax, and best practices for managing multiple instruction files when using GitHub Copilot in VS Code.

## Important: VS Code vs GitHub Web Interface

This guide covers **VS Code's instruction system** which supports `applyTo` patterns. If you're using GitHub Copilot in the web interface, only basic `.github/copilot-instructions.md` (without targeting) is supported.

## Basic Structure

Create `.github/copilot-instructions.md` in your repository root with natural language instructions:

```markdown
We use TypeScript for all new code.
Always include error handling in functions.
Follow React hooks rules - no conditional hooks.
Use functional components over class components.
```

## File Header (Optional)

Use YAML front matter to specify which files the instructions apply to:

```markdown
---
applyTo: "**/*.ts,**/*.tsx"
---

# TypeScript Instructions
Use strict typing and interfaces for all data structures.
```

## How Multiple Instruction Files Work

### Copilot's Behavior
- **Aggregates All Matching Files**: Reads every instruction file where `applyTo` pattern matches the current file
- **Combines Instructions**: Merges guidance from all applicable files (no "first wins" rule)
- **Context-Aware**: Applies the most relevant instructions for the current task

### Managing Multiple Files
```
.github/
├── copilot-instructions.md          # Main instructions (applies to all files)
└── instructions/
    ├── code-review.instructions.md   # applyTo: "**/*.py,**/*.js"
    ├── testing.instructions.md       # applyTo: "**/test_*.py"
    ├── commit.instructions.md        # No applyTo (manual reference)
    └── pr.instructions.md            # No applyTo (manual reference)
```

## Common applyTo Patterns

### File Type Targeting
```markdown
---
applyTo: "**"                    # All files (use sparingly)
applyTo: "**/*.js,**/*.ts"      # JavaScript/TypeScript files  
applyTo: "**/*.py"              # Python files only
applyTo: "**/*.md"              # Markdown files only
---
```

### Directory Targeting
```markdown
---
applyTo: "src/**"               # Files in src directory
applyTo: "tests/**"             # Files in tests directory
applyTo: "docs/**"              # Documentation files
---
```

### Specific Patterns
```markdown
---
applyTo: "**/test_*.py,**/*_test.py"    # Test files
applyTo: "**/*.config.js,**/*.json"     # Configuration files
applyTo: "Dockerfile*,**/*.yml"         # Infrastructure files
---
```

## Best Practices for Multiple Instructions

### 1. Use Hierarchical Structure
```markdown
# Main copilot-instructions.md (no applyTo = applies everywhere)
General project guidelines and role definitions.

# Specialized instruction files with targeted applyTo patterns
- Code review standards for specific file types
- Testing guidelines for test files only
- Build/deploy instructions for config files
```

### 2. Avoid `applyTo: "**"` Conflicts
```markdown
# ❌ Bad: Multiple files with applyTo: "**" 
commit.instructions.md     # applyTo: "**"
pr.instructions.md         # applyTo: "**" 
# Result: Every file gets both commit AND PR instructions

# ✅ Good: Targeted application
code-review.instructions.md # applyTo: "**/*.py"
testing.instructions.md     # applyTo: "**/test_*.py"
commit.instructions.md      # No applyTo (reference manually)
```

### 3. Manual vs Automatic Application
```markdown
# Automatic (with applyTo patterns)
- Code quality standards
- File-type specific conventions
- Testing requirements

# Manual Reference (no applyTo)
- Commit message formats
- Pull request templates
- Deployment procedures
```

## Referencing Other Instruction Files

### In Main Instructions
```markdown
## Quick Reference: When to Use Specialized Instructions

- **Code Reviews**: Use [code-review.instructions.md](.github/instructions/code-review.instructions.md) for quality standards
- **Testing**: Use [testing.instructions.md](.github/instructions/testing.instructions.md) for test generation
- **Commits**: Apply [commit.instructions.md](.github/instructions/commit.instructions.md) for version control

Apply the [code quality guidelines](.github/instructions/code-review.instructions.md) to all Python files.
Apply the [testing standards](.github/instructions/testing.instructions.md) for comprehensive testing.
```

### Cross-File References
```markdown
# In specialized instruction file
Follow the [general coding guidelines](../.github/copilot-instructions.md) for overall project standards.

For commit messages, use the format defined in [commit.instructions.md](.github/instructions/commit.instructions.md).
```

## VS Code Instructions (Separate Feature)

In VS Code, you can also create `.instructions.md` files anywhere in your workspace:

```markdown
---
applyTo: "**/*.py"
---

# Python Instructions  
Use type hints for all function parameters.
Follow PEP 8 style guidelines.
```

## Troubleshooting Common Issues

### Issue: Too Many Instructions Applied
**Problem**: Every file gets instructions from multiple sources
**Solution**: Use more specific `applyTo` patterns or remove `applyTo` for context-specific instructions

### Issue: Instructions Not Applied
**Problem**: `applyTo` pattern doesn't match file types
**Solution**: Check pattern syntax and test with actual file paths

### Issue: Conflicting Instructions
**Problem**: Different instruction files give contradictory guidance
**Solution**: Establish clear hierarchy and remove duplicated instructions

## Example: Complete Instruction Architecture

```markdown
# .github/copilot-instructions.md (Main - no applyTo)
You are a TaskProcessor focused on implementation tasks.

## Quick Reference
- Code Reviews: Use [code-review.instructions.md](.github/instructions/code-review.instructions.md)
- Testing: Use [testing.instructions.md](.github/instructions/testing.instructions.md)
- Commits: Use [commit.instructions.md](.github/instructions/commit.instructions.md) (manual)

# .github/instructions/code-review.instructions.md
---
applyTo: "**/*.py,**/*.js,**/*.ts"
---
Code quality standards for source files.

# .github/instructions/testing.instructions.md  
---
applyTo: "**/test_*.py,**/*_test.py,**/tests/**"
---
Testing guidelines for test files.

# .github/instructions/commit.instructions.md (no applyTo)
Conventional commit format (referenced manually).
```

## Best Practices Summary

- **Main instruction file**: General guidance, no `applyTo` (applies everywhere)
- **Specialized files**: Targeted `applyTo` patterns for specific file types
- **Context-specific files**: No `applyTo`, referenced manually when needed
- **Clear hierarchy**: Each instruction file has a specific, non-overlapping purpose
- **Cross-references**: Link between instruction files for comprehensive guidance

Focus on creating a clean instruction architecture that provides relevant guidance without noise or conflicts.

