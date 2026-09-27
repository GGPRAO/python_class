from app import db, House, app
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maintenance.db')

# Seed 483 houses with default status 'not_paid'

def seed():
    if House.query.count() >= 483:
        print('Already seeded')
        return
    for i in range(1, 484):
        num = f'H-{i:03d}'
        # Use house_number as primary key
        h = House(house_number=num, status='not_paid')
        db.session.add(h)
    db.session.commit()
    print('Seeded 483 houses')

if __name__ == '__main__':
    # If DB exists, try to remove it so schema changes apply cleanly
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
            print('Removed existing database to apply schema changes')
        except PermissionError:
            print('Warning: could not remove existing database (PermissionError). Continuing without deleting. Ensure no other process is locking the DB.')

    # Use the Flask application context to perform DB operations
    with app.app_context():
        db.create_all()
        seed()
