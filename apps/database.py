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

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
