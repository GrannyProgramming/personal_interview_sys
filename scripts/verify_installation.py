#!/usr/bin/env python3
"""
Installation Verification Script for Mnemosyne Interview Preparation System
Created: June 13, 2025
Purpose: Verify all core dependencies are properly installed and functional
"""

import sys
import os
from datetime import datetime

def print_header(title):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def test_basic_imports():
    """Test basic Python environment and imports."""
    print_header("BASIC ENVIRONMENT CHECK")
    
    print(f"Python Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Platform: {sys.platform}")
    
    # Check if we're in WSL
    if os.path.exists('/proc/version'):
        with open('/proc/version', 'r') as f:
            version_info = f.read().lower()
            if 'microsoft' in version_info or 'wsl' in version_info:
                print("✅ Running in WSL environment")
            else:
                print("ℹ️  Running in native Linux environment")
    
    # Check environment variables
    display = os.environ.get('DISPLAY', 'Not set')
    wsl_distro = os.environ.get('WSL_DISTRO_NAME', 'Not set')
    print(f"DISPLAY: {display}")
    print(f"WSL_DISTRO_NAME: {wsl_distro}")

def test_core_packages():
    """Test core package imports."""
    print_header("CORE PACKAGE VERIFICATION")
    
    packages_to_test = [
        ('mnemosyne', 'Mnemosyne flashcard application'),
        ('PyQt6.QtWidgets', 'PyQt6 GUI framework'),
        ('numpy', 'NumPy scientific computing'),
        ('pandas', 'Pandas data analysis'),
        ('matplotlib', 'Matplotlib plotting'),
        ('sqlite3', 'SQLite database (built-in)'),
        ('jupyter', 'Jupyter ecosystem'),
        ('IPython', 'IPython enhanced shell'),
    ]
    
    results = []
    for package, description in packages_to_test:
        try:
            if package == 'PyQt6.QtWidgets':
                import PyQt6.QtWidgets
                version = f"PyQt6 {PyQt6.QtWidgets.QApplication.libraryPaths()}"
                version = "PyQt6 (GUI framework)"
            else:
                module = __import__(package)
                version = getattr(module, '__version__', 'Version not available')
            
            print(f"✅ {package:20} | {description:30} | {version}")
            results.append((package, True, version))
        except ImportError as e:
            print(f"❌ {package:20} | {description:30} | Import failed: {e}")
            results.append((package, False, str(e)))
        except Exception as e:
            print(f"⚠️  {package:20} | {description:30} | Error: {e}")
            results.append((package, False, str(e)))
    
    return results

def test_gui_availability():
    """Test if GUI components can be created (without displaying)."""
    print_header("GUI SYSTEM VERIFICATION")
    
    try:
        from PyQt6.QtWidgets import QApplication, QLabel
        import sys
        
        # Create QApplication instance (required for any Qt widgets)
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        
        # Create a simple widget to test functionality
        label = QLabel("Test label")
        print("✅ PyQt6 widgets can be created successfully")
        
        # Clean up
        app.quit()
        print("✅ GUI framework cleanup successful")
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        print("ℹ️  This might be normal if X11 forwarding is not set up")
        return False

def test_database_functionality():
    """Test SQLite database operations."""
    print_header("DATABASE FUNCTIONALITY CHECK")
    
    try:
        import sqlite3
        import tempfile
        import os
        
        # Create temporary database
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        # Test basic database operations
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create test table
        cursor.execute('''
            CREATE TABLE test_flashcards (
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert test data
        cursor.execute(
            "INSERT INTO test_flashcards (question, answer) VALUES (?, ?)",
            ("What is the capital of France?", "Paris")
        )
        
        # Query test data
        cursor.execute("SELECT * FROM test_flashcards")
        result = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        # Clean up
        os.unlink(db_path)
        
        if result:
            print("✅ SQLite database operations successful")
            print(f"   Test record: {result}")
            return True
        else:
            print("❌ Database test failed: No data retrieved")
            return False
            
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def generate_summary_report(package_results, gui_test, db_test):
    """Generate a summary report of the installation verification."""
    print_header("INSTALLATION VERIFICATION SUMMARY")
    
    total_packages = len(package_results)
    successful_packages = sum(1 for _, success, _ in package_results if success)
    
    print(f"📦 Package Installation: {successful_packages}/{total_packages} successful")
    print(f"🖥️  GUI Framework: {'✅ Working' if gui_test else '❌ Issues detected'}")
    print(f"💾 Database System: {'✅ Working' if db_test else '❌ Issues detected'}")
    
    if successful_packages == total_packages and db_test:
        print(f"\n🎉 INSTALLATION VERIFICATION COMPLETE!")
        print(f"   All core components are working correctly.")
        print(f"   System is ready for Mnemosyne interview preparation.")
    else:
        print(f"\n⚠️  INSTALLATION VERIFICATION INCOMPLETE")
        print(f"   Some components need attention before proceeding.")
        print(f"   Check the detailed output above for specific issues.")
    
    print(f"\n📅 Verification completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main verification routine."""
    print_header("MNEMOSYNE INTERVIEW PREP SYSTEM - INSTALLATION VERIFICATION")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run all tests
    test_basic_imports()
    package_results = test_core_packages()
    gui_test = test_gui_availability()
    db_test = test_database_functionality()
    
    # Generate summary
    generate_summary_report(package_results, gui_test, db_test)

if __name__ == "__main__":
    main()
