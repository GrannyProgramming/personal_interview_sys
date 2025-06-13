---
applyTo: "**/*.py,**/*.sh,**/*.yml,**/*.yaml,Dockerfile*,**/requirements*.txt"
---

# Code Review Instructions for Mnemosyne Interview Preparation System

**Version**: 1.0 | **Framework**: Quality-Focused | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## Overview
You are reviewing code for a personal interview preparation system using Mnemosyne flashcards. Focus on Python best practices, WSL compatibility, and educational content quality.

## Core Review Principles

### 1. Match Review Depth to Code Complexity
- **Simple utility functions**: Basic syntax, naming, documentation
- **Core system components**: Architecture, error handling, performance
- **Content management logic**: Data integrity, backup reliability, user experience

### 2. Python-Specific Quality Standards

#### ✅ ALWAYS Check For:
- Virtual environment compatibility (`requirements.txt` updates)
- Type hints for function parameters and returns
- Proper exception handling with specific exception types
- docstrings following Google or NumPy style
- PEP 8 compliance (use `black` formatting)
- Import organization (stdlib, third-party, local)

#### ❌ NEVER Accept:
- Hardcoded file paths (use `pathlib` or `os.path`)
- Bare `except:` clauses without specific exception types
- Global variables for configuration (use config files/classes)
- SQL injection vulnerabilities in database queries
- Missing error handling for file operations

### 3. WSL Environment Considerations

#### Critical Checks:
- Path separators compatible with both Windows and Linux
- File permissions appropriate for WSL file system
- GUI application compatibility (PyQt6/X11 forwarding)
- Environment variable handling for cross-platform support

#### Example Issues to Flag:
```python
# ❌ Bad - Windows-specific path
CONFIG_PATH = "C:\\Users\\Alex\\config.json"

# ✅ Good - Cross-platform path
from pathlib import Path
CONFIG_PATH = Path.home() / ".config" / "interview_prep" / "config.json"
```

### 4. Educational Content Quality

#### For Flashcard Content Management:
- Validate LaTeX syntax before database storage
- Ensure proper HTML escaping for user content
- Check tag hierarchy consistency (Stage → Topic → Complexity)
- Verify backup/restore functionality preserves content integrity

#### For Study Session Logic:
- Spaced repetition algorithm implementation correctness
- Progress tracking accuracy and data persistence
- User preference handling and validation

### 5. Security & Data Protection

#### Required Checks:
- Database connection security (SQLite file permissions)
- Input validation for user-generated content
- Backup file encryption consideration
- No sensitive data in version control

## Review Process

### 1. Initial Assessment (No Maybe Now Principle)
- **Simple changes** (<20 lines): Focus on syntax and basic quality
- **Medium changes** (20-100 lines): Full architecture and integration review
- **Complex changes** (>100 lines): Comprehensive security and performance audit

### 2. Trust But Verify Approach
- Don't automatically approve "trivial" changes
- Verify that tests actually test the claimed functionality
- Check that documentation matches implementation
- Validate that dependencies are necessary and secure

### 3. Scaling Review Effort
- **Low complexity**: Comment on style and basic functionality
- **Medium complexity**: Suggest architectural improvements and edge case handling
- **High complexity**: Require performance testing and comprehensive error handling

## Project-Specific Guidelines

### Interview Preparation Content
- Verify technical accuracy of algorithm explanations
- Check that code examples compile and run correctly
- Ensure behavioral scenario cards follow STAR method format
- Validate that MLOps content reflects current industry practices

### Mnemosyne Integration
- Confirm database schema changes are backward compatible
- Verify spaced repetition interval calculations
- Check that media file handling works across platforms
- Ensure backup procedures don't corrupt study progress

### Performance Considerations
- Database queries should be optimized for 1000+ cards
- GUI responsiveness must be maintained during large imports
- Memory usage should be reasonable for extended study sessions
- Startup time should remain under 10 seconds

## Feedback Format

Use this structure for review comments:

```markdown
## 🔍 Code Quality Review

### ✅ Strengths
- [Specific positive aspects]

### ⚠️ Issues Found
- **[Severity]**: [Issue description]
  - **Location**: [File:line]
  - **Suggestion**: [Specific fix]

### 🚀 Improvement Opportunities
- [Performance/architecture suggestions]

### 📋 Checklist
- [ ] Type hints present
- [ ] Error handling comprehensive
- [ ] Tests cover edge cases
- [ ] Documentation updated
- [ ] WSL compatibility verified
```

## GitHub-Specific Commands

```yaml
# Apply to specific file types
applyTo: "*.py"
applyTo: "requirements.txt"
applyTo: "*.md"

# Exclude generated files
exclude: "*.pyc"
exclude: "__pycache__/"
exclude: ".pytest_cache/"
exclude: "*.db"
exclude: "backups/"
```

## Hard Never Rules

- **NEVER approve** code that could corrupt study progress or flashcard data
- **NEVER accept** hardcoded credentials or API keys
- **NEVER allow** changes that break WSL compatibility without explicit approval
- **NEVER merge** code that doesn't handle file system errors gracefully

## Success Criteria

A successful code review should result in:
- ✅ Code that runs reliably in WSL environment
- ✅ Proper error handling for all file operations
- ✅ Educational content that enhances interview preparation
- ✅ Maintainable architecture that supports future expansion
- ✅ Comprehensive test coverage for critical functionality

Focus on helping create a robust, reliable interview preparation system that maximizes learning effectiveness while maintaining technical excellence.
