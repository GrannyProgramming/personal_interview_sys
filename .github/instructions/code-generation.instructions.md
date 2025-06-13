---
applyTo: "**/*.py,**/*.sh,**/requirements.txt,**/setup.py,**/pyproject.toml"
---

# Code Generation Standards for Mnemosyne Interview Preparation System

**Version**: 1.0 | **Framework**: Implementation-Focused | **Last Updated**: June 13, 2025  
**Project Context**: Personal interview preparation system using Mnemosyne flashcards for Skyscanner Senior Software Engineer role

---

## 🚀 Quick Reference (Match Conversation Types)

### Code Generation Decision Matrix (No Maybe Now Principle)

| Code Type | Conversation Match | Action | Complexity | Validation |
|-----------|-------------------|--------|------------|------------|
| **Config/setup scripts** | Technical-Direct | Never assess | Direct implementation | Syntax check |
| **Core application logic** | Implementation | Maybe assess | Pattern validation | Unit tests |
| **Database operations** | Technical-Complex | Always assess | Transaction safety | Integration tests |
| **GUI components** | Interactive | Always assess | Cross-platform compatibility | Manual GUI testing |

### Tool Priority Hierarchy (Prioritize Internal Tools)
```
1. Local Python environment    # WSL virtual environment authority
2. Mnemosyne API/database     # Application-specific operations authority  
3. System libraries           # PyQt6, SQLite, standard library authority
4. External packages          # pip packages, LaTeX dependencies
```

### Never Rules (Hard Never - Sparingly Used)
- **NEVER** hardcode file paths without WSL compatibility checks
- **NEVER** create database operations without transaction handling
- **NEVER** implement GUI components without cross-platform consideration
- **NEVER** write Python code that requires Windows-specific libraries in WSL

---

## 🐍 Python Coding Standards (Scaling Effort)

### Code Quality Classification (Good and Bad Examples)

#### ✅ EXCELLENT Python Code
```python
# WSL-compatible path handling with proper error handling
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class MnemosyneConfig:
    """Configuration manager for Mnemosyne interview preparation system.
    
    Handles WSL-compatible paths, environment variables, and database configuration
    with proper error handling and validation.
    """
    
    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or self._get_default_config_dir()
        self.database_path = self.config_dir / "interview_prep.db"
        self._validate_environment()
    
    def _get_default_config_dir(self) -> Path:
        """Get default configuration directory with WSL compatibility."""
        if os.environ.get('WSL_DISTRO_NAME'):
            # WSL environment - use Linux-style paths
            return Path.home() / ".config" / "mnemosyne_interview"
        else:
            # Native Linux/macOS
            return Path.home() / ".mnemosyne_interview"
    
    def _validate_environment(self) -> None:
        """Validate that the environment supports required operations."""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Configuration directory: {self.config_dir}")
        except PermissionError as e:
            raise EnvironmentError(f"Cannot create config directory: {e}")
    
    def get_database_url(self) -> str:
        """Get SQLite database URL with proper escaping."""
        return f"sqlite:///{self.database_path.absolute()}"
```

#### ❌ POOR Python Code (Never Do This)
```python
# Bad: Hardcoded Windows paths, no error handling
config_dir = "C:\\Users\\Alex\\mnemosyne"  # ❌ Won't work in WSL
db = sqlite3.connect("database.db")  # ❌ No path management, no error handling
data = some_function()  # ❌ No type hints, unclear function
```

### Python Code Patterns (Trust But Verify)

#### Database Operations Pattern
```python
import sqlite3
from contextlib import contextmanager
from typing import Generator, Any, List, Tuple

@contextmanager
def get_db_connection(db_path: Path) -> Generator[sqlite3.Connection, None, None]:
    """Context manager for safe database operations with transaction handling."""
    conn = None
    try:
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row  # Enable column access by name
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Database operation failed: {e}")
        raise
    finally:
        if conn:
            conn.close()

def create_flashcard(content: str, tags: List[str], difficulty: int) -> int:
    """Create a new flashcard with proper validation and error handling."""
    if not content.strip():
        raise ValueError("Flashcard content cannot be empty")
    
    if difficulty not in range(1, 6):
        raise ValueError("Difficulty must be between 1 and 5")
    
    with get_db_connection(config.database_path) as conn:
        cursor = conn.execute(
            """INSERT INTO flashcards (content, tags, difficulty, created_at) 
               VALUES (?, ?, ?, datetime('now'))""",
            (content, ','.join(tags), difficulty)
        )
        return cursor.lastrowid
```

