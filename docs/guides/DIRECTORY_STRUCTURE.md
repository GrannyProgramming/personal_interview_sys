# Directory Structure - Mnemosyne Interview Preparation System

**Version**: 1.0 | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## 📁 Complete Directory Structure

```
personal_interview_sys/
├── README.md                           # Project overview and quick start guide
├── requirements.txt                    # Python package dependencies
├── .gitignore                         # Git ignore patterns
├── .vscode/                           # VS Code workspace configuration
├── .github/                           # GitHub configuration and prompts
│   ├── copilot-instructions.md       # GitHub Copilot configuration
│   ├── instructions/                 # System instruction files
│   └── prompts/                      # AI prompt templates
│
├── src/                              # Source code organization
│   ├── core/                         # Core application logic
│   │   ├── __init__.py              # Package initialization
│   │   ├── config.py                # Configuration management
│   │   ├── spaced_repetition.py     # SM-2 algorithm implementation
│   │   └── flashcard_manager.py     # Core flashcard operations
│   ├── content/                      # Content management modules
│   │   ├── __init__.py              # Package initialization
│   │   ├── content_processor.py     # Content validation and processing
│   │   ├── tag_hierarchy.py         # Hierarchical tagging system
│   │   └── card_templates.py        # Template management
│   ├── database/                     # Database operations
│   │   ├── __init__.py              # Package initialization
│   │   ├── db_utility.py            # Database utility functions (moved from root)
│   │   ├── schema.py                # Database schema definitions
│   │   └── backup_manager.py        # Backup and recovery operations
│   └── gui/                          # GUI components (if needed)
│       ├── __init__.py              # Package initialization
│       ├── main_window.py           # Main application window
│       └── card_display.py          # Flashcard display widgets
│
├── content/                          # Flashcard content by interview stage
│   ├── stage1_data_manipulation/    # Stage 1: Data manipulation content
│   │   ├── pandas_operations.md     # pandas DataFrame operations
│   │   ├── sql_queries.md           # SQL query patterns and examples
│   │   ├── data_processing.md       # Data cleaning and transformation
│   │   └── practice_problems.md     # Coding practice problems
│   ├── stage2_culture_fit/          # Stage 2: Behavioral and culture fit
│   │   ├── behavioral_scenarios.md  # STAR method scenarios
│   │   ├── company_values.md        # Skyscanner values alignment
│   │   ├── leadership_examples.md   # Leadership and collaboration examples
│   │   └── conflict_resolution.md   # Conflict and challenge scenarios
│   ├── stage3_mlops_engineering/    # Stage 3: MLOps and system design
│   │   ├── ml_pipelines.md          # ML pipeline design and architecture
│   │   ├── monitoring_strategies.md # Model monitoring and observability
│   │   ├── infrastructure.md        # Cloud infrastructure and deployment
│   │   └── system_design.md         # Distributed systems concepts
│   ├── stage4_work_history/         # Stage 4: Work experience reflection
│   │   ├── technical_achievements.md # Major technical contributions
│   │   ├── project_leadership.md    # Project management and leadership
│   │   ├── problem_solving.md       # Complex problem-solving examples
│   │   └── growth_narrative.md      # Professional development journey
│   └── templates/                    # Card creation templates
│       ├── technical_concept.md      # Template for technical concepts
│       ├── behavioral_scenario.md    # Template for behavioral questions
│       ├── code_example.md          # Template for code-based cards
│       └── system_design.md         # Template for architecture cards
│
├── data/                            # Data storage and persistence
│   ├── databases/                   # SQLite databases
│   │   ├── interview_prep_test.db   # Test database (moved from data/)
│   │   ├── interview_prep_main.db   # Main production database
│   │   └── schema_migrations/       # Database schema migration scripts
│   └── backups/                     # Database backups
│       ├── daily/                   # Daily automated backups
│       ├── weekly/                  # Weekly consolidated backups
│       └── pre_interview/           # Pre-interview safety backups
│
├── config/                          # Configuration files
│   ├── app_config.yaml             # Application configuration
│   ├── study_settings.yaml         # Spaced repetition and study settings
│   ├── tag_hierarchy.yaml          # Tag system configuration
│   └── environment_setup.sh        # Environment setup script
│
├── tests/                           # Test files and test data
│   ├── __init__.py                 # Test package initialization
│   ├── test_mnemosyne_complete.py  # Complete system tests (moved from root)
│   ├── test_spaced_repetition.py  # Spaced repetition algorithm tests
│   ├── test_content_processing.py # Content validation tests
│   ├── test_database_operations.py # Database operation tests
│   └── fixtures/                   # Test data and fixtures
│       ├── sample_cards.json       # Sample flashcard data
│       └── test_databases/         # Test database files
│
├── docs/                           # Documentation and guides
│   ├── planning/                   # Project planning documents
│   │   ├── PLANNING.md            # Master planning document (moved from docs/)
│   │   ├── TASKS.md               # Implementation tasks (moved from docs/)
│   │   └── architecture_decisions.md # ADR documentation
│   ├── guides/                    # User and developer guides
│   │   ├── DIRECTORY_STRUCTURE.md # This file - directory organization
│   │   ├── GETTING_STARTED.md    # Quick start guide
│   │   ├── CONTENT_CREATION.md   # Guide for creating flashcard content
│   │   ├── WSL_SETUP_COMPLETE.md # Complete WSL setup guide
│   │   └── STUDY_METHODOLOGY.md  # Spaced repetition study guide
│   ├── instructions/              # System and AI instructions
│   │   └── (future instruction files moved from .github/instructions/)
│   ├── generic/                   # Legacy documentation (preserved)
│   └── research/                  # Research and reference materials
│
├── scripts/                       # Utility and automation scripts
│   ├── verify_installation.py     # Installation verification (moved from root)
│   ├── setup_environment.py       # Automated environment setup
│   ├── backup_database.py         # Database backup automation
│   ├── import_content.py          # Bulk content import utilities
│   ├── export_study_data.py       # Study progress export
│   └── maintenance/               # System maintenance scripts
│       ├── cleanup_old_backups.py # Backup cleanup automation
│       └── database_optimization.py # Database performance optimization
│
└── media/                         # Images, diagrams, and media assets
    ├── diagrams/                  # System architecture diagrams
    │   ├── ml_pipeline_architecture.png
    │   ├── data_flow_diagram.png
    │   └── system_components.png
    ├── screenshots/               # Application screenshots for documentation
    ├── icons/                     # Application icons and UI assets
    └── templates/                 # Media templates for content creation
```

