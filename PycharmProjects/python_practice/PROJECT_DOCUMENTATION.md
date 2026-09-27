# Python Practice Project Documentation

## 📋 Project Overview

This workspace contains a comprehensive Python project with multiple components focused on **data validation**, **maintenance management**, and **testing automation**. The project demonstrates integration with Snowflake data warehouse, Flask web applications, and Robot Framework for automated testing.

---

## 📁 Project Structure

### Root Level Files

#### **main.py**
- **Purpose**: Snowflake data validation and ETL testing
- **Functionality**:
  - Connects to Snowflake data warehouse
  - Performs count checks between source (SRC) and target (TGT) schemas
  - Executes MINUS queries to identify data differences
  - Exports validation results to CSV format
- **Key Features**:
  - Test Case 1: COUNT_CHECK - Compares row counts between SRC and TGT
  - Test Case 2: MINUS_CHECK - Finds records in SRC but not in TGT
  - Automated CSV report generation

#### **test.py**
- **Purpose**: Enhanced Snowflake validation with detailed logging
- **Improvements over main.py**:
  - Includes source and target count checks separately
  - More detailed test naming and reporting
  - Stores query information in output CSV
  - Better error handling and documentation

#### **test1.py**
- **Purpose**: Additional testing file (variant for testing purposes)

#### **test.ipynb**
- **Purpose**: Jupyter Notebook for interactive Python learning
- **Content**:
  - Basic input/output operations
  - String and integer handling
  - Print statements and formatting
  - Multi-line output examples

#### **Data Files** (CSV)
- `village_data.csv` - Raw village data
- `village1.csv`, `village2.csv`, `village3.csv` - Partitioned village data
- `validation_results.csv` - Output from validation scripts

---

## 📂 Subdirectories

### 1. **functional_testing/** - Automated Testing Suite

#### Files:
- **testcase.py** - Test case definitions and execution logic
- **query_execution.py** - Database query execution utilities
- **automated_testing_sheet.csv** - Test case repository
- **requirements.csv** - Test requirements and specifications

**Purpose**: Comprehensive automated testing framework for functional validation

---

### 2. **maintance/** - Flask Maintenance Management System

#### Overview
A Flask web application for managing **Prajay Water Front Phase 2** properties with 483 houses. Tracks payment status, availability, and month-wise maintenance.

#### Key Files:

##### **app.py**
- Main Flask application
- Provides web interface for property management
- RESTful endpoints for CRUD operations
- Database integration with SQLite/maintenance.db

##### **maintenance.db**
- SQLite database storing property and payment information
- Schema includes: house information, payment status, availability, maintenance tracking

##### **init_db.py**
- Database initialization script
- Creates initial schema and tables
- Populates default data

##### **migrate_db.py**
- Database migration utility
- Adds new columns for month-wise maintenance tracking
- Ensures backward compatibility

##### **check_cols.py**
- Utility to inspect database column structure
- Debugging and validation tool

##### **debug_post.py**
- Debugging utility for POST request handling
- Used for troubleshooting API issues

##### **smoke_test.py**
- Basic smoke tests for application
- Quick validation that core features work

##### **test_maintenance.py**
- Unit tests for maintenance-related operations
- Tests payment calculations and status updates

##### **test_sync.py**
- Tests for data synchronization features
- Validates sync between different data sources

##### **templates/index.html**
- HTML UI template
- Web interface for property management dashboard
- Forms for data entry and updates

##### **requirements.txt**
- Python dependencies for the Flask application
- Includes Flask, database drivers, utilities

##### **Configuration Files**:
- `QUICK_START.txt` - Quick setup instructions
- `START_HERE.txt` - Beginner's guide with ASCII art
- `QUICK_REFERENCE.txt` - Command reference
- `README.md` - Detailed documentation
- `FEATURES.md` - Feature list and description
- `LIVE_ACCESS_INFO.txt` - Production access information
- `NETWORK_ACCESS.txt` - Network configuration details
- `SYNC_DIAGRAM.txt` - Data sync architecture diagram
- `SYNC_FEATURE.md` - Data synchronization feature documentation

##### **launch.bat**
- Batch script for quick application startup
- Activates virtual environment and starts Flask server

#### Web Application Features:
✅ **Dashboard Summary** - Property statistics overview
✅ **Payment Management** - Track paid/unpaid status
✅ **Availability Tracking** - Monitor property status (Available/Rented/Occupied)
✅ **Month-wise Maintenance** - Record monthly maintenance payments

#### Quick Start:
```bash
cd C:\Users\USER\PycharmProjects\python_practice\maintance
launch.bat
# Navigate to http://127.0.0.1:5000/
```

---

### 3. **snowflake_robot_validation/** - Robot Framework Testing

