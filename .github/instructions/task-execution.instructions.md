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
1. TASKS.md               # Implementation roadmap authority
2. User explicit approval # Permission gate for next sub-task  
3. Technical validation   # Functional verification authority
4. Documentation updates  # Progress tracking authority
```

### Never Rules (Hard Never - Sparingly Used)
- **NEVER** mark a sub-task `[x]` without user approval and functional validation
- **NEVER** proceed to next sub-task without explicit user permission ("yes", "y", "continue")
- **NEVER** modify TASKS.md without updating "Relevant Files" section
- **NEVER** skip acceptance criteria validation for any sub-task

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
- `/home/user/.venv/interview_prep_env/` (new): Python virtual environment with interview dependencies
- `/home/user/.bashrc` (modified): Added DISPLAY variable and venv activation
- `requirements.txt` (new): Locked dependency versions for reproducible setup
- `setup_validation.py` (new): Environment verification script
```

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

### Tool Priority for Mnemosyne Tasks
1. **Direct WSL commands**: Native Linux environment operations
2. **Python virtual environment**: Isolated dependency management
3. **Mnemosyne CLI/API**: Application-specific operations
4. **GUI validation**: Visual confirmation of functionality

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
- **Real-time Updates**: Modify TASKS.md immediately after each sub-task completion
- **File Tracking**: Maintain accurate "Relevant Files" section throughout implementation
- **Progress Preservation**: Ensure all progress is documented for session continuity
- **Completion Verification**: Double-check parent task completion status after each sub-task

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
- [ ] Content aligns with interview stage objectives
- [ ] Quality review completed for accuracy and clarity
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
**Starting Task 1.1: Prepare WSL Python Environment**

**Pre-Execution Assessment:**
- Dependencies: WSL2 environment available ✅
- Requirements: Python 3.9+, virtual environment, pip update ✅
- Approach: Use python -m venv, activate, upgrade pip ✅

**Implementation:**
[Execution details with commands and outputs]

**Validation:**
- Python version: 3.9.16 ✅
- Virtual environment: Active and isolated ✅  
- Pip version: 23.1.2 (latest) ✅
- Environment location: /home/user/.venv/interview_prep_env ✅

**Files Modified:**
- `/home/user/.venv/interview_prep_env/` (new): Python virtual environment
- `/home/user/.bashrc` (modified): Added venv activation alias

**Completion:**
Task 1.1 meets all acceptance criteria and is ready for completion marking.

**Permission Request:**
Ready to mark Task 1.1 as complete [x] and proceed to Task 1.2: Configure X11 GUI Forwarding. 
Please confirm with "yes" or "y" to proceed.
```

This comprehensive task execution framework ensures systematic, quality-focused implementation while maintaining user control and educational effectiveness throughout the Mnemosyne interview preparation system development.
