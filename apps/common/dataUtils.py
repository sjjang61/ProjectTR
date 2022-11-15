def obj_to_dict( obj ):
    # return {column: str(getattr(obj, column)) for column in obj.__table__.c.keys()}
    dict = {}
    for column in obj.__table__.c.keys():
        dict[column] = getattr(obj, column)
        # print( "[obj -> dict] %s = %s" %( column, getattr(obj, column) ))

    return dict