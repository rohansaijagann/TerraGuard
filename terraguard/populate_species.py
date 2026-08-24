import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terraguard.settings')
django.setup()

from django.core.management import call_command

if __name__ == '__main__':
    print('Running seed_data command via populate_species.py compatibility wrapper...')
    try:
        call_command('seed_data')
        print('Seed data completed successfully!')
    except Exception as e:
        print(f'Notice: seed_data exception (non-fatal): {e}')
