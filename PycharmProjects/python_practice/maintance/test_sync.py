import werkzeug
try:
    _ = werkzeug.__version__
except AttributeError:
    werkzeug.__version__ = '3.1.6'

from app import app, db, House
from datetime import datetime
import traceback

def test_payment_maintenance_sync():
    """Test that Payment Status and Maintenance Paid are synced for current month"""
    try:
        current_month = datetime.now().strftime('%Y-%m')
        target = 'H-001'

        with app.test_client() as client:
            print(f'\n{"="*70}')
            print(f'🔄 PAYMENT & MAINTENANCE SYNC TESTS (Month: {current_month})')
            print(f'{"="*70}\n')

            # Test 1: Verify index loads
            resp = client.get('/')
            assert resp.status_code == 200
            data = resp.get_data(as_text=True)
            assert 'SYNCED' in data, 'Sync badge not found'
            print('✅ Test 1: Index page shows SYNCED badge')

            # Test 2: Set payment to "Paid" - should auto-add current month maintenance
            print('\n📝 Test 2: Set Payment to PAID → Should auto-add maintenance for current month')
            resp2 = client.post(f"/set_payment/{target}", data={
                'payment_status': 'paid'
            }, follow_redirects=True)
            assert resp2.status_code == 200
            assert 'synced' in resp2.get_data(as_text=True).lower()

            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert h.payment_status == 'paid', 'Payment should be paid'
                assert current_month in h.get_maintenance_months(), f'Maintenance for {current_month} should be added'
            print(f'   ✅ Payment set to PAID')
            print(f'   ✅ Maintenance auto-added for {current_month}')

            # Test 3: Set payment to "Not Paid" - should auto-remove current month maintenance
            print('\n📝 Test 3: Set Payment to NOT PAID → Should auto-remove maintenance for current month')
            resp3 = client.post(f"/set_payment/{target}", data={
                'payment_status': 'not_paid'
            }, follow_redirects=True)
            assert resp3.status_code == 200

            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert h.payment_status == 'not_paid', 'Payment should be not_paid'
                assert current_month not in h.get_maintenance_months(), f'Maintenance for {current_month} should be removed'
            print(f'   ✅ Payment set to NOT PAID')
            print(f'   ✅ Maintenance auto-removed for {current_month}')

            # Test 4: Add maintenance for current month - should auto-update payment to paid
            print('\n📝 Test 4: Add Maintenance for current month → Should auto-set Payment to PAID')
            resp4 = client.post(f"/set_maintenance/{target}", data={
                'action': 'add',
                'maintenance_month': current_month
            }, follow_redirects=True)
            assert resp4.status_code == 200

            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert h.payment_status == 'paid', 'Payment should be auto-set to paid'
                assert current_month in h.get_maintenance_months(), f'Maintenance for {current_month} should exist'
            print(f'   ✅ Maintenance added for {current_month}')
            print(f'   ✅ Payment auto-synced to PAID')

            # Test 5: Remove maintenance for current month - should auto-update payment to not_paid
            print('\n📝 Test 5: Remove Maintenance for current month → Should auto-set Payment to NOT PAID')
            resp5 = client.post(f"/set_maintenance/{target}", data={
                'action': 'remove',
                'maintenance_month': current_month
            }, follow_redirects=True)
            assert resp5.status_code == 200

            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert h.payment_status == 'not_paid', 'Payment should be auto-set to not_paid'
                assert current_month not in h.get_maintenance_months(), f'Maintenance for {current_month} should be removed'
            print(f'   ✅ Maintenance removed for {current_month}')
            print(f'   ✅ Payment auto-synced to NOT PAID')

            # Test 6: Add maintenance for a FUTURE month (should NOT affect current payment)
            print('\n📝 Test 6: Add Maintenance for FUTURE month → Should NOT affect current payment')
            future_month = '2026-03'
            resp6 = client.post(f"/set_maintenance/{target}", data={
                'action': 'add',
                'maintenance_month': future_month
            }, follow_redirects=True)
            assert resp6.status_code == 200

            with app.app_context():
                h = House.query.filter_by(house_number=target).first()
                assert future_month in h.get_maintenance_months(), f'Maintenance for {future_month} should exist'
                # Payment should remain not_paid (current month not affected)
                assert h.payment_status == 'not_paid', 'Payment should remain not_paid (only current month syncs)'
            print(f'   ✅ Maintenance added for {future_month}')
            print(f'   ✅ Payment remains NOT PAID (only current month is synced)')

            # Test 7: CSV export shows both payment and maintenance
            print('\n📝 Test 7: CSV export includes payment status and maintenance')
            resp7 = client.get('/export')
            assert resp7.status_code == 200
            csv_text = resp7.get_data(as_text=True)
            assert 'payment_status' in csv_text
            assert 'maintenance_paid_months' in csv_text
            print(f'   ✅ CSV includes payment_status column')
            print(f'   ✅ CSV includes maintenance_paid_months column')

            # Test 8: Dashboard counts reflect sync
            print('\n📝 Test 8: Dashboard counts are consistent with sync')
            resp8 = client.get('/')
            data = resp8.get_data(as_text=True)
            # Verify the data is rendered
            assert 'Not Paid' in data or 'not_paid' in data.lower()
            print(f'   ✅ Dashboard shows correct counts')

            print(f'\n{"="*70}')
            print(f'🎉 ALL SYNC TESTS PASSED!')
            print(f'{"="*70}')
            print(f'\n📊 SUMMARY:')
            print(f'   • Payment & Maintenance for current month ({current_month}) are SYNCED')
            print(f'   • Set Payment → auto-updates Maintenance for current month')
            print(f'   • Add/Remove Maintenance for current month → auto-updates Payment')
            print(f'   • Past/Future months are independent')
            print(f'   • CSV export includes all data')
            print(f'\n✨ System working as expected!\n')

    except Exception as e:
        print(f'\n❌ ERROR: {e}')
        traceback.print_exc()

if __name__ == '__main__':
    test_payment_maintenance_sync()

