---
applyTo: "**/test_*.py,**/*_test.py,**/tests/**/*.py,**/*test*.py"
---

# Test Generation Instructions for Mnemosyne Interview Preparation System

**Version**: 1.0 | **Framework**: Testing-Focused | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## Overview
Generate comprehensive tests for a Python-based interview preparation system using Mnemosyne flashcards. Focus on educational content reliability, cross-platform compatibility, and data integrity.

## Core Testing Principles

### 1. Match Test Complexity to Code Function
- **Utility functions**: Unit tests with edge cases and error conditions
- **Database operations**: Integration tests with rollback scenarios
- **GUI components**: Mock-based tests with user interaction simulation
- **Content management**: End-to-end tests with real flashcard data

### 2. Python Testing Standards

#### Test Framework Selection
```python
# Primary testing stack
import pytest  # Main testing framework
import pytest-mock  # Mocking capabilities
import pytest-xvfb  # GUI testing in headless environment
import pytest-cov  # Coverage reporting
```

#### ✅ ALWAYS Include:
- **Fixtures** for database setup/teardown
- **Parametrized tests** for multiple input scenarios
- **Mock objects** for external dependencies (file system, GUI)
- **Property-based testing** for complex algorithms (spaced repetition)
- **Coverage targets**: >90% for core logic, >80% overall

#### ❌ NEVER Generate:
- Tests that modify production database
- GUI tests that require actual display server
- Tests with hardcoded file paths
- Tests that depend on external network access
- Tests that don't clean up temporary files

### 3. WSL Environment Testing

#### Critical Test Scenarios:
```python
# Cross-platform path handling
def test_config_path_creation():
    """Test config path works on both Windows and Linux."""
    config_path = get_config_path()
    assert config_path.exists() or config_path.parent.exists()
    assert str(config_path).replace('\\', '/') == str(config_path.as_posix())

# File permission handling
def test_backup_file_permissions():
    """Test backup files have correct permissions in WSL."""
    backup_path = create_backup()
    stat_info = backup_path.stat()
    assert stat_info.st_mode & 0o600  # Owner read/write
```

#### Mock X11 Display:
```python
@pytest.fixture
def mock_display():
    """Mock X11 display for GUI testing."""
    with patch.dict(os.environ, {'DISPLAY': ':0'}):
        yield
```

### 4. Educational Content Testing

#### Flashcard Data Integrity:
```python
def test_flashcard_latex_rendering():
    """Test LaTeX formulas render correctly."""
    card = Flashcard(
        question="What is the time complexity?",
        answer="$O(n \\log n)$"
    )
    rendered = card.render_answer()
    assert "log" in rendered
    assert "error" not in rendered.lower()

def test_tag_hierarchy_validation():
    """Test tag hierarchy follows Stage→Topic→Complexity pattern."""
    valid_tags = ["Stage1", "Stage1/DataManipulation", "Stage1/DataManipulation/Medium"]
    invalid_tags = ["InvalidStage", "Stage1/InvalidTopic/Medium"]
    
    for tag in valid_tags:
        assert validate_tag_hierarchy(tag) is True
    for tag in invalid_tags:
        assert validate_tag_hierarchy(tag) is False
```

#### Spaced Repetition Algorithm:
```python
def test_spaced_repetition_intervals():
    """Test SuperMemo SM-2 algorithm implementation."""
    card = FlashCard(easiness_factor=2.5, interval=1, repetitions=0)
    
    # Test different quality ratings
    test_cases = [
        (5, 6, 2.6),  # Perfect response
        (3, 6, 2.36), # Correct with hesitation
        (0, 1, 1.3),  # Incorrect response
    ]
    
    for quality, expected_interval, expected_ef in test_cases:
        card.update_from_response(quality)
        assert card.interval == expected_interval
        assert abs(card.easiness_factor - expected_ef) < 0.01
```

### 5. Database and Backup Testing

#### Database Operations:
```python
@pytest.fixture
def temp_database():
    """Create temporary database for testing."""
    db_path = Path("/tmp/test_interview_prep.db")
    db = create_database(db_path)
    yield db
    db.close()
    if db_path.exists():
        db_path.unlink()

def test_database_backup_restore():
    """Test complete backup and restore cycle."""
    original_db = create_test_database_with_cards()
    backup_path = create_backup(original_db)
    
    # Corrupt original database
    original_db.execute("DROP TABLE cards")
    
    # Restore from backup
    restore_from_backup(backup_path, original_db)
    
    # Verify data integrity
    cards = original_db.execute("SELECT * FROM cards").fetchall()
    assert len(cards) > 0
    assert all(card['content'] for card in cards)
```

