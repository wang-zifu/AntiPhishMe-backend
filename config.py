import os
import connexion
import logging 

# create an application instance

connexion_app = connexion.App(__name__, specification_dir='./swagger')

DEBUG = True
BASE_DIR = connexion_app.root_path
logging.basicConfig(format='[%(name)s %(levelname)s %(asctime)s]  %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

SQL_ALCH_DATABASE = None 
#
#   ===================================
#   DATABASE_DIALECT: postgresql+pg8000
#   DATABASE_USER: username
#   DATABASE_PASS: password
#   DATABASE_IP: ip(:port)
#   DATABASE_NAME: database
#   ===================================
#
if os.environ.get('DATABASE_DIALECT') and os.environ.get('DATABASE_USER') and os.environ.get('DATABASE_PASS') and os.environ.get('DATABASE_IP') and os.environ.get('DATABASE_NAME'):
    SQL_ALCH_DATABASE = f"{os.environ.get('DATABASE_DIALECT')}://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASS')}@{os.environ.get('DATABASE_IP')}/{os.environ.get('DATABASE_NAME')}"
    logging.debug(f"[DATABASE] Using external database with dialect {os.environ.get('DATABASE_DIALECT')}")
else:
    logging.debug('[DATABASE] Either DATABASE_DIALECT, DATABASE_USER, DATABASE_PASS, DATABASE_URL or DATABASE_NAME is missing')
    logging.debug('[DATABASE] Using default sqlite database')
    pass
SQLALCHEMY_DATABASE_URI = SQL_ALCH_DATABASE or 'sqlite:///' + os.path.join(BASE_DIR, 'database/phishing.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(connexion_app.root_path, 'database/database.db')

connexion_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
connexion_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

connexion_app.add_api('swagger.yml')
