import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maintenance.db')

if not os.path.exists(DB_PATH):
    print('No database file found at', DB_PATH)
    print('Run init_db.py to create and seed the database.')
    raise SystemExit(1)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Get existing columns
cur.execute("PRAGMA table_info('house')")
cols = [r[1] for r in cur.fetchall()]
print('Existing columns:', cols)

# Add payment_status if missing
if 'payment_status' not in cols:
    print('Adding column payment_status')
    cur.execute("ALTER TABLE house ADD COLUMN payment_status TEXT DEFAULT 'not_paid'")
else:
    print('payment_status already exists')

# Add availability if missing
if 'availability' not in cols:
    print('Adding column availability')
    cur.execute("ALTER TABLE house ADD COLUMN availability TEXT DEFAULT 'available'")
else:
    print('availability already exists')

# Add maintenance_paid_months if missing
if 'maintenance_paid_months' not in cols:
    print('Adding column maintenance_paid_months')
    try:
        cur.execute("ALTER TABLE house ADD COLUMN maintenance_paid_months TEXT DEFAULT ''")
        print('Successfully added maintenance_paid_months')
    except sqlite3.OperationalError as e:
        print(f'Error adding maintenance_paid_months: {e}')
else:
    print('maintenance_paid_months already exists')

conn.commit()

# Ensure no NULLs (set defaults where necessary)
cur.execute("UPDATE house SET payment_status='not_paid' WHERE payment_status IS NULL")
cur.execute("UPDATE house SET availability='available' WHERE availability IS NULL")
cur.execute("UPDATE house SET maintenance_paid_months='' WHERE maintenance_paid_months IS NULL")
conn.commit()

print('Migration complete.')

# Final check
cur.execute("PRAGMA table_info('house')")
cols_after = [r[1] for r in cur.fetchall()]
print('Columns after migration:', cols_after)

conn.close()
