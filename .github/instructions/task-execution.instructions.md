---
applyTo: "**/docs/TASKS.md,**/TASKS.md"
---

# Task Execution Instructions for Mnemosyne Interview Preparation System

**Version**: 1.0 | **Framework**: Implementation-Focused | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## 🚀 Quick Reference (Match Conversation Types)

### Task Execution Decision Matrix (No Maybe Now Principle)

| Task Type | Conversation Match | Action | Complexity | Time |
|-----------|-------------------|--------|------------|------|
| **Environment setup** | Technical | Never assess | Direct execution | 5-15 min |
| **Content creation** | Educational | Maybe assess | Content validation | 15-45 min |
| **System integration** | Technical-Complex | Always assess | Full dependency check | 30-90 min |
| **Testing/validation** | Quality-Focused | Always assess | Complete verification | 20-60 min |

### Task Authority Hierarchy (Trust But Verify)
```
1. docs/planning/TASKS.md        # Implementation roadmap authority
2. User explicit approval        # Permission gate for next sub-task  
3. Technical validation          # Functional verification authority
4. Documentation updates         # Progress tracking authority
5. docs/guides/DIRECTORY_STRUCTURE.md # Directory organization authority
```

### Never Rules (Hard Never - Sparingly Used)
- **NEVER** mark a sub-task `[x]` without user approval and functional validation
- **NEVER** proceed to next sub-task without explicit user permission ("yes", "y", "continue")
- **NEVER** modify docs/planning/TASKS.md without updating "Relevant Files" section
- **NEVER** skip acceptance criteria validation for any sub-task
- **NEVER** create files outside the established directory structure without justification

---

## 📋 Task Processing Protocol (Scaling Effort)

### Implementation Readiness Assessment
**Use this checklist before starting any sub-task:**

1. **Dependencies Satisfied**: All prerequisite tasks marked `[x]`
2. **Requirements Clear**: Acceptance criteria understood and achievable
3. **Resources Available**: Tools, access, and time allocated
4. **Validation Plan**: Clear success criteria and testing approach

### Effort Classification (Good and Bad Examples)

#### ✅ EXCELLENT Task Execution
```markdown
**Task 1.1: Prepare WSL Python Environment** ✅
- Implementation: Created virtual environment `interview_prep_env`
- Validation: Python 3.9.16 confirmed, pip 23.1.2 updated
- Files: `/home/user/.venv/interview_prep_env/` (new environment)
- Next: Ready for Task 1.2 (X11 GUI configuration)
- Permission: Awaiting user approval to proceed
```

#### ❌ POOR Task Execution (Never Do This)
```markdown
- Environment ready ❌ (No specific implementation details)
- Python works ❌ (No version confirmation or validation)
- Next task ❌ (No user permission requested)
```

### Simple Task Execution (1-3 implementation steps)
**Scope**: Single component setup, configuration changes
**Example**: Install package, create directory, set environment variable
**Protocol**:
1. Execute implementation directly
2. Validate against acceptance criteria
3. Update TASKS.md with `[x]` marking
4. Request user permission for next sub-task

### Medium Task Execution (3-7 implementation steps)  
**Scope**: Multi-step processes with dependencies
**Example**: Configure GUI forwarding, create content templates
**Protocol**:
1. Provide implementation approach overview
2. Execute step-by-step with intermediate validation
3. Comprehensive acceptance criteria verification
4. Update relevant files documentation
5. Request user permission with detailed completion summary

### Complex Task Execution (7-15 implementation steps)
**Scope**: System-wide integration, extensive content creation
**Example**: Create 60+ flashcards, implement complete backup system
**Protocol**:
1. **Always assess first**: Provide detailed execution plan
2. Break into logical sub-phases with checkpoints
3. Validate each phase before proceeding
4. Comprehensive testing and integration verification
5. Full documentation update with impact analysis
6. Detailed completion report and permission request

---

## 🔄 Task List Maintenance Standards

### Completion Marking Protocol (Trust But Verify)

