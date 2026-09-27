import sqlite3
conn = sqlite3.connect('maintenance.db')
cur = conn.cursor()
cur.execute("PRAGMA table_info('house')")
cols = cur.fetchall()
print('Current columns:')
for c in cols:
    print(f'  {c[1]}: {c[2]}')
conn.close()