#### GUI Component Pattern (PyQt6)
```python
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QTimer, pyqtSignal
from typing import Protocol

class FlashcardDisplayProtocol(Protocol):
    """Protocol for flashcard display components."""
    def show_question(self, question: str) -> None: ...
    def show_answer(self, answer: str) -> None: ...
    def reset_display(self) -> None: ...

class FlashcardWidget(QWidget):
    """Cross-platform flashcard display widget with WSL GUI support."""
    
    card_answered = pyqtSignal(int, bool)  # card_id, correct
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_card_id: Optional[int] = None
        self._setup_ui()
        self._setup_style()
    
    def _setup_ui(self) -> None:
        """Initialize UI components with responsive layout."""
        layout = QVBoxLayout(self)
        
        self.content_label = QLabel()
        self.content_label.setWordWrap(True)
        self.content_label.setMinimumHeight(200)
        
        self.show_answer_btn = QPushButton("Show Answer")
        self.show_answer_btn.clicked.connect(self._show_answer)
        
        layout.addWidget(self.content_label)
        layout.addWidget(self.show_answer_btn)
    
    def _setup_style(self) -> None:
        """Apply consistent styling for cross-platform compatibility."""
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: white;
            }
            QPushButton {
                font-size: 12px;
                padding: 8px 16px;
                border-radius: 4px;
                background-color: #007acc;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
```

---

## 🗄️ Database Design Patterns

### SQLite Schema Standards
```python
# Database schema with proper indexing and constraints
CREATE_TABLES_SQL = """
-- Flashcards table with hierarchical tagging support
CREATE TABLE IF NOT EXISTS flashcards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL CHECK(length(content) > 0),
    answer TEXT,
    tags TEXT NOT NULL,  -- JSON array of hierarchical tags
    difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 5),
    stage TEXT CHECK(stage IN ('data_manipulation', 'culture_fit', 'mlops', 'work_history')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_reviewed TIMESTAMP,
    review_count INTEGER DEFAULT 0,
    success_rate REAL DEFAULT 0.0
);

-- Spaced repetition tracking
CREATE TABLE IF NOT EXISTS review_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    difficulty_rating INTEGER CHECK(difficulty_rating BETWEEN 1 AND 5),
    response_time INTEGER,  -- milliseconds
    correct BOOLEAN NOT NULL,
    FOREIGN KEY (card_id) REFERENCES flashcards(id)
);

-- Performance indexes
CREATE INDEX IF NOT EXISTS idx_flashcards_stage ON flashcards(stage);
CREATE INDEX IF NOT EXISTS idx_flashcards_difficulty ON flashcards(difficulty);
CREATE INDEX IF NOT EXISTS idx_flashcards_last_reviewed ON flashcards(last_reviewed);
CREATE INDEX IF NOT EXISTS idx_review_sessions_card_id ON review_sessions(card_id);
CREATE INDEX IF NOT EXISTS idx_review_sessions_reviewed_at ON review_sessions(reviewed_at);
"""

def initialize_database(db_path: Path) -> None:
    """Initialize database with proper schema and error handling."""
    try:
        with get_db_connection(db_path) as conn:
            conn.executescript(CREATE_TABLES_SQL)
            logger.info("Database initialized successfully")
    except sqlite3.Error as e:
        logger.error(f"Database initialization failed: {e}")
        raise
```

---

## 🎯 Mnemosyne-Specific Patterns

### Spaced Repetition Algorithm Implementation
```python
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

class DifficultyRating(Enum):
    """SM-2 algorithm difficulty ratings."""
    AGAIN = 1      # Complete blackout
    HARD = 2       # Incorrect response, but remembered upon seeing answer
    GOOD = 3       # Correct response, but required some effort
    EASY = 4       # Correct response with perfect recall

@dataclass
class SpacedRepetitionCard:
    """Card data for spaced repetition calculations."""
    card_id: int
    easiness_factor: float = 2.5
    interval: int = 1
    repetitions: int = 0
    last_reviewed: Optional[datetime] = None

def calculate_next_review(
    card: SpacedRepetitionCard, 
    difficulty: DifficultyRating
) -> Tuple[datetime, SpacedRepetitionCard]:
    """Calculate next review date using SM-2 algorithm.
    
    Args:
        card: Current card state
        difficulty: User's difficulty rating (1-4)
    
    Returns:
        Tuple of (next_review_date, updated_card_state)
    """
    now = datetime.now()
    
    # Update easiness factor
    ef = card.easiness_factor
    if difficulty.value >= 3:
        ef += (0.1 - (5 - difficulty.value) * (0.08 + (5 - difficulty.value) * 0.02))
    else:
        ef = max(1.3, ef - 0.8 + 0.28 * difficulty.value - 0.02 * difficulty.value ** 2)
    
    # Calculate next interval
    if difficulty.value < 3:
        # Reset for difficult cards
        interval = 1
        repetitions = 0
    else:
        if card.repetitions == 0:
            interval = 1
        elif card.repetitions == 1:
            interval = 6
        else:
            interval = int(card.interval * ef)
        repetitions = card.repetitions + 1
    
    updated_card = SpacedRepetitionCard(
        card_id=card.card_id,
        easiness_factor=ef,
        interval=interval,
        repetitions=repetitions,
        last_reviewed=now
    )
    
    next_review = now + timedelta(days=interval)
    return next_review, updated_card
```