#### Sub-task Completion Requirements
- [ ] **Functional Validation**: Implementation meets acceptance criteria
- [ ] **User Approval**: Explicit permission received for completion marking
- [ ] **Documentation Update**: Relevant Files section updated
- [ ] **Next Task Ready**: Clear path to next sub-task identified

#### Parent Task Completion Rules
```markdown
# Only mark parent task [x] when ALL sub-tasks are [x]
- [x] 1.1 Prepare WSL Python Environment
- [x] 1.2 Configure X11 GUI Forwarding  
- [x] 1.3 Install Mnemosyne and Dependencies
- [x] 1.4 Verify Complete Installation
- [x] **1. Environment Setup & Configuration** ← Mark only after all above complete
```

#### File Tracking Standards
```markdown
## Relevant Files
- `src/core/config.py` (new): Application configuration management
- `src/database/db_utility.py` (modified): Database utility functions
- `config/app_config.yaml` (new): Application configuration file
- `data/databases/interview_prep_main.db` (new): Main production database
- `content/stage1_data_manipulation/pandas_operations.md` (new): pandas flashcard content
- `scripts/setup_environment.py` (new): Environment setup automation
- `tests/test_spaced_repetition.py` (new): Spaced repetition algorithm tests
```

**Directory Path Guidelines:**
- **Source Code**: Use `src/` prefix for all Python modules and packages
- **Content**: Use `content/stage[N]_[name]/` for interview stage content
- **Configuration**: Use `config/` for all configuration files
- **Data**: Use `data/databases/` for databases, `data/backups/` for backups
- **Documentation**: Use `docs/guides/` for user guides, `docs/planning/` for project docs
- **Scripts**: Use `scripts/` for utility and automation scripts
- **Tests**: Use `tests/` for all test files and fixtures

---

## 🎯 Mnemosyne-Specific Task Guidelines

### Environment Setup Tasks (Stage 1)
- **Focus**: WSL compatibility and GUI forwarding
- **Validation**: Mnemosyne GUI launches successfully
- **Success Metrics**: <10 second startup time, responsive interface

### Content Creation Tasks (Stage 3-4)
- **Focus**: Educational quality and interview relevance  
- **Validation**: Technical accuracy, proper tagging, spaced repetition optimization
- **Success Metrics**: 180+ cards total, 85%+ retention rate potential

### System Integration Tasks (Stage 2, 4-5)
- **Focus**: Backup systems, performance optimization
- **Validation**: Database integrity, backup verification, performance benchmarks
- **Success Metrics**: <500ms card rendering, daily backup automation

---

## 🚧 Quality Assurance Checkpoints

### Before Starting Any Sub-task
```markdown
**Pre-Execution Checklist:**
- [ ] Dependencies from previous sub-tasks satisfied
- [ ] Acceptance criteria clearly understood
- [ ] Implementation approach identified
- [ ] Validation method planned
- [ ] Time estimate reasonable (no >2 hour single sub-tasks)
```

### After Completing Any Sub-task
```markdown
**Post-Execution Validation:**
- [ ] All acceptance criteria met and tested
- [ ] Implementation follows WSL best practices
- [ ] No breaking changes to existing functionality
- [ ] Documentation updated (Relevant Files section)
- [ ] User permission requested before marking [x]
```

### Cross-Task Integration Validation
```markdown
**Integration Checkpoints:**
- [ ] New components integrate with existing system
- [ ] No configuration conflicts introduced
- [ ] Performance impact within acceptable bounds
- [ ] Backup and recovery procedures still functional
```

---

## 🔧 Implementation Standards

### Directory Structure Compliance

All task implementations must follow the established directory structure as defined in `docs/guides/DIRECTORY_STRUCTURE.md`. 

