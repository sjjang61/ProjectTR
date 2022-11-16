import requests
import json, logging
from flask import request, jsonify, make_response

from . import user
from database import db_session
from model import User, UserHero, UserSquad
from common.dataUtils import obj_to_dict

def get_all_user():
    # users = User.query.all()
    return User.query. \
        join(UserHero, User.user_id == UserHero.user_id, isouter=True). \
        join(UserSquad, User.user_id == UserSquad.user_id, isouter=True). \
        all()

def get_user( user_id ):
    # return User.query.filter_by(user_id=user_id).first()
    # return User.query.filter_by(user_id=user_id).join(UserHero).filter_by(user_id=user_id).one()
    return User.query.filter_by(user_id=user_id).\
        join(UserHero, User.user_id == UserHero.user_id, isouter=True). \
        join(UserSquad, User.user_id == UserSquad.user_id, isouter=True). \
        first()

# user object -> dictionary
def get_user_dict( user ):
    dict = obj_to_dict(user)

    heroes = []
    for hero in user.heroes:
        # print("[hero] ", hero)
        heroes.append(hero.hero_id)
    dict['heroes'] = heroes

    squads = []
    for squad in user.squads:
        # print("[squad] ", squad)
        dict_squad = obj_to_dict(squad)
        del dict_squad['user_id']
        squads.append( dict_squad )

    dict['squads'] = squads

    return dict


# attach a handler for logging
# logger = get_task_logger(__name__)

@user.route('/', methods=['GET'])
def select_list():
    print("[get] user list")

    res = []
    users = get_all_user()
    print("[get] user list = ", users, type(users))

    for user in users:
        res.append( get_user_dict( user))

    return json.dumps(res)


@user.route('/<int:user_id>/', methods=['GET'])
def select(user_id):
    print("[get] user")
    user = get_user( user_id )
    print("[get] res user = %r, %r, %r" % (  user, user.squads, user.heroes) )
    return json.dumps( get_user_dict(user) )

@user.route('/', methods=['POST'])
def post():
    id = request.form['id']
    name = request.form['name']
    print("[post] user = ( %s, %s )" %( id, name ))

    user = User( id, name )
    try:
        db_session.add(user)
        db_session.commit()
        print("user was commited, user_id = ", user.user_id)
        # db_session.close()
    except:
        db_session.rollback()

    user = get_user( user.user_id )
    return json.dumps( obj_to_dict(user))


@user.route('/<int:user_id>/', methods=['PUT'])
def put( user_id ):
    id = request.form['id']
    name = request.form['name']
    print("[put] user = ( user_id:%d, id:%s, name:%s )" %( user_id, id, name ))

    try:
        db_session.query(User).filter_by(user_id=user_id).update( values={ 'id' : id, 'name' : name })
        print("user was commited")
        db_session.commit()
        # db_session.close()
    except Exception as e:
        print("[EXCEPTION] put, message = %s" % ( e ))
        db_session.rollback()

    user = get_user(user_id)
    return json.dumps( obj_to_dict(user))

@user.route('/<int:user_id>/', methods=['DELETE'])
def delete( user_id ):
    print("[delete] user = ( user_id:%d )" % (user_id))
    try:
        db_session.query(User).filter_by(user_id=user_id).delete()
        print("user was commited")
        db_session.commit()
    except Exception as e:
        print("[EXCEPTION] user delete, message = %s" % ( e ))
        db_session.rollback()

    data = { 'success' : True }
    return make_response( jsonify(data), 200 )
