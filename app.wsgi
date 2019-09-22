import sys
sys.path.insert(0, '/var/www/catalog_app')
sys.path.insert(0, '/var/www/catalog_app/fb_client_secrets.json')
from views import app as application
application.secret_key = 'super-secret-key'