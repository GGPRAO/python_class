import werkzeug
try:
    _ = werkzeug.__version__
except AttributeError:
    werkzeug.__version__ = '3.1.6'

from app import app, db, House
from datetime import datetime
import traceback

def run_smoke():
    try:
        current_month = datetime.now().strftime('%Y-%m')
        target = 'H-001'

        with app.test_client() as client:
            # Test 1: GET index page
            resp = client.get('/')
            assert resp.status_code == 200, f'Index returned {resp.status_code}'
            data = resp.get_data(as_text=True)
            assert 'Maintenance Management' in data, 'Title not found'
            print('✅ Index page loads')

            # Test 2: Add maintenance month for current month
            resp2 = client.post(f"/set_maintenance/{target}", data={
                'action': 'add',
                'maintenance_month': current_month
            }, follow_redirects=True)
            assert resp2.status_code == 200, f'POST /set_maintenance returned {resp2.status_code}'
            print('✅ Add maintenance month works')

            # Test 3: Verify in DB
            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert h is not None, f'House {target} not found'
                assert current_month in h.get_maintenance_months(), f'Month {current_month} not in maintenance list'
            print('✅ Maintenance month stored in DB')

            # Test 4: Verify CSV export includes maintenance
            resp3 = client.get('/export')
            assert resp3.status_code == 200
            csv_text = resp3.get_data(as_text=True)
            assert 'maintenance_paid_months' in csv_text
            assert current_month in csv_text
            print('✅ CSV export includes maintenance months')

            # Test 5: Remove maintenance month
            resp4 = client.post(f"/set_maintenance/{target}", data={
                'action': 'remove',
                'maintenance_month': current_month
            }, follow_redirects=True)
            assert resp4.status_code == 200
            print('✅ Remove maintenance month works')

            # Test 6: Verify removal in DB
            with app.app_context():
                h2 = House.query.filter_by(house_number=target).first()
                assert current_month not in h2.get_maintenance_months(), f'Month {current_month} still in list'
            print('✅ Maintenance month removed from DB')

            print('\n🎉 ALL SMOKE TESTS PASSED: Month-wise maintenance tracking works!')
    except Exception as e:
        print(f'ERROR: {e}')
        traceback.print_exc()

if __name__ == '__main__':
    run_smoke()