**File Placement Guidelines:**
- **Python Source Code**: All `.py` files go in `src/` with appropriate package structure
- **Configuration Files**: Use `config/` for YAML, JSON, and other config files
- **Database Files**: Production databases in `data/databases/`, backups in `data/backups/`
- **Content Files**: Interview content in `content/stage[N]_[name]/` directories
- **Test Files**: All test files in `tests/` with appropriate naming conventions
- **Documentation**: User guides in `docs/guides/`, planning docs in `docs/planning/`
- **Scripts**: Utility scripts in `scripts/`, maintenance scripts in `scripts/maintenance/`
- **Media Assets**: Images and diagrams in `media/` with appropriate subdirectories

**Import Path Standards:**
```python
# Correct import paths following new structure
from src.core.config import ApplicationConfig
from src.database.db_utility import DatabaseManager
from src.content.content_processor import ContentProcessor

# Update any legacy imports when moving files
# Old: from db_utility import DatabaseManager
# New: from src.database.db_utility import DatabaseManager
```

**File Creation Protocol:**
1. Determine appropriate directory based on file purpose
2. Create file in correct location following naming conventions  
3. Update any import statements to use new paths
4. Add file to "Relevant Files" section with descriptive purpose
5. Validate that file location aligns with project architecture

### WSL Terminal Output Instructions

When working with WSL (Windows Subsystem for Linux), always carefully read and acknowledge ALL terminal output, including:

- Success messages (like "SUCCESS: X11 GUI test completed")
- Error messages and stack traces
- Status indicators and confirmation text
- Multi-line command continuations (lines starting with `>`)

**Key behaviors:**
1. **Read the complete output** - Don't assume silence means failure
2. **Acknowledge what you see** - Quote the actual output text in your response
3. **Check exit codes** - Use `echo $?` after commands to verify success (0 = success)
4. **Wait for completion** - Let long-running commands finish before concluding

**Example response format:**
"I can see the command executed successfully. The output shows: `SUCCESS: X11 GUI test completed`, which confirms the test passed."

**Common WSL pitfalls to avoid:**
- Assuming no visible output means failure
- Missing success messages in multi-line outputs
- Not recognizing when GUI applications run headlessly but successfully

### Tool Priority for Mnemosyne Tasks
1. **Direct WSL commands**: Native Linux environment operations
2. **Python virtual environment**: Isolated dependency management  
3. **Source code modules**: Use `src/` package structure for all Python code
4. **Configuration files**: Use `config/` directory for all settings
5. **Database operations**: Use `src/database/` modules for data persistence
6. **Content management**: Use `content/` directory structure for interview materials
7. **Mnemosyne CLI/API**: Application-specific operations
8. **GUI validation**: Visual confirmation of functionality

### Error Handling Protocol
```markdown
**When Implementation Fails:**
1. Document specific error messages and context
2. Attempt standard troubleshooting (restart, re-install, permissions)
3. Research WSL-specific solutions if applicable
4. Escalate to user with problem description and proposed alternatives
5. **Never** mark task complete if core functionality fails
```

### Performance Standards
- **Environment Setup**: Complete in <30 minutes total
- **Content Creation**: >10 cards per hour average
- **System Response**: GUI operations <2 seconds
- **Backup Operations**: <1 minute for full database export

---

## 📊 Progress Tracking Requirements

### Communication Protocol
- **After Each Sub-task**: Brief completion summary with validation results
- **After Each Parent Task**: Comprehensive progress report with files modified
- **On Blocking Issues**: Immediate escalation with detailed problem description
- **Permission Requests**: Clear "ready to proceed" statements requiring explicit approval

### Status Update Template
```markdown
**Task X.Y Status Update:**
- **Completed**: [Specific implementation description]
- **Validated**: [Acceptance criteria verification method and results]  
- **Files Modified**: [List with one-line descriptions]
- **Next Action**: [Clear description of next sub-task]
- **Permission**: Awaiting user approval to proceed with Task X.Y+1
```

