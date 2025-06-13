---
applyTo: "**/docs/**,README.md,**/*.md"
---

# Documentation Standards for Mnemosyne Interview Preparation System

**Version**: 1.0 | **Framework**: Educational-Focused | **Last Updated**: June 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## 🚀 Quick Reference (Match Conversation Types)

### Documentation Decision Matrix (No Maybe Now Principle)

| Task Type | Conversation Match | Action | Complexity | Time |
|-----------|-------------------|--------|------------|------|
| **Fix typos/formatting** | Simple | Direct edit | Never assess | 1-2 min |
| **Add study content** | Educational | Maybe assess | Content validation | 5-10 min |
| **System architecture docs** | Technical | Always assess | Cross-reference impact | 15-30 min |
| **Planning updates** | Complex planning | Always assess | Full impact analysis | 20-45 min |

### File Authority Hierarchy (Trust But Verify)
```
1. PLANNING.md           # Project vision and requirements authority
2. ARCHITECTURE.md       # Technical design decisions authority  
3. REQUIREMENTS.md       # Functional specifications authority
4. README.md            # Getting started and overview authority
5. docs/content/        # Educational content organization authority
6. docs/setup/          # Installation and configuration authority
```

### Never Rules (Hard Never - Sparingly Used)
- **NEVER** duplicate interview content across multiple files (educational integrity)
- **NEVER** create documentation that contradicts WSL compatibility requirements
- **NEVER** document outdated Mnemosyne setup procedures without testing
- **NEVER** mix technical implementation details in educational content files

**Note**: Version headers and project context ARE appropriate for instruction files (`.github/instructions/*.md`) as these are dynamic, evolving system prompts specific to this project.

---

## 📚 Educational Content Standards (Scaling Effort)

### Content Type Classification (Good and Bad Examples)

#### ✅ EXCELLENT Educational Documentation
```markdown
## Stage 1: Data Manipulation - pandas DataFrame Operations

### Learning Objective
Master pandas operations for technical interview scenarios involving data transformation and analysis.

### Core Concepts
- **DataFrame creation**: `pd.DataFrame()`, `pd.read_csv()`
- **Data selection**: `.loc[]`, `.iloc[]`, boolean indexing
- **Transformations**: `.groupby()`, `.pivot_table()`, `.merge()`

### Practice Example
```python
# Interview scenario: Analyze user engagement data
df = pd.read_csv('user_data.csv')
daily_engagement = df.groupby('date')['sessions'].agg(['count', 'mean'])
```

### Self-Check Questions
- Can you explain the difference between `.loc[]` and `.iloc[]`?
- When would you use `.merge()` vs `.join()`?
- How do you handle missing data in groupby operations?
```

#### ❌ POOR Educational Documentation (Never Do This)
```markdown
# pandas stuff ❌ (No clear learning objective)
Use pandas for data things ❌ (Vague, no specific examples)
```

### Content Organization Standards

#### Stage-Based Structure (Interview Preparation Focus)
```markdown
## Stage 1: Data Manipulation (35% study time)
### Topics
- **pandas Operations** (20 cards, 3-4 hours study)
- **SQL Queries** (25 cards, 4-5 hours study)  
- **Data Processing Patterns** (15 cards, 2-3 hours study)

### Difficulty Progression
- **Basic** (30%): Syntax, simple operations
- **Intermediate** (50%): Complex queries, performance considerations
- **Advanced** (20%): Optimization, edge cases, interview tricks
```

#### Cross-Reference Standards
```markdown
# Internal references (educational context)
[Spaced Repetition Guide](docs/study-methods.md#spaced-repetition "Optimizing retention for technical concepts")

# External references (interview-relevant)
[pandas Documentation](https://pandas.pydata.org/docs/ "Official pandas documentation - essential for interviews")

# Stage progression references
[Next: Culture Fit Preparation](docs/content/stage2-culture-fit.md "Behavioral interview preparation")
```

---

## 🔧 Technical Documentation Standards

### Architecture Documentation (Technical Conversation Type)

#### System Design Documents
```markdown
## Mnemosyne WSL Integration Architecture

### Context
Interview preparation requires reliable cross-platform operation in Windows WSL2 environment with GUI support for Mnemosyne flashcard application.

### Technical Requirements
- **Python Environment**: Virtual environment with locked dependencies
- **GUI Support**: X11 forwarding for Mnemosyne interface
- **Data Persistence**: SQLite database with backup automation
- **Performance**: <10s startup, <500ms card rendering

### Implementation Approach
```python
# Environment setup verification
def validate_wsl_setup():
    """Verify WSL environment supports Mnemosyne GUI operation."""
    check_x11_forwarding()
    validate_python_environment()
    test_mnemosyne_startup()
```
```

