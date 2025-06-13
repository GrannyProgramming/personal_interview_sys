# Pull Request Description Instructions

Generate comprehensive, standardized PR descriptions that facilitate effective code review and project tracking.

## Standard PR Template

```markdown
## 🎯 Purpose
Brief summary of what this PR accomplishes and why it's needed.

## 📋 Changes
### Added
- New functionality or features

### Changed  
- Modified existing functionality

### Fixed
- Bug fixes and issue resolutions

### Removed
- Deprecated or removed functionality

## 🧪 Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Cross-platform compatibility verified

## 📚 Documentation
- [ ] README updated (if needed)
- [ ] Code comments added
- [ ] API documentation updated

## 🚨 Breaking Changes
List any breaking changes and migration steps (if applicable)

##  Related Issues
Closes #X, Fixes #Y, Relates to #Z

## 📝 Review Notes
Specific areas requiring attention or context for reviewers
```

## Project-Specific Sections

### For Educational Content Changes
```markdown
## 📖 Content Changes
- **Stage**: Which interview preparation stage
- **Card Count**: Number of flashcards affected
- **Topics**: Specific topics covered
- **Difficulty**: Beginner/Intermediate/Advanced distribution
```

### For Technical Changes
```markdown
## 🔧 Technical Impact
- **Components**: Which system components are affected
- **Database**: Schema changes or data migrations
- **Performance**: Expected impact on system performance
- **WSL Compatibility**: Cross-platform considerations
```

### For Bug Fixes
```markdown
## � Issue Resolution
- **Problem**: Clear description of the issue
- **Root Cause**: What caused the problem
- **Solution**: How the fix addresses the issue
- **Testing**: Verification steps taken
```

## Quality Standards

### Good PR Descriptions
- Clear, specific purpose statement
- Detailed change breakdown by category
- Comprehensive testing checklist
- Proper issue linking
- Context for reviewers

### Avoid
- Vague descriptions like "update stuff"
- Missing testing information
- No issue references
- Unclear change impacts

## Templates for Common Changes

### Feature Addition
```markdown
## 🎯 Purpose
Add [feature name] to improve [specific benefit]

## � Changes
### Added
- [Specific functionality implemented]
- [New tests for coverage]
- [Documentation updates]

## 🧪 Testing
- [x] Unit tests with X% coverage
- [x] Integration tests pass
- [x] Manual testing scenarios completed
```

### Bug Fix
```markdown
## 🎯 Purpose
Fix [specific issue] that was causing [problem description]

## 📋 Changes
### Fixed
- [Root cause resolution]
- [Error handling improvements]
- [Test cases for regression prevention]

## 🧪 Testing
- [x] Reproducer test case added
- [x] Fix verified across environments
- [x] No regression in related functionality
```

### Content Update
```markdown
## 🎯 Purpose
Update [content area] with [number] new flashcards for [interview stage]

## 📖 Content Changes
- **Stage**: [Stage number and focus area]
- **Card Count**: [X new, Y updated cards]
- **Topics**: [List of specific topics covered]
- **Quality**: [Review and validation completed]
```

## Review Assignment Guidelines

### Complex Changes
- Assign multiple reviewers for architectural changes
- Include domain experts for content updates
- Add security review for data handling changes

### Simple Changes
- Single reviewer for documentation updates
- Automated checks for formatting changes
- Self-review for minor bug fixes

Focus on creating PR descriptions that provide complete context for effective code review while maintaining consistency across the project.