### Content Processing Patterns
```python
import re
from typing import Dict, List, Set
import json

class ContentProcessor:
    """Process and validate flashcard content for interview preparation."""
    
    # LaTeX pattern for mathematical expressions
    LATEX_PATTERN = re.compile(r'\$\$?([^$]+)\$\$?')
    
    # Code block pattern for syntax highlighting
    CODE_PATTERN = re.compile(r'```(\w+)?\n(.*?)\n```', re.DOTALL)
    
    # Hierarchical tag validation
    VALID_STAGES = {'data_manipulation', 'culture_fit', 'mlops', 'work_history'}
    
    @classmethod
    def validate_content(cls, content: str, tags: List[str]) -> Dict[str, Any]:
        """Validate flashcard content and extract metadata.
        
        Returns:
            Dict with validation results and extracted metadata
        """
        issues = []
        metadata = {
            'has_latex': bool(cls.LATEX_PATTERN.search(content)),
            'has_code': bool(cls.CODE_PATTERN.search(content)),
            'word_count': len(content.split()),
            'code_languages': [],
            'latex_expressions': []
        }
        
        # Extract code languages
        code_matches = cls.CODE_PATTERN.findall(content)
        metadata['code_languages'] = [lang for lang, _ in code_matches if lang]
        
        # Extract LaTeX expressions for validation
        latex_matches = cls.LATEX_PATTERN.findall(content)
        metadata['latex_expressions'] = latex_matches
        
        # Validate tag hierarchy
        stage_tags = [tag for tag in tags if tag in cls.VALID_STAGES]
        if not stage_tags:
            issues.append("Must have at least one stage tag")
        elif len(stage_tags) > 1:
            issues.append("Should have exactly one stage tag")
        
        # Content length validation
        if metadata['word_count'] < 3:
            issues.append("Content too short (minimum 3 words)")
        elif metadata['word_count'] > 500:
            issues.append("Content very long (consider splitting)")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'metadata': metadata
        }
    
    @classmethod
    def extract_hierarchical_tags(cls, tags: List[str]) -> Dict[str, List[str]]:
        """Extract hierarchical tag structure from flat tag list."""
        hierarchy = {
            'stage': [],
            'topic': [],
            'complexity': [],
            'other': []
        }
        
        for tag in tags:
            if tag in cls.VALID_STAGES:
                hierarchy['stage'].append(tag)
            elif tag.startswith('complexity_'):
                hierarchy['complexity'].append(tag)
            elif any(topic in tag.lower() for topic in ['pandas', 'sql', 'python', 'ml', 'system']):
                hierarchy['topic'].append(tag)
            else:
                hierarchy['other'].append(tag)
        
        return hierarchy
```

---

## 🖥️ WSL Environment Compatibility

### Environment Detection and Setup
```python
import os
import subprocess
import sys
from pathlib import Path

class WSLEnvironment:
    """Manage WSL-specific environment setup and validation."""
    
    @staticmethod
    def is_wsl() -> bool:
        """Detect if running in WSL environment."""
        return (
            'microsoft' in Path('/proc/version').read_text().lower()
            if Path('/proc/version').exists()
            else False
        ) or bool(os.environ.get('WSL_DISTRO_NAME'))
    
    @staticmethod
    def validate_gui_support() -> Dict[str, bool]:
        """Validate GUI support in WSL environment."""
        checks = {
            'display_set': bool(os.environ.get('DISPLAY')),
            'x11_available': False,
            'qt_platform': False
        }
        
        # Test X11 availability
        try:
            result = subprocess.run(['xset', 'q'], 
                                 capture_output=True, 
                                 timeout=5)
            checks['x11_available'] = result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        # Test Qt platform
        try:
            import PyQt6.QtWidgets
            app = PyQt6.QtWidgets.QApplication.instance()
            if app is None:
                app = PyQt6.QtWidgets.QApplication([])
            checks['qt_platform'] = True
        except ImportError:
            pass
        
        return checks
    
    @classmethod
    def setup_environment(cls) -> None:
        """Configure environment for optimal WSL operation."""
        if not cls.is_wsl():
            return
        
        # Set display if not already set
        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':0'
        
        # Configure Qt for WSL
        os.environ['QT_QPA_PLATFORM'] = 'xcb'
        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
        
        # Validate setup
        gui_status = cls.validate_gui_support()
        if not all(gui_status.values()):
            logger.warning(f"GUI setup incomplete: {gui_status}")
```

