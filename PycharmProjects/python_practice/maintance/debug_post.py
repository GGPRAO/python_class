import traceback
import werkzeug
try:
    _ = werkzeug.__version__
except AttributeError:
    werkzeug.__version__ = '3.1.6'

from app import app

try:
    with app.test_client() as client:
        target = 'H-001'
        print('GET /')
        r = client.get('/')
        print('GET / status', r.status_code)
        print('---')
        print('POST /set_payment')
        r2 = client.post(f"/set_payment/{target}", data={'payment_status':'paid'}, follow_redirects=True)
        print('status', r2.status_code)
        print('headers', r2.headers)
        print('data snippet:', r2.get_data(as_text=True)[:400])
        print('---')
        print('POST /set_availability')
        r3 = client.post(f"/set_availability/{target}", data={'availability':'rented'}, follow_redirects=True)
        print('status', r3.status_code)
        print('headers', r3.headers)
        print('data snippet:', r3.get_data(as_text=True)[:400])
        print('---')
        r4 = client.get('/export')
        print('GET /export status', r4.status_code)
        print(r4.get_data(as_text=True)[:400])
except Exception:
    traceback.print_exc()
