Maintenance Management for Prajay Water Front Phase 2

This Flask web app manages 483 houses with tracking for:
- Payment status (Paid / Not Paid)
- Availability (Available / Rented / Occupied)
- **Month-wise Maintenance** (Paid / Not Paid per month)

Quick start:

1. Create a virtualenv and install requirements:

   python -m venv .venv
   .\.venv\Scripts\Activate
   pip install -r requirements.txt

2. Run the database migration (if needed) to add new columns:

   python migrate_db.py

3. Run the app:

   python app.py

4. Open in browser:

   http://127.0.0.1:5000/

Features:

✅ Dashboard Summary:
   - Total Houses (483)
   - Paid / Not Paid houses
   - Available / Rented / Occupied houses
   - Maintenance Paid for current month

✅ Per-House Management:
   - Set payment status (Paid / Not Paid)
   - Set availability (Available / Rented / Occupied)
   - Add/Remove maintenance month (month picker input)
   - Visual indicators (✅ Paid / ❌ Not Paid) for current month's maintenance

✅ CSV Export:
   - Download full house list with all fields (payment_status, availability, maintenance_paid_months)
   - maintenance_paid_months is comma-separated list of months (e.g., "2026-02,2026-03")

Example: Add maintenance for February 2026:
   1. Click the month picker next to a house row
   2. Select 2026-02
   3. Click "+ Month"
   4. The row highlights green (✅ Paid)
   5. To remove, click "- Remove" button when current month is paid

Smoke Tests:

Run test_maintenance.py to verify month-wise functionality:

   python test_maintenance.py

This tests:
   - Adding maintenance month
   - Storing in DB
   - CSV export includes months
   - Removing maintenance month
