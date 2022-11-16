import json
from flask import request, jsonify, make_response
from . import squad
from common.dataUtils import obj_to_dict
from model import User, UserSquad
from database import db_session

# user object -> dictionary
def get_user_squad_dict( squad ):
    dict = obj_to_dict(squad)
    del dict['user_id']
    return dict

def get_user_squad( user_id, hero_id = 0 ):
    if hero_id == 0 :
        return UserSquad.query.filter_by(user_id=user_id).all()

    return UserSquad.query.filter_by(user_id=user_id, hero_id= hero_id ).first()

@squad.route('/', methods=['GET'])
def select_list( user_id ):
    print("[squad] list = ", user_id )

    response = []
    squades = get_user_squad( user_id )
    for squad in squades:
        response.append( get_user_squad_dict( squad ))

    # print( response )
    return json.dumps( response )

# [nouse] 의미가 없음
@squad.route('/<int:hero_id>/', methods=['GET'])
def select(user_id, hero_id):
    print("[squad] get  = ", user_id, hero_id )
    squad = get_user_squad(user_id, hero_id )
    return json.dumps( get_user_squad_dict( squad ))

@squad.route('/', methods=['POST'])
def post( user_id ):
    hero_id = request.form['hero_id']
    pos_x = request.form['pos_x']
    pos_y = request.form['pos_y']

    print("[post] squad = ( %s, %s, pos_x:%r, pos_y:%r )" % (user_id, hero_id, pos_x, pos_y ))

    squad = UserSquad(user_id, hero_id, pos_x, pos_y)
    try:
        db_session.add(squad)
        db_session.commit()
        print("squad was commited")
        # db_session.close()
    except:
        db_session.rollback()

    squad = get_user_squad(user_id, hero_id)
    return json.dumps(obj_to_dict(squad))


# [nouse] 의미가 없음
@squad.route('/<int:hero_id>/', methods=['PUT'])
def update(user_id, hero_id):
    print("[squad] update ")
    return make_response( {}, 404)


@squad.route('/<int:hero_id>/', methods=['DELETE'])
def delete(user_id, hero_id):
    print("[squad] delete = ( user_id:%r, hero_id:%r)" %( user_id, hero_id ))

    try:
        db_session.query(UserSquad).filter_by(user_id=user_id, hero_id=hero_id).delete()
        print("commit : squad was deleted")
        db_session.commit()
    except Exception as e:
        print("[EXCEPTION] squad delete, message = %s" % ( e ))
        db_session.rollback()

    data = { 'success' : True }
    return make_response( jsonify(data), 200 )