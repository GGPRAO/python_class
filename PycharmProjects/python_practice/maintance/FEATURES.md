PRAJAY WATER FRONT PHASE 2 - MAINTENANCE MANAGEMENT SYSTEM
========================================================

✅ COMPLETED FEATURES:

1. House Management
   ✅ Total Houses: 483 (H-001 to H-483)
   ✅ Paid / Not Paid tracking
   ✅ Availability status: Available / Rented / Occupied
   ✅ Month-wise Maintenance tracking (per month payment)

2. Dashboard Summary
   ✅ Total Houses count
   ✅ Paid houses count
   ✅ Not Paid houses count
   ✅ Available houses count
   ✅ Rented houses count
   ✅ Occupied houses count
   ✅ Maintenance Paid (current month) count

3. Per-House Controls
   ✅ Set Payment Status (dropdown)
   ✅ Set Availability (dropdown)
   ✅ Add Maintenance Month (month picker)
   ✅ Remove Maintenance Month (button)

4. Data Export
   ✅ CSV Export (houses.csv)
   ✅ Includes: house_number, payment_status, availability, maintenance_paid_months

5. Visual Indicators
   ✅ Row colors for payment status (green=paid, red=not_paid)
   ✅ Row colors for availability (light green=available, orange=rented, blue=occupied)
   ✅ Row colors for maintenance (light green=paid, light red=not paid)
   ✅ Checkmarks (✅ Paid / ❌ Not Paid) for current month's maintenance

========================================================

📁 FILES IN maintance/ FOLDER:

app.py                          - Flask application (routes, models, logic)
migrate_db.py                   - Database migration script
init_db.py                      - Database initialization and seeding script
requirements.txt                - Python dependencies (Flask, Flask-SQLAlchemy)
templates/index.html            - Dashboard and management UI
maintenance.db                  - SQLite database (auto-created)
README.md                        - User guide and quick start
test_maintenance.py             - Smoke tests for month-wise maintenance
check_cols.py                   - Utility to check database columns
smoke_test.py                   - General smoke tests (legacy)
debug_post.py                   - Debug utility for POST requests (legacy)

========================================================

🚀 HOW TO LAUNCH:

Option 1: Quick start (assumes Python installed)
---
cd C:\Users\USER\PycharmProjects\python_practice\maintance
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
python migrate_db.py
python app.py

Then open: http://127.0.0.1:5000/

Option 2: If DB is fresh
---
cd C:\Users\USER\PycharmProjects\python_practice\maintance
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
python init_db.py
python app.py

Then open: http://127.0.0.1:5000/

========================================================

📊 HOW TO USE:

1. View Dashboard:
   - Open http://127.0.0.1:5000/
   - See summary cards: Total, Paid, Not Paid, Available, Rented, Occupied, Maintenance Paid

2. Manage a House:
   - Find house in table (e.g., H-001)
   - Change Payment Status: Select dropdown → Click Set
   - Change Availability: Select dropdown → Click Set
   - Add Maintenance: Click month picker → Select month → Click "+ Month"
   - Remove Maintenance: If current month is paid, click "- Remove"

3. Export Data:
   - Click "Export CSV" link
   - File houses.csv is downloaded
   - Contains: house_number, payment_status, availability, maintenance_paid_months
   - Example row: H-001,paid,rented,2026-02,2026-03

4. Add New House:
   - Fill in house number (e.g., H-484)
   - Select payment status (default: Not Paid)
   - Select availability (default: Available)
   - Click "Add House"

========================================================

✅ VERIFIED & TESTED:

✅ Migration script adds missing columns successfully
✅ Index page loads with all data
✅ Setting payment status works
✅ Setting availability works
✅ Adding maintenance month works
✅ Removing maintenance month works
✅ CSV export includes all fields
✅ Current month maintenance status shows correctly
✅ Visual indicators update properly

Test Results: ALL SMOKE TESTS PASSED ✅

========================================================

🔧 TROUBLESHOOTING:

If you get "no such column" errors:
   → Run: python migrate_db.py

If port 5000 is busy:
   → Edit app.py last line: app.run(debug=True, port=5001)

If database is corrupted:
   → Delete maintenance.db and run: python init_db.py

If dependencies missing:
   → Ensure venv is activated and run: pip install -r requirements.txt

========================================================

📝 DATABASE SCHEMA:

House table:
   - house_number (TEXT, PRIMARY KEY)       - House ID (H-001, H-002, ... H-483)
   - payment_status (TEXT)                  - 'paid' or 'not_paid'
   - availability (TEXT)                    - 'available', 'rented', or 'occupied'
   - maintenance_paid_months (TEXT)         - Comma-separated months (e.g., '2026-02,2026-03')
   - status (TEXT) [legacy]                 - Old field, kept for compatibility

========================================================

🎯 NEXT ENHANCEMENTS (Optional):

- Add authentication (login/password)
- Add pagination for 483 houses table
- Add search/filter by house number
- Add reports (paid % per month, etc.)
- Add bulk import/update from CSV
- Add multi-month maintenance selection
- Add notes field per house
- Add date range filters
- Add analytics dashboard
- Add user roles (admin, staff, viewer)

========================================================

