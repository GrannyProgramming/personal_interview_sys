# Mnemosyne Interview Preparation System

A comprehensive flashcard-based learning system using Mnemosyne for mastering technical concepts and behavioral scenarios for the Skyscanner Senior Software Engineer - Distributed Systems (AI Enablement) interview.

## 🎯 Project Overview

**Target Role**: Skyscanner Senior Software Engineer - Distributed Systems (AI Enablement)  
**Timeline**: 4-7 day rapid preparation window  
**Environment**: Python virtual environment in Windows WSL2  
**Learning Method**: Spaced repetition using Mnemosyne flashcards

## 🚀 Quick Start

### Prerequisites
- Windows WSL2 with GUI support (X11 forwarding)
- Python 3.8+ in WSL environment
- X11 server running (VcXsrv or X410)

### Installation
```bash
# Clone repository
git clone <repository-url>
cd personal_interview_sys

# Create virtual environment
python -m venv interview_prep_env
source interview_prep_env/bin/activate

# Install Mnemosyne and dependencies
pip install mnemosyne
pip install -r requirements.txt

# Verify GUI operation
export DISPLAY=:0
mnemosyne
```

## 📚 Interview Preparation Stages

### Stage 1: Data Manipulation (35% study time)
- **Topics**: pandas, SQL, data processing patterns
- **Card Count**: 60-80 flashcards
- **Focus**: Technical competency for data manipulation tasks

### Stage 2: Culture Fit (20% study time)
- **Topics**: Behavioral scenarios, company values, STAR method
- **Card Count**: 40-50 flashcards
- **Focus**: Cultural alignment and behavioral competency

### Stage 3: MLOps Engineering (30% study time)
- **Topics**: Pipelines, monitoring, infrastructure, system design
- **Card Count**: 70-90 flashcards
- **Focus**: Technical system design and operational excellence

### Stage 4: Work History (15% study time)
- **Topics**: Technical achievements, project reflections
- **Card Count**: 30-40 flashcards
- **Focus**: Experience articulation and growth demonstration

## 📖 Documentation

- **[Planning Document](docs/PLANNING.md)**: Complete project vision, requirements, and architecture
- **[Task Breakdown](docs/TASKS.md)**: Detailed implementation tasks and progress tracking
- **Setup Guides**: WSL configuration and environment setup (coming soon)
- **Content Templates**: Flashcard creation templates by stage (coming soon)

## 🛠️ System Architecture

- **Database**: SQLite for card storage and study history
- **Spaced Repetition**: SuperMemo SM-2 algorithm implementation
- **Content Organization**: Hierarchical tagging (Stage → Topic → Difficulty)
- **Backup Strategy**: Automated daily exports with integrity validation
- **Performance Targets**: <10s startup, <500ms card rendering

## 📊 Success Metrics

- ✅ Complete system setup within 4 hours
- ✅ Comprehensive card library covering all interview domains
- ✅ 85%+ retention rate on technical concepts
- ✅ Confident performance across all interview stages
- ✅ Reliable operation in WSL2 environment

## 🤝 Contributing

This is a personal interview preparation system. For documentation standards and contribution guidelines, see [documentation instructions](.github/instructions/documentation.instructions.md).

## 📄 License

Personal use project for interview preparation.

---

**Last Updated**: June 13, 2025  
**Status**: Initial setup phase  
**Next Milestone**: Complete WSL environment setup and Mnemosyne installation