### Documentation Maintenance
- **Real-time Updates**: Modify `docs/planning/TASKS.md` immediately after each sub-task completion
- **File Tracking**: Maintain accurate "Relevant Files" section using proper directory paths
- **Progress Preservation**: Ensure all progress is documented for session continuity
- **Completion Verification**: Double-check parent task completion status after each sub-task
- **Directory Compliance**: Verify all created files follow `docs/guides/DIRECTORY_STRUCTURE.md` standards

---

## 🎓 Educational Content Quality Standards

### Flashcard Creation Requirements (Tasks 3.1-3.4)
- **Technical Accuracy**: All code examples execute correctly in target environment
- **Interview Relevance**: Content directly applicable to Skyscanner Senior Engineer role
- **Spaced Repetition Optimization**: Appropriate difficulty progression and review intervals
- **Multimedia Integration**: LaTeX for math, syntax highlighting for code

### Content Validation Checklist
```markdown
**Per Content Creation Sub-task:**
- [ ] Required card count achieved (specified in acceptance criteria)
- [ ] All code examples tested and functional
- [ ] Proper hierarchical tagging applied (Stage → Topic → Complexity)
- [ ] Content stored in correct `content/stage[N]_[name]/` directory
- [ ] Content aligns with interview stage objectives
- [ ] Quality review completed for accuracy and clarity
- [ ] Files follow naming conventions from `docs/guides/DIRECTORY_STRUCTURE.md`
```

---

## 🚀 Success Criteria

Effective task execution should demonstrate:
- ✅ **Systematic Progress**: Each sub-task builds on previous completed work
- ✅ **Quality Validation**: All implementations meet acceptance criteria before completion
- ✅ **Clear Communication**: User always informed of status and next actions
- ✅ **Documentation Integrity**: TASKS.md accurately reflects current system state
- ✅ **User Control**: Explicit permission required for all forward progress

**Task Execution Mission**: Transform the comprehensive Mnemosyne interview preparation plan into a fully functional system through systematic, validated, user-approved implementation of individual sub-tasks while maintaining quality standards and educational effectiveness.

---

## 📝 Example Task Execution Flow

### Ideal Sub-task Processing Example
```markdown
**Starting Task 2.1: Design Hierarchical Tag System**

**Pre-Execution Assessment:**
- Dependencies: Directory structure established ✅
- Requirements: Three-tier tag structure, documentation ✅
- Approach: Create YAML config, implement validation logic ✅

**Implementation:**
[Execution details with commands and outputs]

**Validation:**
- Tag hierarchy supports Stage → Topic → Complexity ✅
- Configuration file properly structured ✅  
- Validation logic handles edge cases ✅
- Documentation clearly explains usage ✅

**Files Modified:**
- `config/tag_hierarchy.yaml` (new): Hierarchical tag system configuration
- `src/content/tag_hierarchy.py` (new): Tag validation and management logic
- `docs/guides/CONTENT_CREATION.md` (new): Tag usage guidelines for content creators
- `tests/test_tag_hierarchy.py` (new): Comprehensive tag system validation tests

**Completion:**
Task 2.1 meets all acceptance criteria and follows established directory structure.

**Permission Request:**
Ready to mark Task 2.1 as complete [x] and proceed to Task 2.2: Create Card Templates. 
Please confirm with "yes" or "y" to proceed.
```

### Directory Structure Compliance Example
```markdown
**Files Created Following Structure Guidelines:**
- `src/content/tag_hierarchy.py` ✅ (Source code in appropriate package)
- `config/tag_hierarchy.yaml` ✅ (Configuration in config directory)
- `docs/guides/CONTENT_CREATION.md` ✅ (User guide in guides directory)
- `tests/test_tag_hierarchy.py` ✅ (Tests in tests directory)

**Import Path Updates:**
```python
# New structured imports
from src.content.tag_hierarchy import TagManager
from config import load_yaml_config

# Updated from legacy paths
# Old: from tag_utils import TagManager
# New: from src.content.tag_hierarchy import TagManager
```
```

This comprehensive task execution framework ensures systematic, quality-focused implementation while maintaining user control and educational effectiveness throughout the Mnemosyne interview preparation system development.
