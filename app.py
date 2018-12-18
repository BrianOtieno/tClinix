from flask_migrate import Migrate
from os import environ
from pathlib import Path
from sys import exit

from config import config_dict
from tClinix import create_app, db

get_config_mode = environ.get('TCLINIX_CONFIG_MODE', 'Debug')
print("config mode = " + get_config_mode)
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid TCLINIX_CONFIG_MODE environment variable entry.')

app = create_app(Path.cwd(), config_mode)
Migrate(app, db)

print("Migrated!")
if __name__=='__main__':
    app.run()
