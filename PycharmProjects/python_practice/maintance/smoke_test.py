import werkzeug
try:
    _ = werkzeug.__version__
except AttributeError:
    werkzeug.__version__ = '3.1.6'

from app import app, db, House


def run_smoke():
    # Use app context so DB queries work
    with app.app_context():
        total = House.query.count()
        # pick a house to change
        target = 'H-001'
        h = House.query.filter_by(house_number=target).first()
        assert h is not None, f'Target house {target} missing'

    # Use test client to request index page
    with app.test_client() as client:
        resp = client.get('/')
        print('GET / status', resp.status_code)
        data = resp.get_data(as_text=True)
        print('Index page length', len(data))
        assert resp.status_code == 200, f'Index returned {resp.status_code}'
        assert str(total) in data, 'Total count not found in page'

        # change payment status of H-001 to 'paid'
        resp2 = client.post(f"/set_payment/{target}", data={'payment_status': 'paid'}, follow_redirects=True)
        print('POST /set_payment status', resp2.status_code)
        print(resp2.get_data(as_text=True)[:1000])
        assert resp2.status_code == 200

        # change availability of H-001 to 'rented'
        resp3 = client.post(f"/set_availability/{target}", data={'availability': 'rented'}, follow_redirects=True)
        print('POST /set_availability status', resp3.status_code)
        print(resp3.get_data(as_text=True)[:1000])
        assert resp3.status_code == 200

        # confirm in DB the status was updated
        with app.app_context():
            h2 = House.query.filter_by(house_number=target).first()
            assert h2.payment_status == 'paid', f'Expected payment_status paid, found {h2.payment_status}'
            assert h2.availability == 'rented', f'Expected availability rented, found {h2.availability}'

        # export CSV and verify target row exists and matches
        resp4 = client.get('/export')
        print('GET /export status', resp4.status_code)
        csv_text = resp4.get_data(as_text=True)
        print(csv_text.splitlines()[:3])
        assert resp4.status_code == 200
        assert 'house_number,payment_status,availability' in csv_text
        assert f"{target},paid,rented" in csv_text

        print('SMOKE TEST PASS: index, set_payment, set_availability, and export CSV behave as expected')

if __name__ == '__main__':
    run_smoke()