#### Structure:

##### **libraries/snowflake_lib.py**
- Custom Robot Framework library for Snowflake operations
- Keywords for database connections
- Query execution utilities
- Data validation keywords

##### **resources/tables.yml**
- YAML configuration file
- Table definitions and schema mappings
- Test data specifications

##### **tests/validation.robot**
- Robot Framework test suite
- Automated acceptance tests for Snowflake validation
- Keywords-driven test cases

##### **Test Results** (Auto-generated):
- `report.html` - HTML test report
- `log.html` - Detailed test execution log
- `output.xml` - Machine-readable test output
- `validation_results.csv` - Validation results in CSV format

**Purpose**: Behavior-driven testing framework integrated with Robot Framework for Snowflake data warehouse validation

---

## 🔄 Workflow Summary

### Data Validation Flow:
```
1. Python Scripts (main.py, test.py)
   ↓
2. Connect to Snowflake
   ↓
3. Execute Validation Queries
   ├─ COUNT_CHECK
   ├─ MINUS_CHECK
   └─ Additional Validations
   ↓
4. Generate CSV Reports
   ↓
5. Store in validation_results.csv
```

### Maintenance Management Flow:
```
1. Flask Web App (maintance/app.py)
   ↓
2. SQLite Database (maintenance.db)
   ↓
3. User Interface (templates/index.html)
   ↓
4. CRUD Operations
   ├─ Create new properties
   ├─ Update payment status
   ├─ Manage availability
   └─ Track maintenance
```

### Automated Testing Flow:
```
1. Functional Tests (functional_testing/)
   ↓
2. Robot Framework Tests (snowflake_robot_validation/)
   ↓
3. Test Reports Generated
   ├─ HTML Reports
   ├─ XML Output
   └─ CSV Results
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Data Warehouse** | Snowflake |
| **Web Framework** | Flask |
| **Database** | SQLite |
| **Testing Framework** | Robot Framework |
| **Language** | Python 3.10+ |
| **Interactive Notebook** | Jupyter |
| **Data Format** | CSV, YAML |

---

## 📊 Key Features

### Data Validation
- ✅ Cross-schema data comparison
- ✅ Row count validation
- ✅ Data difference detection (MINUS queries)
- ✅ CSV report generation

### Maintenance Management
- ✅ 483 property management
- ✅ Payment tracking (Paid/Not Paid)
- ✅ Availability status (Available/Rented/Occupied)
- ✅ Month-wise maintenance tracking
- ✅ Web-based dashboard

### Testing & Automation
- ✅ Automated functional tests
- ✅ Robot Framework integration
- ✅ HTML test reports
- ✅ Smoke tests for quick validation

---

## 🚀 Getting Started

### Option 1: Run Maintenance App
```bash
cd maintance
.\.venv\Scripts\Activate      # Activate virtual environment
pip install -r requirements.txt # Install dependencies
python app.py                  # Start Flask app
# Visit http://127.0.0.1:5000/
```

### Option 2: Run Validation Scripts
```bash
python main.py                 # Run main validation
# Check validation_results.csv for results
```

### Option 3: Run Automated Tests
```bash
cd snowflake_robot_validation
robot -d tests tests/validation.robot
# Check tests/report.html for results
```

---

## 📝 Important Notes

### Security ⚠️
- **Credentials are hardcoded in scripts** - Move to environment variables in production
- Use `.env` files for sensitive information
- Never commit credentials to version control

### Database Maintenance
- Always run `migrate_db.py` after schema changes
- Keep backups of `maintenance.db` before migrations
- Use `check_cols.py` to verify schema integrity

### Testing
- Run smoke tests before deployment
- Review validation results in CSV format
- Check HTML reports for detailed test information

---

## 📞 Support & Documentation

Refer to these files for additional information:
- `maintance/START_HERE.txt` - Quick start guide
- `maintance/README.md` - Detailed README
- `maintance/FEATURES.md` - Feature documentation
- `maintance/QUICK_REFERENCE.txt` - Command reference
- `maintance/SYNC_FEATURE.md` - Data sync documentation

---

## 📅 Last Updated
April 24, 2026

**Version**: 1.0  
**Status**: Active & Maintained

---

## ✨ Quick Links

| Task | File | Command |
|------|------|---------|
| Start Web App | `maintance/app.py` | `python app.py` |
| Run Validation | `main.py` | `python main.py` |
| Initialize DB | `maintance/init_db.py` | `python init_db.py` |
| Migrate DB | `maintance/migrate_db.py` | `python migrate_db.py` |
| Run Robot Tests | `snowflake_robot_validation/tests/validation.robot` | `robot tests/validation.robot` |
| Check DB Schema | `maintance/check_cols.py` | `python check_cols.py` |

---


