#FIXME : The code below shoud be refactored!
# Task Logging
LOGGING = True
LOG_OUTPUT = ".\\resource\\log\\task_log.log"
# Flask-BootStrap
BOOTSTRAP_SERVE_LOCAL = True

# dbhost = '27.102.197.60'
# dbuser = 'root'
# dbpass = 'pickstar'
# dbname = 'pickstar'
# DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' +dbname + '?charset=utf8&use_unicode=0'

dbuser = "root"
dbpass = "pjt!@#123"
dbhost = "13.209.48.241"
dbname = "project_tr"
port = 3306
DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' +dbname + '?charset=utf8&use_unicode=0'


# Flask Configuration
SECRET_KEY = 'devkey'
