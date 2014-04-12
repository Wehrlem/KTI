from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'KTI Dashboard'
settings.subtitle = 'Trends for tourism'
settings.author = 'Marcel Wehrle'
settings.author_email = 'marcel@unifr.ch'
settings.keywords = ''
settings.description = 'Dashboard to visualize data collected for the KTI - project'
settings.layout_theme = 'Default'
settings.database_uri = 'mongodb://admin:grid@localhost/ktidasboard'
settings.security_key = 'b303b7b6-da8b-42f1-934f-65cde2f243b3'
settings.email_server = 'localhost'
settings.email_sender = 'marcel.wehrle@unifr.ch'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
