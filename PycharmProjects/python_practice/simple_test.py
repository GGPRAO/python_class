import sys
import os
os.chdir(r'C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications')
sys.path.insert(0, '.')

# Step 1
print('TEST 1')
sys.stdout.flush()

try:
    from gmail.gmail_config import GmailConfig
    print('TEST 2 - CONFIG OK')
    sys.stdout.flush()
except Exception as e:
    print(f'CONFIG ERROR: {e}')
    sys.stdout.flush()
    import traceback
    traceback.print_exc()

try:
    from gmail.gmail_service import GmailService
    print('TEST 3 - SERVICE OK')
    sys.stdout.flush()
except Exception as e:
    print(f'SERVICE ERROR: {e}')
    sys.stdout.flush()
    import traceback
    traceback.print_exc()

try:
    from gmail import get_chatbot_adapter
    print('TEST 4 - ADAPTER OK')
    sys.stdout.flush()
except Exception as e:
    print(f'ADAPTER ERROR: {e}')
    sys.stdout.flush()
    import traceback
    traceback.print_exc()

print('DONE')
sys.stdout.flush()

