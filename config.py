import os

basedir = os.path.abspath(os.path.dirname(__file__))

account_sid = "AC40f5201186378f3d191189033af5f25f"

auth_token = "c97192da5b1db09f80a516037a022cd6"

minion_assembler = "+17327023043"


SECRET_KEY = 'Chile is not a frog'

SQLALCHEMY_DATABASE_URI = 'mysql://minions:minions@localhost/minions'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OAUTH_CREDENTIALS = {
    'minions': {
        'id': '',
        'secret': ''
    }
}

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

LOG_FILENAME = "minions.log"

LOG_FORMAT = ""

ALLOWED_EXTENSIONS = ["pdf"]