#### Configuration Documentation
```markdown
## WSL Environment Setup

### Prerequisites Verification
- [ ] WSL2 installed and updated
- [ ] X11 server running (VcXsrv or X410)
- [ ] Python 3.8+ available
- [ ] Display environment variable set

### Installation Steps
1. **Create isolated environment**:
   ```bash
   python -m venv interview_prep_env
   source interview_prep_env/bin/activate
   ```

2. **Install Mnemosyne with dependencies**:
   ```bash
   pip install mnemosyne
   pip install -r requirements.txt
   ```

3. **Verify GUI operation**:
   ```bash
   export DISPLAY=:0
   mnemosyne
   ```
```

---

## 📊 Content Quality Assurance (Trust But Verify)

### Educational Content Validation

#### Content Review Checklist
- [ ] **Technical Accuracy**: All code examples tested and functional
- [ ] **Interview Relevance**: Content directly applicable to target role
- [ ] **Learning Progression**: Appropriate difficulty scaling within topics
- [ ] **Retention Optimization**: Spaced repetition principles applied
- [ ] **Cross-Platform Compatibility**: Examples work in WSL environment

#### Flashcard Quality Standards
```markdown
## Quality Flashcard Template

### Front (Question)
**Context**: Pandas DataFrame manipulation interview question
**Question**: How do you efficiently merge two large DataFrames on multiple columns while handling missing values?

### Back (Answer)
**Solution**:
```python
# Efficient merge with missing value handling
result = pd.merge(
    df1, df2, 
    on=['user_id', 'date'], 
    how='outer',  # Preserve all records
    suffixes=('_left', '_right')
).fillna(method='ffill')  # Forward fill missing values
```

**Key Points**:
- Use `how='outer'` to preserve all records during merge
- `suffixes` parameter handles column name conflicts
- `fillna()` strategies depend on data context
- Consider memory usage for large DataFrames

**Interview Follow-up**: "What's the time complexity of this merge operation?"
```

### Documentation Maintenance Protocol

#### Update Triggers (Scaling Effort)
- **Simple Updates** (2-4 steps): Content corrections, link fixes
- **Medium Updates** (5-9 steps): New flashcard topics, study guide additions  
- **Complex Updates** (10+ steps): Architecture changes, full content reorganization

#### Version Control Standards
```markdown
## Documentation Change Log

### Content Updates
- **2025-06-13**: Added Stage 1 pandas flashcard templates
- **2025-06-13**: Created WSL setup verification procedures
- **2025-06-13**: Established educational content quality standards

### Technical Updates  
- **2025-06-13**: Updated Mnemosyne installation procedures for WSL2
- **2025-06-13**: Added performance benchmarking requirements
- **2025-06-13**: Created backup automation documentation
```

---

## 🎯 Interview-Specific Guidelines

### Stage-Specific Documentation Requirements

#### Stage 1: Data Manipulation
- **Focus**: Technical competency demonstration  
- **Content Type**: Code examples, syntax references, pattern explanations
- **Documentation Style**: Technical reference with practical examples
- **Success Metrics**: Can solve data manipulation problems under interview pressure

#### Stage 2: Culture Fit  
- **Focus**: Behavioral competency and company alignment
- **Content Type**: STAR method scenarios, company value examples
- **Documentation Style**: Narrative-based with structured responses
- **Success Metrics**: Confident storytelling with relevant examples

#### Stage 3: MLOps Engineering
- **Focus**: System design and operational excellence
- **Content Type**: Architecture patterns, monitoring strategies, deployment concepts
- **Documentation Style**: System design documentation with decision rationale
- **Success Metrics**: Can design and defend MLOps solutions

#### Stage 4: Work History
- **Focus**: Technical achievement reflection and growth demonstration
- **Content Type**: Project summaries, technical challenges overcome
- **Documentation Style**: Achievement-oriented with quantifiable impact
- **Success Metrics**: Clear articulation of technical contributions and learning

---

## 🔄 Continuous Improvement Protocol

### Documentation Effectiveness Metrics
- **Content Coverage**: All interview stages adequately documented
- **Usage Analytics**: Which documents are referenced most frequently  
- **Update Frequency**: How often content requires revision
- **User Feedback**: Self-assessment of documentation usefulness

### Quality Evolution Standards
- **Weekly Review**: Content accuracy and relevance validation
- **Bi-weekly Assessment**: Cross-reference integrity and navigation efficiency
- **Monthly Optimization**: Content organization and study workflow improvements
- **Pre-Interview Audit**: Final validation of all documentation accuracy

---

## 🚀 Success Criteria

Effective documentation should:
- ✅ Enable rapid system setup (<4 hours total)
- ✅ Support confident interview performance across all stages
- ✅ Provide clear learning progression and retention tracking
- ✅ Maintain technical accuracy and practical applicability
- ✅ Scale efficiently with additional content and system complexity

**Documentation Mission**: Create actionable, accurate, and educationally effective documentation that directly contributes to interview success while maintaining technical excellence and system reliability.
