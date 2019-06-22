import os

from dotenv import load_dotenv

# Initialize environment variables
load_dotenv('.env')


PATH_TO_ORCA = os.environ.get('PATH_TO_ORCA')
SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')
LIST_OF_BENCHS = ['geek_bench4', 'sling_shot_extreme', 'antutu7',
                  'battery_test']
GOOGLE_CREDENTIAL_FILE = os.environ.get('GOOGLE_CREDENTIAL_FILE')
