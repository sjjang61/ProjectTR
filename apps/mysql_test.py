# from apps.common.dbUtils import db_utils

import apps.common.dbUtils as db_utils

user = "root"
password = "pjt!@#123"
host = "13.209.48.241"
database = "project_tr"
port = 3306

db_conn = db_utils.connect(host, port, user, password, database )

sql = 'select * from test'
df = db_utils.exec_read_sql(sql, db_conn)
print( "sql = ", df)