### 6. Error Handling and Edge Cases

#### File System Errors:
```python
def test_config_file_missing():
    """Test graceful handling of missing config file."""
    with patch('pathlib.Path.exists', return_value=False):
        config = load_config()
        assert config == get_default_config()

def test_database_locked():
    """Test handling of database lock situations."""
    with patch('sqlite3.connect', side_effect=sqlite3.OperationalError("database is locked")):
        with pytest.raises(DatabaseLockError):
            open_database()
```

#### Memory and Performance:
```python
def test_large_flashcard_set_performance():
    """Test system performance with 1000+ flashcards."""
    cards = [create_test_card(i) for i in range(1000)]
    
    start_time = time.time()
    search_results = search_cards("python")
    end_time = time.time()
    
    assert end_time - start_time < 0.5  # Should complete in <500ms
    assert len(search_results) > 0
```

## Test Organization Structure

```
tests/
├── unit/
│   ├── test_flashcard_model.py
│   ├── test_spaced_repetition.py
│   ├── test_tag_management.py
│   └── test_content_rendering.py
├── integration/
│   ├── test_database_operations.py
│   ├── test_backup_restore.py
│   └── test_import_export.py
├── gui/
│   ├── test_main_window.py
│   ├── test_study_session.py
│   └── test_card_editor.py
├── fixtures/
│   ├── sample_cards.json
│   ├── test_database.sql
│   └── mock_responses.py
└── conftest.py  # Shared fixtures and configuration
```

## Coverage and Quality Targets

### Coverage Requirements:
- **Core business logic**: 95%+ coverage
- **Database operations**: 90%+ coverage
- **GUI components**: 70%+ coverage (focus on logic, not rendering)
- **Overall project**: 85%+ coverage

### Quality Metrics:
```python
# Performance benchmarks
MAX_STARTUP_TIME = 10.0  # seconds
MAX_SEARCH_TIME = 0.5    # seconds
MAX_CARD_RENDER_TIME = 2.0  # seconds

# Memory usage limits
MAX_MEMORY_USAGE = 100  # MB for 1000 cards
```

## GitHub-Specific Commands

```yaml
# Apply to Python files
applyTo: "*.py"
applyTo: "tests/**/*.py"

# Exclude from test generation
exclude: "tests/"
exclude: "*.pyc"
exclude: "__pycache__/"
exclude: "*.db"
exclude: "migrations/"

# Test-specific patterns
test_file_pattern: "test_*.py"
test_function_pattern: "test_*"
```

## Test Generation Templates

### Basic Unit Test Template:
```python
def test_{function_name}():
    """Test {function_description}."""
    # Arrange
    input_data = create_test_data()
    expected_result = calculate_expected_result()
    
    # Act
    actual_result = function_under_test(input_data)
    
    # Assert
    assert actual_result == expected_result
    assert validate_side_effects()
```

### Integration Test Template:
```python
def test_{integration_scenario}(temp_database):
    """Test {integration_description}."""
    # Setup
    setup_test_environment(temp_database)
    
    # Execute
    result = perform_integration_operation()
    
    # Verify
    assert_database_state_correct(temp_database)
    assert_no_data_corruption()
    assert_performance_acceptable()
```

## Hard Never Rules

- **NEVER generate** tests that could corrupt actual study data
- **NEVER create** tests that require manual intervention
- **NEVER write** tests that depend on specific file system layout
- **NEVER produce** tests that don't clean up after themselves
- **NEVER include** actual personal study content in test fixtures

## Success Criteria

Generated tests should:
- ✅ Run reliably in WSL environment without GUI display
- ✅ Cover all critical paths including error conditions
- ✅ Execute quickly (full test suite <30 seconds)
- ✅ Provide clear failure messages for debugging
- ✅ Maintain data integrity throughout test execution
- ✅ Support continuous integration workflows

Focus on creating tests that build confidence in the system's reliability for interview preparation while maintaining fast feedback cycles for development.
