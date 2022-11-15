# from serverApplication import app
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
#
# user = "root"
# password = "pjt!@#123"
# host = "13.209.48.241"
# database = "project_tr"
# port = 3306
#
# db_url = sqlalchemy.engine.URL.create(
#     drivername="mysql",
#     username=user,
#     password=password,
#     host=host,
#     port=port,
#     database=database,
# )
# # app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql://{user}:{password}@{host}:{port}/{database}")
# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 3600
# app.config["WTF_CSRF_ENABLED"] = True
# app.config["SECRET_KEY"] = 'whatever'
# db = SQLAlchemy(app)

# db.create_all()
# print("DB created.")


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
import settings

db_url = sqlalchemy.engine.URL.create(
    drivername="mysql",
    username=settings.dbuser,
    password=settings.dbpass,
    host=settings.dbhost,
    port=settings.port,
    database=settings.dbname,
)
engine = create_engine(db_url, convert_unicode=True, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# from sqlalchemy.ext.declarative import as_declarative
#
# @as_declarative()
# class Base:
#     def _asdict(self):
#         return {c.key: getattr(self, c.key)
#                 for c in inspect(self).mapper.column_attrs}

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
