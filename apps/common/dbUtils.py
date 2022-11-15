# -*- coding: utf-8 -*-
import pymysql
import pandas as pd

def connect( db_ip, db_port, db_user, db_pass, db_scheme ):

    conn = pymysql.connect( host=db_ip, user=db_user, password = db_pass, db= db_scheme, charset="utf8" )
    # `SQLALCHEMY_DATABASE_URI = 'mysql://root:nhn!@#123@49.50.161.172:3306/dreamteam_db'
    return conn

def disconnect( conn ):
    conn.close()

# SQL 실행
def exec_read_sql( sql, conn ):
    # cur = conn.cursor()
    # cur.execute( sql )
    # result = cur.fetchall()
    return pd.read_sql( sql, conn )

def exec_write_sql( sql, conn, is_autocommit = False ):
    cur = conn.cursor()
    effect_rows = cur.execute( sql )
    print( effect_rows )

    if is_autocommit == True:
        conn.commit()

    return effect_rows

def commit( conn ):
    conn.commit()

def rollback( conn ):
    conn.rollback()

def get_table_list( conn, db_scheme, except_list = [] ):
    '''
    DB 스키마 내의 테이블 리스트 조회
    :param conn: DBConnection
    :param db_scheme: DB 스키마
    :param except_list: [ 제외 테이블명 리스트 ]
    :return: [ 테이블명 리스트 ]
    '''
    sql = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '%s' AND table_name not in ( '%s' )
    """ % ( db_scheme, "','".join( except_list ))
    # print( sql )

    df = exec_read_sql(sql, conn )
    return df['TABLE_NAME'].tolist()


def is_exist_table( conn, table_name, db_schema = "min_craw" ):
    sql = """
        select 1 
        from information_schema.tables 
        where table_schema = '%s' and table_name = '%s'
    """ % ( db_schema, table_name )

    rows = exec_read_sql(sql, conn )
    return len(rows) == 1

