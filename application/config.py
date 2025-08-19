class config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
class LocalDevelopmentConfig(config):
    #configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.sqlite3"
    DEBUG = True
# congit for security
SECRET_KEY = "nkjd8273nvuh#@%$&^gng$^YJY67u8"
SECURITY_PASSWORD_HASH ="bcrypt"
SECURITY_PASSWORD_SALT = "Pass@nfjwe4454^^fsAAd" 
WTF_CSRF_ENABLED = False
SECUIRTY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Tocken"