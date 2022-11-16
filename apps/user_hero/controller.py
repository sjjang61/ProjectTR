import json
from flask import request, jsonify, make_response
from . import hero
from common.dataUtils import obj_to_dict
from model import User, UserHero
from database import db_session

# user object -> dictionary
def get_user_hero_dict( hero ):
    return hero.hero_id

def get_user_hero( user_id, hero_id = 0 ):
    if hero_id == 0 :
        return UserHero.query.filter_by(user_id=user_id).all()

    return UserHero.query.filter_by(user_id=user_id, hero_id= hero_id ).first()

@hero.route('/', methods=['GET'])
def select_list( user_id ):
    print("[hero] list = ", user_id )

    response = []
    heroes = get_user_hero( user_id )
    for hero in heroes:
        response.append( get_user_hero_dict( hero ))

    # print( response )
    return json.dumps( response )

# [nouse] 의미가 없음
@hero.route('/<int:hero_id>/', methods=['GET'])
def select(user_id, hero_id):
    print("[hero] get  = ",  user_id, hero_id )
    hero = get_user_hero(user_id, hero_id )
    return json.dumps( get_user_hero_dict( hero ))

@hero.route('/', methods=['POST'])
def post( user_id ):
    hero_id = request.form['hero_id']
    print("[post] hero = ( %s, %s )" % (user_id, hero_id))

    hero = UserHero(user_id, hero_id)
    try:
        db_session.add(hero)
        db_session.commit()
        print("hero was commited")
        # db_session.close()
    except:
        db_session.rollback()

    hero = get_user_hero(user_id, hero_id)
    return json.dumps(obj_to_dict(hero))


# [nouse] 의미가 없음
@hero.route('/<int:hero_id>/', methods=['PUT'])
def update(user_id, hero_id):
    print("[hero] update ")
    return make_response( {}, 404)


@hero.route('/<int:hero_id>/', methods=['DELETE'])
def delete(user_id, hero_id):
    print("[hero] delete = ( user_id:%r, hero_id:%r)" %( user_id, hero_id ))

    try:
        db_session.query(UserHero).filter_by(user_id=user_id, hero_id=hero_id).delete()
        print("commit : hero was deleted")
        db_session.commit()
    except Exception as e:
        print("[EXCEPTION] hero delete, message = %s" % ( e ))
        db_session.rollback()

    data = { 'success' : True }
    return make_response( jsonify(data), 200 )