---

## 📋 Directory Purpose and Usage Guidelines

### Source Code Organization (`src/`)

#### `src/core/`
**Purpose**: Core application logic and fundamental algorithms  
**Contents**: Configuration management, spaced repetition algorithms, core flashcard operations  
**Usage**: Import core functionality for application components

#### `src/content/`
**Purpose**: Content management and processing logic  
**Contents**: Content validation, tag hierarchy management, template processing  
**Usage**: Handle flashcard content creation, validation, and organization

#### `src/database/`
**Purpose**: Database operations and data persistence  
**Contents**: Database utilities, schema management, backup operations  
**Usage**: All database interactions should go through these modules

#### `src/gui/`
**Purpose**: GUI components and user interface logic  
**Contents**: Application windows, flashcard display widgets, user interactions  
**Usage**: Desktop application interface components (if needed beyond Mnemosyne)

### Content Organization (`content/`)

#### Stage-Based Directories
- **`stage1_data_manipulation/`**: Technical concepts for data manipulation interviews
- **`stage2_culture_fit/`**: Behavioral scenarios and culture fit preparation  
- **`stage3_mlops_engineering/`**: MLOps and system design concepts
- **`stage4_work_history/`**: Personal experience and achievement reflection

#### `content/templates/`
**Purpose**: Standardized templates for creating consistent flashcard content  
**Usage**: Copy and customize templates for new content creation

### Data Management (`data/`)

#### `data/databases/`
**Purpose**: SQLite database storage with separation of test and production data  
**Usage**: Main application databases, schema migrations

#### `data/backups/`
**Purpose**: Automated backup storage with retention policies  
**Usage**: Daily, weekly, and pre-interview backup storage

### Configuration (`config/`)
**Purpose**: Application settings, study parameters, and environment configuration  
**Usage**: Centralized configuration management for all application components

### Testing (`tests/`)
**Purpose**: Comprehensive test suite with test data and fixtures  
**Usage**: Unit tests, integration tests, and system validation

### Documentation (`docs/`)

#### `docs/planning/`
**Purpose**: Project planning, task management, and architectural decisions  
**Usage**: Project management and development planning

#### `docs/guides/`
**Purpose**: User guides, setup instructions, and best practices  
**Usage**: Reference documentation for users and developers

### Utilities (`scripts/`)
**Purpose**: Automation scripts, maintenance utilities, and system tools  
**Usage**: Command-line tools for system management and automation

### Media Assets (`media/`)
**Purpose**: Images, diagrams, and visual content for documentation and flashcards  
**Usage**: Store and organize visual assets for content and documentation

---

## 🚀 Migration and Usage Notes

### File Movements Completed
- `db_utility.py` → `src/database/db_utility.py`
- `test_mnemosyne_complete.py` → `tests/test_mnemosyne_complete.py`
- `verify_installation.py` → `scripts/verify_installation.py`
- `data/interview_prep_test.db` → `data/databases/interview_prep_test.db`
- `docs/PLANNING.md` → `docs/planning/PLANNING.md`
- `docs/TASKS.md` → `docs/planning/TASKS.md`

### Import Path Updates Required
When using the reorganized code, update import statements:
```python
# Old import
from db_utility import DatabaseManager

# New import  
from src.database.db_utility import DatabaseManager
```

### Configuration Updates
Update any hardcoded paths in configuration files to use the new directory structure.

### Version Control
The `.git/` directory and `.github/` configurations remain at the root level for proper repository management.

---

## 🎯 Benefits of This Structure

1. **Clear Separation of Concerns**: Source code, content, data, and documentation are cleanly separated
2. **Scalable Content Organization**: Interview stages have dedicated directories for focused content development
3. **Professional Development Structure**: Follows Python project best practices with proper package organization
4. **Educational Focus**: Content structure directly maps to interview preparation stages
5. **Maintenance Efficiency**: Automated scripts and utilities are centralized for easy management
6. **Documentation Clarity**: Multiple documentation types are properly organized

This directory structure supports the systematic development and maintenance of the Mnemosyne interview preparation system while maintaining educational effectiveness and technical excellence.