---

## 📊 Performance and Testing Standards

### Performance Monitoring Pattern
```python
import time
import functools
from typing import Callable, Dict, Any
import logging

def performance_monitor(threshold_ms: int = 1000):
    """Decorator to monitor function performance and log slow operations."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.perf_counter()
                duration_ms = (end_time - start_time) * 1000
                
                if duration_ms > threshold_ms:
                    logger.warning(
                        f"Slow operation: {func.__name__} took {duration_ms:.1f}ms "
                        f"(threshold: {threshold_ms}ms)"
                    )
                else:
                    logger.debug(f"{func.__name__} completed in {duration_ms:.1f}ms")
        
        return wrapper
    return decorator

# Usage example
@performance_monitor(threshold_ms=500)
def load_flashcards_for_review(stage: str, limit: int = 20) -> List[Dict]:
    """Load flashcards due for review with performance monitoring."""
    # Implementation here
    pass
```

### Testing Patterns
```python
import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

@pytest.fixture
def temp_database():
    """Provide a temporary database for testing."""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
        db_path = Path(tmp.name)
    
    try:
        initialize_database(db_path)
        yield db_path
    finally:
        if db_path.exists():
            db_path.unlink()

@pytest.fixture
def mock_wsl_environment():
    """Mock WSL environment for testing."""
    with patch.dict(os.environ, {'WSL_DISTRO_NAME': 'Ubuntu', 'DISPLAY': ':0'}):
        yield

def test_flashcard_creation_validation(temp_database):
    """Test flashcard creation with proper validation."""
    # Test valid flashcard
    card_id = create_flashcard(
        content="What is pandas DataFrame.merge()?",
        tags=["data_manipulation", "pandas", "complexity_intermediate"],
        difficulty=3
    )
    assert isinstance(card_id, int)
    assert card_id > 0
    
    # Test invalid flashcard
    with pytest.raises(ValueError, match="content cannot be empty"):
        create_flashcard("", ["data_manipulation"], 3)
    
    with pytest.raises(ValueError, match="Difficulty must be between"):
        create_flashcard("Valid content", ["data_manipulation"], 6)
```

---

## 🔧 Development Workflow Standards

### Error Handling Pattern
```python
from enum import Enum
import traceback

class ErrorSeverity(Enum):
    LOW = "low"          # Degraded functionality, system continues
    MEDIUM = "medium"    # Feature unavailable, workaround possible
    HIGH = "high"        # System unstable, immediate attention needed
    CRITICAL = "critical" # System failure, data loss risk

class InterviewPrepError(Exception):
    """Base exception for interview preparation system."""
    
    def __init__(self, message: str, severity: ErrorSeverity = ErrorSeverity.MEDIUM):
        super().__init__(message)
        self.severity = severity
        self.timestamp = datetime.now()

def handle_application_error(func: Callable) -> Callable:
    """Decorator for consistent error handling across the application."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except InterviewPrepError:
            # Re-raise application errors
            raise
        except Exception as e:
            # Convert unexpected errors to application errors
            logger.error(f"Unexpected error in {func.__name__}: {e}")
            logger.debug(f"Traceback: {traceback.format_exc()}")
            raise InterviewPrepError(
                f"Unexpected error in {func.__name__}: {str(e)}",
                ErrorSeverity.HIGH
            ) from e
    
    return wrapper
```

---

## 🚀 Success Criteria for Generated Code

### Code Quality Metrics
- ✅ **Type Safety**: All functions have proper type hints
- ✅ **Error Handling**: Comprehensive exception handling with user-friendly messages
- ✅ **WSL Compatibility**: Cross-platform path handling and environment detection
- ✅ **Performance**: Database operations complete in <500ms, GUI responses in <100ms
- ✅ **Testing**: All public functions have corresponding unit tests
- ✅ **Documentation**: Docstrings for all classes and public methods

### Implementation Standards
- **Database**: Transaction safety, proper indexing, connection pooling
- **GUI**: Responsive design, cross-platform styling, accessibility support
- **Content**: LaTeX support, syntax highlighting, hierarchical tagging
- **Algorithm**: Proper SM-2 implementation, performance optimization
- **Environment**: WSL compatibility, virtual environment isolation

**Code Generation Mission**: Create robust, maintainable, and educational-focused Python code that supports effective interview preparation while maintaining cross-platform compatibility and optimal performance in WSL environments.
